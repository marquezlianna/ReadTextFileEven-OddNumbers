def process():
    # open numbers.txt(read), even.txt(append), odd.txt(append)
    with open("numbers.txt") as input_file, open("even.txt", "a") as output_even, open("odd.txt", "a") as output_odd:
        # read numbers.txt line by line
        for line in input_file:
            input_num = int(line)
        # print all even numbers in the list
            if input_num % 2 == 0:
            # write to even.txt
                output_even.write(str(input_num) + "\n")        

