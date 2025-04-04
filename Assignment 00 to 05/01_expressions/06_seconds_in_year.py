# Use Python to calculate the number of seconds in a year, and tell the user 
# what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):
# There are 5 seconds in a year!
# You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 
# 60 minutes in an hour, and 60 seconds per minute.


year : int = 365        #Days per year is 365
hour : int = 24         #Hour per day is 24
minutes : int = 60      #Minutes per hour is 60
second : int = 60       #Second per minutes is 60

# Calculate Total Seconds in a year
def main():

  total_second = year * hour * minutes * second
  print(f"There are {total_second} seconds in a year")

if __name__ == "__main__":
  main()