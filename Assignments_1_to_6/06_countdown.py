import time

def countdown(t):
  while t:
    mints, secs = divmod(t,60)
    timer = '{:02d}:{:02d}'.format(mints,secs)
    print(timer, end='\r')
    time.sleep(1)
    t -= 1

  print("Time up!")

def main():
  user_input:int= int(input("Enter the minute in second.(ex:1mint = 60sec) "))
  countdown(user_input)

if __name__ == "__main__":
  main()