import sys

# I have this set up in my bash profile as:
#   alias convert="python3 PATH/TO/FILE/numberconverter.py"
# So that I can call it with convert <type> <number>


# arg 1: type of num (dec, hex, bin, oct)
# arg 2: num

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

def main():
    if len(sys.argv) == 3:
        t = sys.argv[1]
        num = sys.argv[2]
    elif len(sys.argv) == 2 and sys.argv[1] == '-h':
        print("\nNUMBER CONVERTER HELP")
        print("Usage: numberconverter.py <FORMAT> <NUMBER>")
        print("  Where <FORMAT> is the current format of your number, which is one of the following:")
        print("    - dec")
        print("    - bin")
        print("    - hex")
        print("    - oct")
        print("  Where <NUMBER> is the number you would like to convert. Please use prefix 0x for") 
        print("  hex numbers, 0b for binary, and 0o for octal. Decimal numbers require no prefix.\n")
        print("If one or both arguments are omitted, the program will ask you to interactively enter")
        print("your numbers and formats\n")
        exit()
    else:
        t = input("Please enter the format of your number (dec, hex, bin, oct): ")
        num = input("Please enter your numbner: ")
    print("\nYou entered %s. This number is in %s format.\n" % (num, t))
    match t:
        case "dec":
            try:
                num = eval(num)
                decimal(num)
            except NameError:
                print("That is not a valid number")
        case "hex":
                try: 
                    hexa(num)
                except ValueError:
                    print("That is not a valid number")
        case "bin" :
                try:
                    bina(num)
                except ValueError:
                    print("That is not a valid number")
        case "oct":
                try:
                    octa(num)
                except ValueError:
                    print("That is not a valid number")
        case _:
            print("format not recongnized\n")

if (__name__ == "__main__"):
    main()
