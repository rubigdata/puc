import settings
import tweepy
import dataset
from textblob import TextBlob

db = dataset.connect(settings.CONNECTION_STRING)

result = db[settings.TABLE_NAME].all()
dataset.freeze(result, format='csv', prefix=settings.DATA_DIR, filename=settings.CSV_NAME)
