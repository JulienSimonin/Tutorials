# Import the datetime
import datetime

# Asking the user the task and the deadline and make it a list
user_imput = input("Enter your task and your deadline separated by colon :\n")
user_list = user_imput.split(" : ")

# Assinging the data of the list to the variables
task = user_list[0]
deadline = user_list[1]

# Define the deadline as a date data type and the date of the day
deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
date_today = datetime.datetime.today()

# Calculate how many time is left until the deadline in days and hours 
time_remaining = deadline_date - date_today
time_remaining_hour = time_remaining.total_seconds() / 60 / 60

# Response to the user
def countdown():
    if deadline_date <= date_today :
        return (f"The date of your {task} is overpassed !")
    # If the deadline date is less than today's date then that means that the deadline is overpassed
    elif int(time_remaining_hour) >= 24 :
        return (f"The time remaining for the {task} is {time_remaining.days} days")
    # If the time remaining for the deadline is over 24 hours then the time remaining is displayed in days
    else :
        return (f"The time remaining for the {task} is {round(time_remaining_hour, 2)} hours")
    # If the time remaning is under 24 hours then it's displayed in hours with 2 decimals

# Call out result and print it
result = countdown()
print(result)

