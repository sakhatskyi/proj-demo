from .processors import *

def receive_input() -> str:
    return input("Give your input")

def process_int_input(given_input):
    try:
        int_input = int(given_input)
    except:
        print('bad input')
        return False
    else:
        print('all good')
        process_int(int_input)


if __name__ == '__main__':
    given_input = receive_input()
    int_result = process_int_input(given_input=given_input)
    if not int_result:
        process_str
