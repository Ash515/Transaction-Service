def account(accno,accname,accpin,balance):
    print("Your account Information")
    print("Account Number:",accno)
    print("Accountant Name:",accname)
    print("Account Pin:",accpin)
    print("Balance:",balance)
    print("\n \n Click the options")
    i=0
    while i<=3:
     choice=int(input("1. Deposit\n 2. Withdraw\n 3.Check Balance "))
     if choice==1:
        deposit=int(input("Enter the deposit amount:"))
        if deposit>=100:
            balance=balance+deposit
            print("Thank you for deposition !")
            print("Total amount:",balance)
        else:
            print("Please deposit more than 100 Rs")
     elif(choice==2):
        withdrawamt=int(input("Enter the withdraw amount:"))
        if withdrawamt>=100:
            balance-=withdrawamt
            print("You have successfully withdrawn Rs",withdrawamt)
            print("Total amount:",balance)
        else:
            print("Please withdraw more than 100 Rs")
     elif(choice==3):
        print("Total amount:",balance)
     else:
        print("Invalid Choice!")
     i+=1

acno=input("Enter the Account Number:")
acname=input("Enter Accountant name: ")
acpin=input("Enter Account pin: ")
balance=0

account(acno,acname,acpin,balance)
