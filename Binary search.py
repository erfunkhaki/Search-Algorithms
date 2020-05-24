def binary_search(numbers,print_flag,number):
    # print flag is used to allow the user to enter
    # the search number only on the first time the
    # function is called

    if(print_flag == 0):
        print("Number will be searched for using the binary search method")
        number = int(input("please enter a number: "))
    found = 0
    
    if len(numbers) == 0:
        found = 1
        print ("not found")
    else:
        middle = len(numbers)//2
        left_list = numbers[:middle]
        right_list = numbers[middle+1:]
        if numbers[middle] == number:
            print(str(number) + " found")
            return number
            found = 1
        else:
            if numbers[middle] > number:
                binary_search(left_list,1,number)
            else:
                binary_search(right_list,1,number)

numbers = [2,5,7,8,11,13,17,19,23,29]
binary_search(numbers,0,0)
