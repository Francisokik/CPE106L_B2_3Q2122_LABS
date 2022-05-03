import random

def main():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = 15
  rnd = random.randint(0, last)

  print(quotes[rnd])
  print(quotes[6])

if __name__== "__main__":
  main()
