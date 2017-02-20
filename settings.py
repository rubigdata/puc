#TRACK_TERMS = ["rutte", "wilders", "klaver", "pechthold"]
TRACK_TERMS = ["rutte", "klaver", "pechthold"]
CONNECTION_STRING = ""
CSV_NAME = "tweets.csv"
TABLE_NAME = "verkiezingen"

try:
    from private import *
except Exception:
    pass
