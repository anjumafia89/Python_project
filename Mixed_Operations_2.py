#Body Fat Percentage Calculator
# Create a program that calculates the body fat percentage for a given weight and body fat weight. Then, determine if the person is in a healthy range.
weight = float(input("Enter weight kg : "))
body_fat_weight = float(input("Enter body fat weight kg: "))
gender=input('Enter your gender (male/female): ')
body_fat_percentage = (body_fat_weight/weight) * 100

if gender=="male":
    if 6 <= body_fat_percentage <= 24:
        health_status = "Healthy"
    elif body_fat_percentage < 6:
        health_status = "Underfat"
    else:
        health_status = "Overfat"
elif gender=="female":
    if 16 <= body_fat_percentage <= 30:
        health_status = "Healthy"
    elif body_fat_percentage < 16:
        health_status = "Underfat"
    else:
        health_status = "Overfat"
else:
    health_status = "Invalid"


print(f"Body Fat Percentage: {body_fat_percentage:.2f}%")
print(f"Health Status: {health_status}")