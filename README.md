# Audio TheraPy
Spotify playlist generator using sentiment analysis on personal journal/diary entry data.
Requires Spotify Premium to use; I've hidden my user credentials in a .gitignore but if you'd like to run this project, download the below dependencies and visit https://developer.spotify.com/ to generate your personal tokens.

### Tech/Libraries Used
* Spotipy
  * Access Spotify API for user history and playlist generation.
* NLTK
  * Valence Aware Dictionary and sEntiment Reasoner (VADER) for sentiment analysis of user text entry.
* Pandas
  * Storage of scraped song data and Boolean indexing for quick recall.
 
### Contents
1. sentiment.py
  1. Evaluates the sentiment of a given body of text.
2. spotify_scraper.py
  1. Scrapes Spotify API for song information and contains details in a pd.DataFrame.
3. audio_thera.py
  1. main() function that runs scripts developed in the other .py files.
4. secrets.py (.gitignore)
  1. Contains user credentials including username, scope, client_id, client_secret, and redirect_uri for the app.

### Example
Add screen recording of script in action (include arg from command line, Spotify API auth, and resulting playlist)

### Next Steps
Discuss Flask, SQL database, and improved categorization of songs and sentiment analysis.

### License
Add MIT license data here.
