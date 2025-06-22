from datetime import datetime
from datetime import timedelta
today=datetime.now()
yesterday=today-timedelta(days=1)
print(yesterday)
hours=today-timedelta(hours=1)
print(hours)