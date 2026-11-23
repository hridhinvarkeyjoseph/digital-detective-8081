def main():
    print("Number System Converter")
    print("1. Decimal to binary, octal, and hexadecimal")
    print("2. Binary to decimal")
    print("3. Octal to decimal")
    print("4. Hexadecimal to decimal")

    choice = input("Choose 1-4: ").strip()

    try:
        if choice == "1":
            number = int(input("Enter a decimal number: "))
            print("Binary:", bin(number)[2:])
            print("Octal:", oct(number)[2:])
            print("Hexadecimal:", hex(number)[2:].upper())
        elif choice == "2":
            number = input("Enter a binary number: ")
            print("Decimal:", int(number, 2))
        elif choice == "3":
            number = input("Enter an octal number: ")
            print("Decimal:", int(number, 8))
        elif choice == "4":
            number = input("Enter a hexadecimal number: ")
            print("Decimal:", int(number, 16))
        else:
            print("Please choose a number from 1 to 4.")
    except ValueError:
        print("Invalid number. Please check your input.")

if __name__ == "__main__":
    main()
