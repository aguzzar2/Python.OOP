from bankAccount import *



def main():
    john = Checking("John", 50000)
    jill = Savings("Jill", 101000)
    print(john, jill)

    alpha_centurion = john + jill
    print(alpha_centurion)
if __name__ == "__main__":
    main()