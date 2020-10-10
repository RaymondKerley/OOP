count = 1
while count <= 30:
    if count % 15 == 0:

        print(str(count) + " FizzBuzz")

    elif (count) % 5 == 0:

        print(str(count) + " Buzz")

    elif count % 3 == 0:

        print(str(count) + " Fizz")

    else:

        print(count) 

    count += 1