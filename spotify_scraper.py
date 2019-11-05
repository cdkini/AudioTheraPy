import bisect
import datetime as dt
import pandas as pd
import random
import spotipy
import spotipy.util as util

from secrets import secret_dict
from sentiment import classifications

token = util.prompt_for_user_token( # Stored in secret file for security purposes.
        username=secret_dict['username'], # 6 digit Spotify ID
        scope=secret_dict['scope'], # Use 'user-top-read playlist-modify-private'
        client_id=secret_dict['client_id'], # Generated when you register app to Spotify Developer
        client_secret=secret_dict['client_secret'], # Generated when you register app to Spotify Developer
        redirect_uri=secret_dict['redirect_uri'] # Whatever you set up; I used http://localhost:8888/callback/
)

sp = spotipy.Spotify(auth=token)

def top_artists(num=5):
    '''
    Determines the top artists a user has listened to recently.

    Parameters:
    num (int): Number of artists desired (max=5).

    Returns:
    artist_list (list): List of top artist's Spotify URI's.
    '''
    artist_data = sp.current_user_top_artists(limit=num, time_range='medium_term')

    return [artist_data['items'][i]['id'] for i in range(num)]

def recommendations(artist_list, num=100):
    '''
    Generates song recommendations based off of user's top artists.

    Parameters:
    artist_list (list): List of artist Spotify URI's used as a basis for recommendations.
    num (int): Number of desired recommended songs (max=100)

    Returns:
    song_df (pd.Dataframe): Includes title, artist, and related Spotify URI.
    '''
    recs_data = sp.recommendations(seed_artists=artist_list, limit=num)
    song_df = pd.DataFrame(columns=['Song', 'Artist', 'URI'])

    for i in range(num):
        song = recs_data['tracks'][i]['name']
        artist = recs_data['tracks'][i]['artists'][0]['name']
        uri = recs_data['tracks'][i]['id']

        song_df.loc[i] = [song, artist, uri]
        
    return song_df

def song_sentiment(song_df, classifications):
    '''
    Adds a sentiment score and related classification for each song in a dataframe.

    Parameters:
    song_df (pd.DataFrame): List of songs; must include related Spotify URI's.

    Returns:
    song_df (pd.DataFrame): Updated df with 'Sentiment Score' and 'Classification' columns. 
    '''
    for i, song in song_df.iterrows():
        valence = sp.audio_features(song['URI'])[0]['valence'] # Spotify API's measure of sentiment
        song_df.loc[i, 'Sentiment Score'] = valence

        thresholds = [0, 0.125, 0.25, 0.375, 0.625, 0.75, 0.875]
        classifications = classifications

        pos = bisect.bisect_left(thresholds, valence) 
        song_df.loc[i, 'Classification'] = classifications[pos-1]

    return song_df

def generate_playlist(song_df, classifications, mood):
    '''
    Creates a playlist for the user based on current sentiment.
    The more negative the sentiment, the more positive the recommended songs.
    If sentiment is already positive or neutral, that will be the basis for recommendations.

    Parameters:
    song_df (pd.DataFrame): List of songs, must include URI's, sentiment scores, and classifications.
    classifications (list): List of categories for sentiment classification.
    mood (tuple): Current user classification and sentiment score.

    Returns:
    Playlist based on user sentiment in user's personal Spotify library.
    '''
    today = f'{dt.datetime.now(): %B %d, %Y}'
    playlist = sp.user_playlist_create(
            user=secret_dict['username'],
            name=f'Audio TheraPy: {today}',
            public=False
    )

    if mood in classifications[:3]: # If sentiment is negative, abs(sentiment) is recommended.
        mood = classifications[:3:-1][classifications[:3].index(mood)]
     
    song_df = song_df[song_df['Classification']==mood]

    sp.user_playlist_add_tracks(
            user=secret_dict['username'],
            playlist_id = playlist['id'],
            tracks = song_df['URI']
    )
