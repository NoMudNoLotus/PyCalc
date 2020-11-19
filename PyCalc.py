#!/usr/bin/python3
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                         Made By: NoMudNoLotus                               #
#  A basic calculator for multiplication, Divison, Addition, and Subtraction  #
#  My first program in the Numbers SubCategory of karan's "MEGA PROJECT LIST" #
#  GitHub link to the "Mega Project List": https://kutt.it/SUJ7Os             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def Calc(a, b, opt):
    # Cats, formats, and prints the params
    if (opt == "+"):
        print( str(a) + " " + str(opt) + " " + str(b) + " = " + str(int(a) + int(b)) )
    if (opt == "-"):
        print( str(a) + " " + str(opt) + " " + str(b) + " = " + str(int(a) - int(b)) )
    if (opt == "*"):
        print( str(a) + " " + str(opt) + " " + str(b) + " = " + str(int(a) * int(b)) )
    if (opt == "+"):
        print( str(a) + " " + str(opt) + " " + str(b) + " = " + str(int(a) / int(b)) )

def main():  # Wrapper function
    opt = input("What kind of operation would you like to do?\nChoose between + - * / : ")
    if (opt not in "+-*/"):
        opt = input("Please choose a character for an arithmetic operation; must choose between '+' '-' '*' '/' : ")
    a = input("Please input value 1: ")
    b = input("Please input value 2: ")

    print(Calc(a, b, opt))
    

if __name__ == '__main__':
    main()

