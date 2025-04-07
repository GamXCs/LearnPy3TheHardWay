name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Lets' talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

convert_in_to_cm = height * 2.54
convert_lbs_kgs = weight * 2.2

# this line is tricky, tr to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I got {total}.")

print(f"My height in centimeters is {convert_in_to_cm} cm's and my weight in kilograms is {convert_lbs_kgs:.2f}")

