print("Enter seconds:")

timefromuser = int(input())

days1 = int(timefromuser / 86400)
days = int(days1)

hours1 = int(timefromuser - days * 86400)
hours = int(hours1 / 3600)

minutes1 = int(hours1 - hours * 3600)
minutes = int(minutes1 / 60)

seconds1 = int(minutes1 - minutes * 60)
seconds = int(seconds1 / 60)

print("Days:", days, "Hours:", hours, "Minutes", minutes, "Second:", seconds1)