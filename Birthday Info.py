import bday

def userMode():
    print("\n"+"Interested in your birthday? Get ready to learn about it!")
    print("Simply enter your date of birth below.")
    dob = input("Date of Birth (mm/dd/yyyy): ")
    validInput = False
    while not validInput:
        try:
            m = dob[0:2]
            m = m.lstrip("0")
            d = dob[3:5]
            d = d.lstrip("0")
            y = dob[6:]
            cz = bday.chineseYear(y)
            hs = bday.horoscopeSun(m,d)
            dw = bday.dayOfWeek(y,m,d)
            validInput = True
        except ValueError:
            print("Date of birth not recognized. Please try again")
            dob = input("Date of Birth (mm/dd/yyyy): ")
    print("\n"+"You were born on a " + dw + ".")
    print("According to the Chinese zodiac, you were born in the Year of the " + cz + ".")
    print("Accoring to astrology, you are a " + hs + ".")

userMode()
