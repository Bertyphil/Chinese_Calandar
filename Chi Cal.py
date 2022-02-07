from lunardate import LunarDate

value= (input("Enter your birthday (DD MM YYYY) :"))
value= value.split(" ")
a = LunarDate.fromSolarDate(int(value[2]),int(value[1]),int(value[0]))

animal = ["Rat","Ox","Tiger","Rabbit","Dragon","Snake","Horse","Sheep","Monkey","Rooster","Dog","Pig"]

b = a.year
b = b-1900
b = b%12
if (a.month <10):
    a.month = str(a.month)
    a.month = "0"+ a.month
print("Your Lunar Birthday is (DD MM YYYY):",a.day,a.month,a.year)
print("Your Chinese animal is:",animal[b] )