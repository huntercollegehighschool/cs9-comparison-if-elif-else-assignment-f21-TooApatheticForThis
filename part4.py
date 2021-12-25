'''
______
PART 4
______
Write a program that prompts the user to enter two integer inputs. The program prints a string stating if the inputs are both positive, negative, if one of the inputs is zero, or if they have opposite signs. (Hint: this code can be written using only four code blocks, but you may find ways to do this using more.)

Four examples of what should appear on the console when this program runs (note: the test driver is case sensitive):

Enter a number:  3
Enter another number:  7
positive

Enter a number:  -5
Enter another number:  -2
negative

Enter a number:  7
Enter another number:  0
zero

Enter a number:  2
Enter another number:  -2
opposite
'''

#start writing your code below

num1 = int(input("Enter number one: "))
num2 = int(input("Enter number two: "))

if num1 > 0 and num2 > 0:
  print("Both numbers are positive.")
elif num2 < 0 and num1 < 0:
  print("Both numbers are negative.")
elif num1 == 0 or num2 == 0:
  print("One of these numbers is zero.")
elif num1 > 0 and num2 < 0 or num1 < 0 and num2 > 0:
  print("These numbers are opposites.")