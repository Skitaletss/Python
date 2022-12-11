month = input("Enter the month:").title()
if month in("December", "January", "February", "12", "01", "02"):
    print("Winter")
elif month in("March", "April", "May", "03", "04", "05"):
    print("Spring")
elif month in("June", "July", "August", "06", "07", "08"):
    print("Summer")
elif month in("September", "October", "November", "09", "10", "11"):
    print("Autumn")
else:
    print("Error")