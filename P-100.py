class Atm():
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin
        
    def checkbalance(self):
        print("Your balance is 50000")

    def withdrawl(self, amount):
        newamount=50000-amount
        print("You have withdrawn"+str(amount)+"an your remaining Balance is"+str(newamount))

def main():
    cardnumber=input("Insert your card number")
    pin=input("Enter your pin")
    user=Atm(cardnumber,pin)
    print("press 1 for balance enquiry and press 2 for withdrawl")
    activity=int(input("enter your choice"))
    if(activity==1):
        user.checkbalance()

    elif (activity==2):
        amount=amount=int(input("Enter the amount"))
        user.withdrawl(amount)
        
    else:
        print("Enter a valid number")
    
if __name__ == "__main__":
    main()
        