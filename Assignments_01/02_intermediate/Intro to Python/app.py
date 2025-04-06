def main():
  earth_weight :int = int(input("Please enter the weight of Earth "))
  planet : str = str(input("Please enter the planet name. (ex: Mars, Jupiter) ")).lower()

  if planet == "mercury":
    gravity = 0.376
  elif planet == "venus":
    gravity = 0.889
  elif planet == "mars":
    gravity = 0.378
  elif planet == "jupiter":
    gravity = 2.36
  elif planet == "saturn":
    gravity = 1.081
  elif planet == "uranus":
    gravity = 0.815
  elif planet == "neptune":
    gravity = 1.14
  else:
    print("Please Enter a Valid or Correct spelling of Planet")

  result = earth_weight * gravity
  result = round(result,2)
  print(f"The equivlant of {planet} is {result}")

if __name__ == "__main__":
  main()