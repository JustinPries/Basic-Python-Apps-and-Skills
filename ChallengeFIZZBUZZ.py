name = input("Please enter your name: ")
number = int(input("Please enter a number: "))


if number % 5 == 0 and number % 3 == 0:
    print("Is a FizzBuzz number")

elif number % 5 == 0:
    print("Is a Buzz number.")

elif number % 3 == 0:
    print("Is a Fizz number.")

elif number % 5 != 0 or number % 3 !=0:
    print("Is neither a fizzy or buzzy number.")