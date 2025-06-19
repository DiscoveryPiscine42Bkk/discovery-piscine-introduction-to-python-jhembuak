# isneg.py

def main():
    try:
        number = int(input("Enter a number: "))
        if number < 0:
            print("This number is negative.")
        elif number > 0:
            print("This number is positive.")
        else:
            print("This number is both positive and negative.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
