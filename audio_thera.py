import datetime as dt
from sentiment import classifications, sentiment_classifier
import spotify_scraper as ss
from secrets import secret_dict
import sys
import time

def main():
    sentiment_classifications = classifications
    sentiment = sentiment_classifier(sentiment_classifications)
    print('\nPlease wait a moment as we generate your playlist...')
    recs = ss.song_sentiment(ss.recommendations(ss.top_artists()), sentiment_classifications)
    ss.generate_playlist(recs, sentiment_classifications, sentiment[0])
    return f'Your playlist has been created! -> Audio TheraPy: {dt.datetime.now(): %B %d, %Y}'

if __name__ == '__main__':
    main()
    time.sleep(5)
    sys.exit()