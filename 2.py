print ("Program Odd or Even")
num=int(input('Write number \n'))
check=int(input('write number to divide ? \n'))
if (num % check) == 0:
    print("dzielenie bez reszty")
else:
    print("Reszta z dzielenia", (num%check)) 

