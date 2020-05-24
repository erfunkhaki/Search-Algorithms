def linear_search():
    character = ""
    # for error handling, backslash and quotations escaped
    illegal = "1234567890!@#$%^&*()-_=+[]{}\\|;:'\"/?.>,<`~"
    message = input("What are your plans for summer: ")
    while(len(character) != 1):
        character = input("what character do you want to search for? ")
    count = 0

    for x in message:
        if character[:] in illegal:
            print("you must enter a character")
            return
        if x == character:
            count += 1
    
    print(character +  " appears: " + str(count) + " times")
    return count


numbers = [2,5,7,8,11,13,17,19,23,29]
linear_search()
