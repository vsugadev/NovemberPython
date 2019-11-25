x = eval(input("Enter the Score: "))

if x > 90:
    print ("Grade is A. You Scored - " , x)
elif (int (x) > 80):
    print ("Grade is B. You Scored - " , x)
elif (x > 70):
    print("Grade is C. You Scored - ", x)
elif (x > 60):
    print("Grade is D. You Scored - ", x)
else:
    print("Grade is F. You Scored - ", x)

day = eval(input("Enter the Day: "))

if day == 1:
    print ("Today is Monday..." , day)
elif day == 2:
    print("Today is Tuesday...", day)
elif day == 3:
    print("Today is Wednesday...", day)
elif day == 4:
   print("Today is Thrusday...", day)
elif day == 5:
    print("Today is Friday...", day)
elif day == 6:
    print("Today is Saturday...", day)
elif day == 7:
   print("Today is Sunday...", day)
else:
    print("Invalid Entry ", day)

# Python program to Find day of
# the week for a given date
import datetime
import calendar


def findDay(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[born])


# Driver program
#date = '03 02 2019'
date = input("Enter the Date : [DD MM YYYY] : ")
print("Day is: " + findDay(date))


