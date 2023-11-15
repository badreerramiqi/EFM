def is_leap_year(a):
    # Check if the year 'a' is divisible evenly by 400
    if a % 400 == 0  or (a % 4 == 0 and a % 100 != 0  ) :
        # If divisible by 400, it is a leap year
        return True
    else:
        # If not divisible by 400, it is not a leap year
        return False

t=[]
def leap_years_between(siecle):
    # Iterate over a 100-year range starting from the specified 'start_year'
    for i in range(siecle*100, siecle*100+ 100):
        # Check if the current year 'i' is a leap year using the is_leap_year function
        if is_leap_year(i) == True:
            # If it's a leap year, print a message indicating so
            t.append(i)
    return t
            
siecle=int(input("type the siecle"))

# Call the leap_years_between function with a starting year 
print("The leep years in ",siecle ,"is ",leap_years_between(siecle))