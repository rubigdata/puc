import settings
import dataset

db = dataset.connect(settings.CONNECTION_STRING)
res = db.query('SELECT count(*) c FROM verkiezingen')
for row in res:
    print(row['c'])
