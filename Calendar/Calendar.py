class Calendar:
    def __init__(self) -> None:
        self.week_day_names = ('SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT')
        self.months_name_and_code = ((0, "JAN"),(3, "FEB"),(3, "MAR"),(6, "APR"),(1, "MAY"),(4, "JUN"),(6, "JULY"),(2, "AUG"),(5, "SEP"),(0, "OCT"),(3, "NOV"),(5, "DEC"))

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

    def get_week_day_name_from_date(self, date:int, month:int, year:int) -> str:
        week_day_names_index = (date + self.months_name_and_code[month - 1][0] + 
                                self.get_year_special_code(year) + 
                                (year % 100) + (year % 100) // 4) % 7
        # week_day_names_index = (date + self.months_name_and_code[month - 1][0] + self.get_year_special_code(year) + (year % 100) + (year % 100) // 4) % 7

        if (year % 4) == 0 and ((year % 100) != 0 or (year % 400) == 0) and (month <= 2 and month > 0):
            week_day_names_index -= 1
        
        week_day_names_index = week_day_names_index % 7
        
        return self.week_day_names[week_day_names_index]
        

        # return "Sggs"

#__main__
cal = Calendar()
print(cal.get_week_day_name_from_date(1,1,2024))