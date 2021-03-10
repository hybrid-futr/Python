#Converting kilometers to miles
print("How many kilometeres do you want to convert to miles?")

kms = input()
miles = float(kms)/1.60934
miles = round(miles,2)

print(f"Ok, that's {miles} miles")