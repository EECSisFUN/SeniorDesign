# uses a twitch api python library to get various twitch data 
from Apps import TwitchAuth

crl = None
byte_obj = None
myClientID = TwitchAuth.getClientId()
mySecret = TwitchAuth.getSecret()
# hello
def setup():
    global crl, byte_obj
    crl = pycurl.Curl()
    crl.setopt(pycurl.URL, "https://api.twitch.tv/helix")
    byte_obj = BytesIO()

def authHeader():
    global myClientID, mySecret
    return ['Authorization: Bearer ' + mySecret, 
            'Client-Id: ' + myClientID]

def topGames():
    # returns JSON of the top games
    crl.setopt(pycurl.URL, "https://api.twitch.tv/helix/games/top")
    crl.setopt(pycurl.HTTPHEADER, authHeader())
    crl.perform()
    #return crl.get("https://api.twitch.tv/helix/games/top", authHeader)

setup()

print(topGames())

