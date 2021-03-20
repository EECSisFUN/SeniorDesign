from plexapi.myplex import MyPlexAccount
# from Apps import PlexAuth # running with main
import PlexAuth # running just this file
import ImageWriter


account = MyPlexAccount(PlexAuth.getUsername(), PlexAuth.getPassword())
plex = account.resource(PlexAuth.getServerName()).connect()
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
    for movie in movies.search(None, director=director):
        arr.append(movie.title)
    return arr

def getMovieByTitle(title):
    global movies
    arr = []
    for movie in movies.search(title):
        arr.append(movie.title)
    return arr

def getMoviePosterByTitle(title):
    global movies
    for movie in movies.search(title):
        print(baseurl + movie.art)
        ImageWriter.writeImage(movie.title, baseurl + movie.art)

#getMoviePosterByTitle("tenet")

