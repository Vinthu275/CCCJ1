#Function to check and ensure proper digit entry
def check_digit(msg,min):
  while True:
    num=input(msg)
    if num.isdigit():
      intNum=float(num)
      if intNum < min:
        print("sorry, not in range")
      else:
        break
    else:
      print(f"Digits bigger than {min} only")
  return intNum

#get info from the user
print("A regular box of cupcakes holds 8 cupcakes, while a small box holds 3 cupcakes. There are 28 students in a class and a total of at least 28 cupcakes. Your job is to determine how many cupcakes will be left over if each student gets one cupcake.\n")

#gets input from user for regular and small boxes
def get_left_overs():
  #gets regular boxes input and errors checks
  regular_boxes = check_digit("How many regular boxes do you wish to buy? ", 0)
  #gets small boxes input and errors checks
  small_boxes = check_digit("How many small boxes do you wish to buy? ", 0)

  #calculate number of cupcakes bought
  number_of_cupcakes_bought=(8*regular_boxes)+(3*small_boxes)

  #calculate the leftovers
  return number_of_cupcakes_bought - 28

#get input from user
left_overs = get_left_overs()

#keep asking for input if leftovers is less than 0
while left_overs < 0:
  print("Need more boxes")
  left_overs = get_left_overs()

#spit out left overs to the user
print("You have " + str(left_overs) + " cupcakes left over")
