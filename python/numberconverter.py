import sys
import re

# I have this set up in my bash profile as:
#   alias convert="python3 PATH/TO/FILE/numberconverter.py"
# So that I can call it with convert <number>

# arg 1: num

def decimal(num):
    print("Binary:      ", bin(num))
    print("Hexadecimal: ", hex(num)) 
    print("Octal:       ", oct(num))
    return

def hexa(num):
    print("Decimal:     ", int(num,16))
    print("Binary:      ", bin(int(num,16)))
    print("Octal:       ", oct(int(num,16)))

def bina(num):
    print("Decimal:     ", int(num,2))
    print("Hexadecimal: ", hex(int(num,2)))
    print("Octal:       ", oct(int(num,2)))

def octa(num):
    print("Decimal:     ", int(num,8))
    print("Hexadecimal: ", hex(int(num,8)))
    print("Binary:      ", bin(int(num,8)))

def get_format(num):
    match num[:2]:
        case "0x": return "hex"
        case "0o": return "oct"
        case "0b": return "bin"
        case _: return "dec"

def main():
    if len(sys.argv) == 2:
        num = sys.argv[1]
    elif len(sys.argv) == 2 and sys.argv[1] == '-h':
        print("\nNUMBER CONVERTER HELP")
        print("Usage: numberconverter.py <NUMBER>")
        print("  Where <NUMBER> is the number you would like to convert. Please use prefix 0x for") 
        print("  hex numbers, 0b for binary, and 0o for octal. Decimal numbers require no prefix.\n")
        print("If the argument is omitted, the program will ask you to interactively enter")
        print("your number\n")
        exit()
    else:
        num = input("Please enter your number: ")
    t = get_format(num)
    print("\nYou entered %s. This number is in %s format.\n" % (num, t))
    match t:
        case "dec":
            try:
                num = eval(num)
                decimal(num)
            except:
                print("That is not a valid number")
        case "hex":
                try: 
                    hexa(num)
                except:
                    print("That is not a valid number")
        case "bin" :
                try:
                    bina(num)
                except:
                    print("That is not a valid number")
        case "oct":
                try:
                    octa(num)
                except:
                    print("That is not a valid number")
    exit()

if (__name__ == "__main__"):
    main()
