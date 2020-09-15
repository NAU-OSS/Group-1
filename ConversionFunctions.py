# function to extract the characteristic of any given number
def characteristicFun(numString, c):
    try:
        c[0] = int(float(numString))
        return True
    except:
        return False

# function to extract the mantissa of any given number
def mantissaFun(numString, numerator, denominator):
    try:
        value = numString.split(".")[1]
        numerator[0] = int(value)
        count = 1
        for i in value:
            count = count * 10
        denominator[0] = count
        return True
    except:
        return False

def main():
    # Declare Variables and convert number from list->str
    number = input("Enter a decimal number: ").split()
    number = str(number[0])
    
    numerator = [0]
    denominator = [0]
    characteristic = [0]
    if characteristicFun(number, characteristic) and\
    mantissaFun(number, numerator, denominator):
        print("\nCharacteristic:", characteristic[0])
        print("Mantissa:", numerator[0], "/", denominator[0])
    else:
        print("Error!")

if __name__ == "__main__":
    main()
