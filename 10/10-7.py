while True:
    
    num1 = input("\nEnter first number: ")
    num2 = input("Enter second number: ")

    try:
        sum = int(num1) + int(num2)
        print('Sum: ' + str(sum))
        flag = input("\nEnter q to quit: ")
        if flag == 'q':
            break

    except ValueError:
        print("Sorry. Something went wrong.")
        flag = input("\nEnter q to quit: ")
        if flag == 'q':
            break