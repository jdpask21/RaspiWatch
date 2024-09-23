import datetime

WEEK_DAY = ["(MON)", "(TUE)", "(WED)", "(THU)", "(FRI)", "(SAT)", "(SUN)"]

def get_now_time():
    dt = datetime.datetime.now()
    str_month_day = "{}/{}".format(dt.month, dt.day)
    str_weekday = WEEK_DAY[dt.weekday()]
    return dt.hour, dt.minute, str_month_day, str_weekday, dt

if __name__=="__main__":
    print(get_now_time())