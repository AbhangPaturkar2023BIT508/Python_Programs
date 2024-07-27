class Calendar:
    def __init__(self) -> None:
        self.week_day_names = ('SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT')
        self.months_name_code_daycount = ((0, "JAN", 31),(3, "FEB", 28),(3, "MAR", 31),(6, "APR", 30),(1, "MAY", 31),(4, "JUN", 30),(6, "JULY", 31),(2, "AUG", 31),(5, "SEP", 30),(0, "OCT", 31),(3, "NOV", 30),(5, "DEC", 31))
    # end of __init__

    # Return True if argument year is leap, otherwise return False
    def is_leap_year(self, year : int) -> bool:
        if (year % 4) == 0 and ((year % 100) != 0 or (year % 400) == 0):
            return True
        else:
            return False
    # end of is_leap_year

    # Return special code of year which we will pass as argument
    def get_year_special_code(self, year : int) -> int:
        mod_year = year % 400
        if mod_year < 100 and mod_year >= 0:
            return 6
        if mod_year < 200 and mod_year >= 100:
            return 4
        if mod_year < 300 and mod_year >= 200:
            return 2
        if mod_year < 400 and mod_year >= 300:
            return 0 
    # end of get_year_special_code 

    # Return week-day name of given date
    def get_week_day_name_from_date(self, date:int, month:int, year:int) -> str:
        week_day_names_index = (date + self.months_name_code_daycount[month - 1][0] + 
                                self.get_year_special_code(year) + 
                                (year % 100) + (year % 100) // 4) % 7


        if self.is_leap_year(year) and (month <= 2 and month > 0):
            week_day_names_index -= 1
        
        week_day_names_index = week_day_names_index % 7
        
        return self.week_day_names[week_day_names_index]
    # end of get_week_day_name_from_date

    def print_week_day_horizontally(self) : 
        for week_day in self.week_day_names:
            print(week_day, end="|")
        print()
    # end of print_week_day_horizontally

    def print_space(self, count):
        for i in range(count):
            print("   ", end='|')

    def print_month_days(self, start_week_day):
        index_start_week_day = self.week_day_names.index(start_week_day)
        self.print_space(index_start_week_day)
        for i in range(1,self.months_name_code_daycount[0][2]+1):
            if i >= 10:
                print('',i,end='|')
            else:
                print(' ',i,end='|')
            if ((index_start_week_day + i ) % 7 == 0):
                print()
        self.print_space(35-(index_start_week_day+self.months_name_code_daycount[0][2]))

    def print_month(self, year:int):
        week_day_name_of_first_jan = self.get_week_day_name_from_date(1,1,year)
        self.print_week_day_horizontally()
        self.print_month_days(week_day_name_of_first_jan)
        # print(week_day_name_of_first_jan)
    # end of print_month

# end of Calendar
        

#__main__
cal = Calendar()
# print(cal.get_week_day_name_from_date(1,3,2024))
cal.print_month(2024)

#end of __main__