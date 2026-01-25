# python program to convert celcius to fahrenheit using map().
celcius = [10,20,15,30,50]
def farh(c):
    return (c * 9/5) + 32
farehnheit = list(map(farh,celcius))
print(farehnheit)
  