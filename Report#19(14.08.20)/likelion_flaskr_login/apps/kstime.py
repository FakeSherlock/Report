# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

def kstime(hours):
    tm = datetime.now()
    fulldate = datetime(tm.year, tm.month, tm.day, tm.hour, tm.minute, tm.second)
    fulldate = fulldate + timedelta(hours=hours)
    return fulldate

# kstime 이라는 class를 저장한 module 파일입니다.
# kstime class는 fulldate라는 변수에 현재 시간을 flask 내장함수 datetime을 통해 저장합니다.
# 그리고 외부 변수, hours를 받아서 timedelta 함수로 fulldate의 값을 조정합니다.

# <timedelta 함수(클래스)>
# timedelta는 시간이나 날짜를 연산하기 위한 python 함수입니다.
# 다음과 같은 예제가 있습니다.

# from datetime import datetime
# from datetime import timedelta
# dt =  datetime.now()
# print dt


# dt = datetime.now()+timedelta(days=-3)
# dt_1 = dt+timedelta(days=-3)

# print str(dt) +"\n"+str(dt_1)

# subtract = dt-dt_1
# print subtract



