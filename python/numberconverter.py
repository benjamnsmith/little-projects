import sys

# I have this set up in my bash profile as:
#   alias convert="python3 PATH/TO/FILE/numberconverter.py"
# So that I can call it with convert <type> <number>


# arg 1: type of num (dec, hex, bin, oct)
# arg 2: num

def decimal(num):
    print("Binary:      ",bin(num))
    print("Hexadecimal: ",hex(num)) 
    print("Octal:       ", oct(num))
    return

def hexa(num):
    print("Decimal:     ",int(num,16))
    print("Binary:      ", bin(int(num,16)))
    print("Octal:       ", oct(int(num,16)))

def bina(num):
    print("Decimal:     ",int(num,2))
    print("Hexadecimal: ", hex(int(num,2)))
    print("Octal:       ",oct(int(num,2)))

def octa(num):
    print("Decimal:     ",int(num,8))
    print("Hexadecimal: ",hex(int(num,8)))
    print("Binary:      ",bin(int(num,8)))

def main():
    t = sys.argv[1]
    num = sys.argv[2]
    if (t == "dec"):
        try:
            num = eval(num)
            decimal(num)
        except NameError:
            print("That is not a valid number")
    elif (t == "hex"):
        try: 
            hexa(num)
        except ValueError:
            print("That is not a valid number")
    elif (t == "bin"):
        try:
            bina(num)
        except ValueError:
            print("That is not a valid number")
    elif (t == "oct"):
        try:
            octa(num)
        except ValueError:
            print("That is not a valid number")
    else:
        print("format not recongnized\n")

if (__name__ == "__main__"):
    main()
