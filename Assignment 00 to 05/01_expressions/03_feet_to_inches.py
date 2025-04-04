# Converts feet to inches. Feet is an American unit of measurement. 
# There are 12 inches per foot. Foot is the singular, and feet is the plural.

foot : int = 12  # 1 foot = 12 inches

def main():
  user : float = float(input("Enter your feet"))
  total_inches = user * foot
  print(f"{user} feet = {total_inches} inches")

if __name__ == "__main__":
  main()