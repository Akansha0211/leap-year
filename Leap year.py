def leap_year(yr):
    if yr%4==0 and yr%100!=0:
        return True
    elif yr%4==0 and yr%100==0 and yr%400==0:
        return True
    else:
        return False
n=int(input("Enter a year"))
print(leap_year(n))

