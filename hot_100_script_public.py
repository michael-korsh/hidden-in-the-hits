import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
import numpy
import sqlite3

cid = 'CLIENT ID'
secret = 'SECRET ID'

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_ids_from_playlist(user, playlist_id):
      '''
      Given a playlist, retrieves the track id for every song in the playlist.
      '''
      
      ids = []
      playlist = sp.user_playlist(user, playlist_id)
      for item in playlist['tracks']['items']:
          track = item['track']
          ids.append(track['id'])
      return ids

def get_all_track_ids():
   ''' 
   Retrieves the track id from each song in each Spotify playlist for every Year-End Billboard Hot 100 from 2010-2019.
   Places all ids in a single flattened list.

   '''
   ids = []
   ids_2019 = get_ids_from_playlist('21ksdt3ca2433ykekswnkdrni', '5lO5SKSvwbLetiBt6k7wNX') # 2019 playlist
   ids_2018 = get_ids_from_playlist('swegawaffle','4wSmeoexS546V0zZ0tpMAz') #2018 playlist
   ids_2017 = get_ids_from_playlist('wickeddreamer96','2XPEN88QyrPQ9zGqS8uS2x') # 2017 playlist
   ids_2016 = get_ids_from_playlist('wickeddreamer96','3JbWD8OGutoTKUbR3RvR8u') # 2016 playlist
   ids_2015 = get_ids_from_playlist('wickeddreamer96','6LYxiUgw87zsDPqU0sdalZ') # 2015 playlist
   ids_2014 = get_ids_from_playlist('wickeddreamer96','2trgZsxRpWX7sq28yHC40u') # 2014 playlist
   ids_2013 = get_ids_from_playlist('wickeddreamer96','1KK0RvFmgsUkZ8zELRZgjS') # 2013 playlist
   ids_2012 = get_ids_from_playlist('stealthamo','6ERBbbhAninxZrDNNwFAYD') # 2012 playlist
   ids_2011 = get_ids_from_playlist('wickeddreamer96','2z3eLip2NlV9quzTEm37cW') # 2011 playlist
   ids_2010 = get_ids_from_playlist('wickeddreamer96','4aUY170nZ3mhkzMpTAXDv2') # 2010 playlist

   ids.append(ids_2019)
   ids.append(ids_2018)
   ids.append(ids_2017)
   ids.append(ids_2016)
   ids.append(ids_2015)
   ids.append(ids_2014)
   ids.append(ids_2013)
   ids.append(ids_2012)
   ids.append(ids_2011)
   ids.append(ids_2010)
   
   flattened_ids = []

   for sublist in ids:
       for val in sublist:
           flattened_ids.append(val)
   
   return flattened_ids
            
def all_years():
    '''
    Creates a labeling sequence corresponding to the playlist for each year.
    '''
    years = [2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010] 
    years = numpy.repeat(years, 100)
    return years

def get_all_positions():
    '''
    Creates a labeling sequence corresponding to the position on the Hot 100 for each track.
    '''
    positions = []
    for b in range(100):
        b = b+1
        positions.append(b)
    positions = 10 * positions
    return positions

def get_track_features(id):
      '''
      Retrieves the song same, artist and emotional valence measure from a track, given the track id.
      '''

      info = sp.track(id)
      audio = sp.audio_features(id)
      
    
      name = info['name']
      artist = info['album']['artists'][0]['name']
      valence = audio[0]['valence']
      key = audio[0]['key']
      mode = audio[0]['mode']
      danceability = audio[0]['danceability']
      tempo = audio[0]['tempo']

      track = [name, artist, valence, key, mode, danceability, tempo]

      return track

def get_all_track_features(all_ids):
    '''
    Compiles  all track information for all track ids.
    '''
    
    track_features = []

    for a in all_ids:
        track_features.append(get_track_features(a))
    
    return track_features


all_ids = get_all_track_ids()

years = all_years()
positions = get_all_positions()

track_features = get_all_track_features(all_ids)

df = pd.DataFrame(track_features, columns=['name','artist','valence','key','mode','danceability','tempo'])
df['year'] = years
df['position'] = positions

modes_dict = {'mode': [0,1], 'modename': ['minor', 'major']}
modes = pd.DataFrame.from_dict(modes_dict)

keys_dict = {'key': [0,1,2,3,4,5,6,7,8,9,10,11], 'keyname': ['C', 'C#','D','D#','E','F','F#','G','G#','A','Bb','B']}
keys = pd.DataFrame.from_dict(keys_dict)

df.to_csv('hot_100s.csv')
modes.to_csv('modes.csv')
keys.to_csv('keys.csv')
