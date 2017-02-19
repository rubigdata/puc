import settings
import dataset

db = dataset.connect(settings.CONNECTION_STRING)
res = db.query('SELECT user_name u, COUNT(*) c FROM verkiezingen GROUP BY user_name HAVING c > 1 ORDER BY c DESC')
for row in res:
    print(row['u'], row['c'])
