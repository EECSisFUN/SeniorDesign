from plexapi.myplex import MyPlexAccount
from plexapi.server import PlexServer

import plexapi
# from Apps import PlexAuth # running with main
try:
    from Apps import PlexAuth
    from Apps import ImageWriter
except ModuleNotFoundError:
    import PlexAuth
    import ImageWriter

plex = PlexServer(PlexAuth.getBaseUrl(), PlexAuth.getToken())

# account = MyPlexAccount(PlexAuth.getUsername(), PlexAuth.getPassword())
# plex = account.resource(PlexAuth.getServerName()).connect()

baseurl = plex._baseurl

movies = plex.library.section('Movies')

def getUnwatchedMovies():
    global movies
    arr = []
    for video in movies.search(unwatched=True):
        arr.append(video.title)
    return arr

def getMovieByDirector(director):
    global movies
    arr = []
    for movie in movies.search(director):
        arr.append(movie.title)
    return arr

def getMovieByTitle(title):
    global movies
    arr = []
    for movie in movies.search(title):
        arr.append(movie.title)
    return arr

def getMoviePosterByTitle(title):
    global movies, baseurl
    for movie in movies.search(title):
        print(baseurl + movie.art)
        ImageWriter.writeImage(movie.title, baseurl + movie.art)

#getMoviePosterByTitle("tenet")
#print(plexapi.video.Movie == plexapi.video.Movie)
#print(getMovieByTitle("tenet"))

for movie in getMovieByTitle("tenet"):
    print(plex.transcodeImage(movie, 400,400))

print(plex.clients())

for client in plex.sessions():
    print(client.title)

