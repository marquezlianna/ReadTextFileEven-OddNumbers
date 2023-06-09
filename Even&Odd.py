# Write a Python program that reads a text file named numbers.txt that contains 20 integers.
# The program will create two other text file; the first text file will be named even.txt that will contains all even numbers extracted from the numbers.txt
# The second text file will be named odd.txt that will contains all odd numbers extracted from the numbers.txt

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
        # print all odd numbers in the list
            else:
                # write to odd.txt
                output_odd.write(str(input_num) + "\n")

# === start ===
process()
