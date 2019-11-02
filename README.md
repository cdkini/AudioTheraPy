# Audio TheraPy
- - - -
### About
Spotify playlist generator using sentiment analysis on personal journal/diary entry data.
Requires Spotify Premium to use; I've hidden my user credentials in but if you'd like to run this project, download the below dependencies and visit https://developer.spotify.com/ to generate your personal tokens. See the <b>"Example"</b> section below for a demonstration.
- - - -
### Tech/Libraries Used
* Spotipy
  * Access Spotify API for user history and playlist generation.
* NLTK
  * Valence Aware Dictionary and sEntiment Reasoner (VADER) for sentiment analysis of user text entry.
* Pandas
  * Storage of scraped song data and Boolean indexing for quick recall.
 - - - -
### Contents
* <b>sentiment.py</b>
  * Evaluates the sentiment of a given body of text.
* <b>spotify_scraper.py</b>
  * Scrapes Spotify API for song information and contains details in a pd.DataFrame.
* <b>audio_thera.py</b>
  * main() function that runs scripts developed in the other .py files.
* <b>secrets.py</b> (<i>.gitignore</i>)
  * Contains user credentials including username, scope, client_id, client_secret, and redirect_uri for the app.
- - - -
### Example
Add screen recording of script in action (include arg from command line, Spotify API auth, and resulting playlist)
- - - -
### Next Steps
- [ ] Host application on Flask or Django.
- [ ] Create SQLite database to store sentiment analysis results / recommended songs.
- [ ] Improve method of analyzing song sentiment through Spotify's metrics.
- - - -
### License
Add MIT license data here.
