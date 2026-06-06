#File: easter_date.py
#Description: A program to calculate for easter date
#Assignment 3

    #Name: Enoch Shamo Abbey
    #Index No: 2425404607
    #Email : 2425404607@live.gctu.edu.gh
    #Grader: Augustus Buckman
    #
    # On my honor,Enoch Shamo Abbey, this programming assignment is my own work
    #and I have not provided this code to any other student.

    # THE USER HAS TO INPUT THE YEAR
year =int(input("Enter a year: "))
    # THE LUNAR YEAR CYCLE POSITION
lunar_year_cycle_position= year % 19
    # WEEKDAY SLIDE PART 1
weekday_slide_part_1 = year % 4
    #WEEKDAY SLIDE PART 2
weekday_slide_part_2 = year % 7
    #LEAP YEAR
leap_year_100= year // 100
leap_year_400 = leap_year_100 // 4
    # LUNAR OBIT CORRECTION
lunar_obit_correction = (13 + 8 * leap_year_100 ) // 25
    #CENTURY START
century_start = (15 - lunar_obit_correction + leap_year_100 - leap_year_400) % 30
    # SUNDAY OFFSET
sunday_offset = (4 + leap_year_100 - leap_year_400) % 7
    # DAYS ADDED
days_added = (19 * lunar_year_cycle_position + century_start ) % 30
    #DAY OF THE WEEK OFFSET
day_of_the_week_offset = (2 * weekday_slide_part_1 + 4 * weekday_slide_part_2 + 6 * days_added + sunday_offset) % 7
     # TOTAL DAYS ADDED
total_days_added = 22 + days_added + day_of_the_week_offset
day_of_easter = total_days_added % 31
month_of_easter = 3 + (total_days_added // 31)

print("In", year ,"Easter Sunday is on ", str(month_of_easter) + "/" + str(day_of_easter) + "/" + str(year)  + ".")


