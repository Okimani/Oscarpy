from datetime import datetime, timedelta #import the datetime and timedelta Libraries.
print('Hello world')
today = datetime.now()
five_days_ago = today - timedelta(days=5)
print(five_days_ago)
print(today)


