#def isValue(checkStr):
#   if not checkStr.isdigit() :
#        exit("Not Digit");
         
print("Enter Day of Year : ");
day = int(input());
#isValue(str(day))
if day > 31 or day <= 0:
    exit("Day Must be Valid");
    
    
print("Enter Month of Year : ");
month = int(input());
#isValue(str(month))

if month > 12 or month <= 0:
    exit("Month must be Valid");

print("Enter Year : ");
year = int(input());
#isValue(str(year));

if year < 0 :
    exit("Write Valid Year");

day_of_week = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thusday","Friday"];

answer_of_date = (day+((13*(month+1))/5)+year+(year/4)-(year/100)+(year/400))%7

#print(answer_of_date);
print("Thier is : ",day_of_week[int(answer_of_date)]);