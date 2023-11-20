#Exercise 3 Odd or Even
#Create a python program that determines if the number is Odd or even based on the user input

value = input("what Number? ")

if int(value) % 2 == 0: 
  print(value)
  print("is even")
else:
  print(value)
  print("is odd")
