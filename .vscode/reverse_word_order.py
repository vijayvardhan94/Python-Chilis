input_string = input("enter a string")
def split_string(input_string):
    result = input_string.split()
    print(result[::-1])
    
split_string(input_string)
