# uses a twitch api python library to get various twitch data 
try:
    from Apps import TwitchAuth
except ModuleNotFoundError:
    import TwitchAuth
import requests
import socket
import time


myClientID = TwitchAuth.getClientId()
mySecret = TwitchAuth.getSecret()
myOAuth = TwitchAuth.getOAuth()
myRedirectUri = TwitchAuth.getRedirectUri()
myChannelOAuth = TwitchAuth.getChannelOAuth()
myUserID = TwitchAuth.getUserId()

ircbot = socket.socket()

joinedChannel = False # keeps track of if a channel is joined or not
joinedChannelName = ""

def setup():
    global myClientID, mySecret, myOAuth, myRedirectUri, ircbot, myChannelOAuth

    if myOAuth == None:
        attemptAuthenication()
    # get the OAuth
    if myOAuth == None:
        # get the OAuth
        head = {
            'client_id' : myClientID,
            'client_secret' : mySecret,
            'grant_type' : 'client_credentials',
            "scope": "moderation:read",
            }
        r = requests.post(url = "https://id.twitch.tv/oauth2/token", data = head)
        print(r.json())
        
        if r.status_code == 200:
            print('got twitch oAuth sucessful')
            TwitchAuth.setOAuth(r.json()['access_token'])
            myOAuth = TwitchAuth.getOAuth()

    # setup irc bot
    ircbot.connect(("irc.chat.twitch.tv", 6667))
    ircbot.send(("PASS " + myChannelOAuth + "\r\n").encode("utf-8"))
    ircbot.send(("NICK maxzilla2017\r\n").encode("utf-8"))
    
    
def attemptAuthenication():
    global myClientID, myRedirectUri
    head = {
            'client_id' : myClientID,
            'redirect_uri' : myRedirectUri,
            'response_type' : 'token',
            "scope": "analytics:read:games channel:edit:commercial channel:manage:broadcast channel:manage:extensions channel:read:stream_key channel:read:subscriptions moderation:read user:edit user:edit:follows user:manage:blocked_users user:read:blocked_users user:read:broadcast user:read:subscriptions",
            }
    r = requests.post(url = "https://id.twitch.tv/oauth2/authorize", params = head)
    print(r.url)
    print(r.json())

def joinChannel(channel):
    global joinedChannel, joinedChannelName
    ircbot.send(("JOIN #" + channel + "\r\n").encode("utf-8"))
    joinedChannel = True
    joinedChannelName = channel
   

def authHeader():
    global myClientID, mySecret, myOAuth
    return {
            'Client-ID' : myClientID,
            'Authorization' : ("Bearer " + myOAuth)
            }

def getTopGames():
    r = requests.get(url = "https://api.twitch.tv/helix/games/top", headers = authHeader())
    return r.json()

def getModerators():
    global myUserID
    myUrl = "https://api.twitch.tv/helix/moderation/moderators"
    r = requests.get(url = myUrl, params = {'broadcaster_id': myUserID}, headers = authHeader())
    return r.json()

def getBans():
    global myUserID
    myUrl = "https://api.twitch.tv/helix/moderation/banned"
    r = requests.get(url = myUrl, params = {'broadcaster_id': myUserID}, headers = authHeader())
    return r.json()

def getSubscriptions():
    global myUserID
    myUrl = "https://api.twitch.tv/helix/subscriptions"
    r = requests.get(url = myUrl, params = {'broadcaster_id': myUserID}, headers = authHeader())
    return r.json()

def checkSubscribed(username):
    global myUserID
    user = getUserId(username)['data'][0]["id"]
    print(myUserID, user)
    myUrl = "https://api.twitch.tv/helix/subscriptions/user"
    r = requests.get(url = myUrl, params = {'broadcaster_id': myUserID, 'user_id': user}, headers = authHeader())
    return r.json()


def getUserId(username):
    r = requests.get(url = "https://api.twitch.tv/helix/users?login=" + username, headers = authHeader())
    return r.json()

def updateDescription(desc):
    global myUserID
    myUrl = "https://api.twitch.tv/helix/users"
    r = requests.put(url = myUrl, params = {'description': desc}, headers = authHeader())
    return r.json()

def commercialHeader():
    global myClientID, mySecret, myOAuth
    return {
            'Client-ID' : myClientID,
            'Authorization' : ("Bearer " + myOAuth),
            'Content-Type' : "application/json"
            }

def startCommercial():
    global myUserID
    myUrl = "https://api.twitch.tv/helix/channels/commercial"
    data = '{"broadcaster_id":' + myUserID + ', "length" : 60}'
    r = requests.post(url = myUrl, headers = commercialHeader(), data = data)
    return r.json()

def v5Header():
    global myClientID, mySecret, myOAuth
    return {
            'Client-ID' : myClientID,
            'Accept' : 'application/vnd.twitchtv.v5+json'
            }

def getViewerCount():
    global myUserID
    myUrl = "https://api.twitch.tv/kraken/streams/" + myUserID
    r = requests.get(url = myUrl, headers = v5Header())
    return r.json()['stream']['viewers']

def getChat(channel):
    global joinedChannel, joinedChannelName

    if (joinedChannel == False or (joinChannel and joinedChannelName != channel)):
        joinChannel(channel)

    chat = []
    # bad, but were gonna get 3 seconds worth of chat for each call
    start = time.time()
    print('here! in chat1')
    while (time.time() - start) < 3:
        response = ircbot.recv(2040).decode()
        name = response[1:response.find("!")]
        msg = response[response.find(channel)+len(channel)+2:]
        if (len(msg) > 0):
            # print(name, ":", msg)
            chat.append((str(name), str(msg)))
    print('here! in chat2')
    print(chat)
    return chat


#setup()


