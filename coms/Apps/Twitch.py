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

ircbot = socket.socket()

joinedChannel = False # keeps track of if a channel is joined or not
joinedChannelName = ""

def setup():
    global myClientID, mySecret, myOAuth, myRedirectUri, ircbot, myChannelOAuth

    # get the OAuth
    if myOAuth == None:
        # get the OAuth
        head = {
            'client_id' : myClientID,
            'client_secret' : mySecret,
            'grant_type' : 'client_credentials',
            "scope": "chat:read"
            }
        r = requests.post(url = "https://id.twitch.tv/oauth2/token", data = head)
        #print(r.json())
        
        if r.status_code == 200:
            print('got twitch oAuth sucessful')
            TwitchAuth.setOAuth(r.json()['access_token'])
            myOAuth = TwitchAuth.getOAuth()

    # setup irc bot
    ircbot.connect(("irc.chat.twitch.tv", 6667))
    ircbot.send(("PASS " + myChannelOAuth + "\r\n").encode("utf-8"))
    ircbot.send(("NICK maxzilla2017\r\n").encode("utf-8"))
    


def joinChannel(channel):
    global joinedChannel, joinedChannelName
    ircbot.send(("JOIN #" + channel + "\r\n").encode("utf-8"))
    joinedChannel = True
    joinedChannelName = channel
   

def authHeader():
    global myClientID, mySecret, myOAuth
    return {
            'client-id' : myClientID,
            'Authorization' : ("Bearer " + myOAuth)
            }

def getTopGames():
    r = requests.get(url = "https://api.twitch.tv/helix/games/top", headers = authHeader())
    return r.json()

def getChat(channel):
    global joinedChannel, joinedChannelName

    if (joinedChannel == False or (joinChannel and joinedChannelName != channel)):
        joinChannel(channel)

    chat = []
    # bad, but were gonna get 3 seconds worth of chat for each call
    start = time.time()
    while (time.time() - start) < 2:
        response = ircbot.recv(1024).decode("utf-8")
        name = response[1:response.find("!")]
        msg = response[response.find(channel)+len(channel)+2:]
        if (len(msg) > 0):
            # print(name, ":", msg)
            chat.append((str(name), str(msg)))
        time.sleep(.1)
    return chat

def getFakeText():
    chat = {

    }
    currentTime = time.time()
    count = 0
    while (count < 50):
        chat[str(count)] = ["maxdgoad", "message" +  str(count)]
        count+=1
    return chat


#setup()
#print(getTopGames())


