#Exercise
user_input = input("Enter a number: ")

#Convert input to an integer 
try:
  number = int(user_input)
  #Check if number is odd or even
  if number % 2 == 0:
    print(f"{number} is an even number.")
        
  else:
    print(f"{number} is an odd number")
  exept ValueError:
    print("You did not enter a number.")
