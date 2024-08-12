#Develop a program that converts a given number of minutes into hours and minutes. For example, 125 minutes should be converted to 2 hours and 5 minutes.

minutes=int(input("Enter time in minutes"))
hours=minutes//60
remaining_minutes=minutes%60
print('Converting minutes to hours and minutes')
print(f'{hours} hours {minutes} minutes')
