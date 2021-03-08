# uses a twitch api python library to get various twitch data 
#from Apps import TwitchAuth
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

def setup():
    global myClientID, mySecret, myOAuth, myRedirectUri, ircbot

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
        
        if r.status_code == 200:
            print('got twitch oAuth sucessful')
            TwitchAuth.setOAuth(r.json()['access_token'])
            myOAuth = TwitchAuth.getOAuth()
            

    # setup irc bot
    ircbot.connect(("irc.chat.twitch.tv", 6667))
    ircbot.send(("PASS " + myChannelOAuth + "\r\n").encode("utf-8"))
    ircbot.send(("NICK mazilla2017\r\n").encode("utf-8"))
    


def joinChannel(channel):
    ircbot.send("JOIN {}\r\n".format("#" + channel).encode("utf-8"))
    while True:
        response = ircbot.recv(1024).decode("utf-8")
        name = response[1:response.find("!")]
        msg = response[response.find(channel)+len(channel)+2:]
        print(name, ":", msg)
        time.sleep(.1)

def authHeader():
    global myClientID, mySecret, myOAuth
    return {
            'client-id' : myClientID,
            'Authorization' : ("Bearer " + myOAuth)
            }

def getTopGames():
    r = requests.get(url = "https://api.twitch.tv/helix/games/top", headers = authHeader())
    return r.json()

setup()
# print(topGames())
joinChannel("limmy")

