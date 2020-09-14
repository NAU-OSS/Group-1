def characteristicFun(numString, c):
    try:
        c[0] = int(float(numString))
        return True
    except:
        return False

def mantissaFun(numString, numerator, demoninator):
    try:
        value = numString.split(".")[1]
        numerator[0] = int(value)
        count = 1
        for i in value:
            count = count * 10
        demoninator[0] = count
        return True
    except:
        return False


def main():
    # Declare Variables
    number = "123.456"
    numerator = [0]
    demoninator = [0]
    characteristic = [0]

    if characteristicFun(number, characteristic) and mantissaFun(number, numerator, demoninator):
        print(characteristic[0])
        print(numerator[0])
        print(demoninator[0])
    else:
        print("Error!")


if __name__ == "__main__":
    main()

    
