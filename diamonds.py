number_of_rows = int(input("please enter the number of rows: "))

# print the upper half of our diamond
for i in range(number_of_rows):
   #printing spaces
   print(" " * (number_of_rows - i - 1), end="")
   # printing *
   print("*" * (i * 2 + 1))

#  print the lower half, we need the second last row to form the diamond shape(-2)
for i in range(number_of_rows - 2, -1, -1):
    print(" " * (number_of_rows - i - 1), end="")
    print("*" * (2 * i + 1))
    
    