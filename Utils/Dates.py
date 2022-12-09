import numpy as np
import datetime
import math

from enum import Enum

class DateFormatTypes(Enum):
    BLOOMBERG = 1
    US_SHORT = 2
    US_MEDIUM = 3
    US_LONG = 4
    US_LONGEST = 5
    UK_SHORT = 6
    UK_MEDIUM = 7
    UK_LONG = 8
    UK_LONGEST = 9
    DATETIME = 10
    

gDateFormatType = DateFormatTypes.US_LONG

def set_date_format(format_type):
    global gDateFormatType
    gDateFormatType = format_type

###################################*****************************############################################

short_day_names = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

long_day_names = [
    'MONDAY',
    'TUESDAY',
    'WEDNESDAY', 
    'THURSDAY',
    'FRIDAY', 
    'SATURDAY',
    'SUNDAY'
]

short_month_names = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

long_month_names = [
    'JANUARY',
    'FEBRUARY',
    'MARCH',
    'APRIL',
    'MAY',
    'JUNE',
    'JULY',
    'AUGUST',
    'SEPTEMBER',
    'OCTOBER',
    'NOVEMBER',
    'DECEMBER'
]

monthDaysNotLeapYear = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthDaysLeapYear = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


###################################*****************************############################################


def is_leap_year(y:int):
    leap_year = ((y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0))
    return(leap_year)


def parse_date(datestr, dateformat):
    dtobj = datetime.datetime.strptime(datestr,dateformat)
    return dtobj.day, dtobj.month, dtobj.year



###################################*****************************############################################

gDateCounterList = None
gStartYear = 1900
gEndYear = 2100


def calculate_list_raw():
    day_counter = 0
    max_days = 0
    
    global gDateCounterList
    global gStartYear
    global gEndYear
    
    gDateCounterList = []
    
    idx =-1
    
    for yyyy in range(1900, gEndYear+1):
        if yyyy == 1900:
            leap_year = True
        else:
            leap_year= is_leap_year(yyyy)
        
        for mm in range(12):
            
            if leap_year is True:
                max_days = monthDaysLeapYear[mm]
            else:
                max_days = monthDaysNotLeapYear[mm]
            
            for _ in range(0, max_days):
                idx += 1
                day_counter += 1
                if yyyy >= gStartYear:
                    gDateCounterList.append(day_counter)
            
            for _ in range(max_days, 31):
                idx += 1
                if yyyy >= gStartYear:
                    gDateCounterList.append(-999)


def calculate_list():

    day_counter = 0
    max_days = 0

    global gDateCounterList
    global gStartYear
    global gEndYear

    gDateCounterList = []

    idx = -1 

    for yy in range(1900, gEndYear+1):

        if yy == 1900:
            leap_year = True
        else:
            leap_year = is_leap_year(yy)

        for mm in range(1, 13):

            if leap_year is True:
                max_days = monthDaysLeapYear[mm-1]
            else:
                max_days = monthDaysNotLeapYear[mm-1]

            for _ in range(1, max_days+1):
                idx += 1
                day_counter += 1
                if yy >= gStartYear:
                    gDateCounterList.append(day_counter)

            for _ in range(max_days, 31):
                idx += 1
                if yy >= gStartYear:
                    gDateCounterList.append(-999)


def date_index(dd,mm,yyyy):
    idx = (yyyy-gStartYear)*12*31+(mm-1)*31+(dd-1)
    return(idx)


def date_from_index(idx):
    yyyy = int(gStartYear + idx/12/31)
    mm = 1 + int((idx - (yyyy - gStartYear)*12*31)/31)
    dd = 1 + idx - (yyyy - gStartYear)*12*31 - (mm-1)*31
    return(dd,mm,yyyy)

def weekday(daycount):
    weekday = (daycount+5)%7
    return(weekday)

