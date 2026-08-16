def read_int(prompt, min, max):
    #
    # Write your code here.
    #
    read_input = ""
    while(True):
        try:
            read_input = int(input(prompt))
            if read_input < min or read_input > max:
                print("Error: the value is not within permitted range (min..max)")
            else:
                return read_input

        except ValueError:
            print("Error: wrong input")


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
