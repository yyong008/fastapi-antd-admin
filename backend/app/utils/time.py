from datetime import datetime, timedelta

def get_today_time():
    today_midnight = datetime.combine(datetime.today(), datetime.min.time())
    tomorrow_midnight = today_midnight + timedelta(days=1)
    return today_midnight, tomorrow_midnight

print(get_today_time())
