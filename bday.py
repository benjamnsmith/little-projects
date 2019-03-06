def chineseYear(year):
    zodiacs = ["Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig", "Rat", "Ox", "Tiger", "Rabbit"]
    year = int(year)
    backwards = False
    dist = year - 2000
    if dist < 0:
        backwards = True
    dist = abs(dist) % 12
    if backwards:
        dist = -dist
    yourZodiac = zodiacs[dist]
    return yourZodiac

def horoscopeSun(month,day):
    month = int(month)
    day = int(day)
    if month == 1 and day <= 20:
        yourSign = "Capricorn"
    elif month == 1 and day >= 21:
        yourSign = "Aquarius"
    elif month == 2 and day <= 19:
        yourSign = "Aquarius"
    elif month == 2 and day >= 20:
        yourSign = "Pisces"
    elif month == 3 and day <= 20:
        yourSign = "Pisces"
    elif month == 3 and day >= 21:
        yourSign = "Aries"
    elif month == 4 and day <= 20:
        yourSign = "Aries"
    elif month == 4 and day >= 21:
        yourSign = "Taurus"
    elif month == 5 and day <= 21:
        yourSign = "Taurus"
    elif month == 5 and day >= 22:
        yourSign = "Gemini"
    elif month == 6 and day <= 21:
        yourSign = "Gemini"
    elif month == 6 and day >= 22:
        yourSign = "Cancer"
    elif month == 7 and day <= 22:
        yourSign = "Cancer"
    elif month == 7 and day >= 23:
        yourSign = "Leo"
    elif month == 8 and day <=22:
        yourSign = "Leo"
    elif month == 8 and day >= 23:
        yourSign = "Virgo"
    elif month == 9 and day <= 22:
        yourSign = "Virgo"
    elif month == 9 and day >= 23:
        yourSign = "Libra"
    elif month == 10 and day <= 22:
        yourSign = "Libra"
    elif month == 10 and day >= 23:
        yourSign = "Scorpio"
    elif month == 11 and day <= 21:
        yourSign = "Scorpio"
    elif month == 11 and day >= 22:
        yourSign = "Sagittarius"
    elif month == 12 and day <= 21:
        yourSign = "Sagittarius"
    elif month == 12 and day >= 22:
        yourSign = "Capricorn"
    else:
        yourSign = "Stupid"

    return yourSign

def dayOfWeek(year, month, day):
    year = int(year)
    month = int(month)
    day = int(day)
    leapYear = False
    if year % 4 == 0:
        leapYear = True
        if year % 100 == 0:
            leapYear = False
            if year % 400 == 0:
                leapYear = True
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    cenDigs = year // 100
    yDigs = year % 100
    value = yDigs + (yDigs // 4)
    if cenDigs == 18:
        value += 2
    elif cenDigs == 20:
        value += 5
    elif cenDigs == 19:
        value -= 1
    if not leapYear:
        value += 1
    firstDayNum = (value + 1) % 7
    totalDays = 0
    for i in range(1,month):
        if i == 9 or i == 4 or i == 6 or i == 11:
            totalDays += 30
        elif i == 2 and leapYear:
            totalDays += 29
        elif i == 2 and not leapYear:
            totalDays += 28
        else:
            totalDays += 31
    totalDays += day - 1
    yourDay = days[(firstDayNum + totalDays) %7]
    return yourDay
