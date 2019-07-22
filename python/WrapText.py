##PROBLEM STATEMENT##
#You are given a string and width .
#Your task is to wrap the string into a paragraph of width .

j = 0
i = 0

print ("This program gets a String to be Wrapped & Wrap length")

wrap_string = input("please enter the String to be Wrapped : ")
wrap_string_len = int(input("please enter the Wrap length : "))

total_str_len = len(wrap_string)

for j in range(total_str_len):
    print(wrap_string[j], end="")
    i = i+1
    if i == wrap_string_len:
        print()
        i = 0
