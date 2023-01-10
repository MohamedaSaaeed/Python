#creating leap year function 
def leap_year(year):
    #there are 3 condition to identify leap year        
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
year = int(input("Enter a year: "))
print(leap_year(year))
