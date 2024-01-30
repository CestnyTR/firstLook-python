def sum():
    num1 = int(input("sayı 1 :"))
    num2 = int(input("sayı 2 :"))
    total = num1+num2
    print("toplama işleminin sonucu : ", str(total))


def subtraction():
    num1 = int(input("sayı 1 :"))
    num2 = int(input("sayı 2 :"))
    print("Çıkarma işleminin sonucu : ", str(num1-num2))


def divide():
    num1 = int(input("sayı 1 :"))
    num2 = int(input("sayı 2 :"))
    print("Bölme işleminin sonucu : ", str(num1/num2))


def multiply():
    num1 = int(input("sayı 1 :"))
    num2 = int(input("sayı 2 :"))
    print("Çarpma işleminin sonucu : ", str(num1*num2))


class math:
    def calculate(operation):
        if operation == "+":
            sum()

        elif operation == "-":
            subtraction()

        elif operation == "/":
            divide()

        elif operation == "*":
            multiply()
        else:
            print("geçersiz işlem")
