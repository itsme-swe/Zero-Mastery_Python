# Argument index formatting
a = 22
b = 7
c = a / b

print("Division of {0} and {1} is {2:2.3}".format(a,b,c))   # Outpt: Division of 22 and 7 is 3.14
# Here {} are place holders and the values inside the placeholder is index values and inside the .format() function are the variable names

name = "Harsh"
car = "Virtus"
engine = "1500cc"

print(f"I am {name:15} and I drive {car:^10} volkswagen car and it is {engine:>} engine car")
# Output: I am Harsh           and I drive   Virtus   volkswagen car and it is 1500cc engine car