"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
""" 

user_age = int(input("Please enter your age:"))
calc_heart = (220-user_age)
calc_heart_high = calc_heart * .85
calc_heart_low = calc_heart * .65


print(f'When you exercise to strengthen your heart, you should keep your heart rate between {calc_heart_high:.2f} and {calc_heart_low:.2f} beats per minute.')