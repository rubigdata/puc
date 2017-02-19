import settings
import dataset
#from textblob import TextBlob

db = dataset.connect(settings.CONNECTION_STRING)
res = db.query('SELECT user_name u, retweet_count rc, text t FROM verkiezingen')
for row in res:
    print(row['u'], row['rc'], row['t'])
