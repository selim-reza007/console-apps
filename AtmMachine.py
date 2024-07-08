


import os
clear = lambda: os.system("cls")

class CardHolder:
    def __init__(self, cardNumber, pin, holderName, balance):
        self.cardNumber = cardNumber
        self.pin = pin
        self.holderName = holderName
        self.balance = balance
    
    #getter methods
    def get_cardNumber(self):
        return self.cardNumber
    def get_pin(self):
        return self.pin
    def get_holderName(self):
        return self.holderName
    def get_balance(self):
        return self.balance
    
    #setter methods
    def set_cardNumber(self, cardNumber):
        self.cardNumber = cardNumber
    def set_pin(self, pin):
        self.pin = pin
    def set_holderName(self, holderName):
        self.holderName = holderName
    def set_balance(self, balance):
        self.balance = balance

    #display card holder info
    def display_card_holder(self):
        print(f"Card number : {self.cardNumber}\nPIN : {self.pin}\nHolder Name : {self.holderName}\nAvailable balance : {self.balance}\n")
    
    def view_balance(self):
        print(f"Your avaiable balance is : {self.balance} taka.\n")

    def add_money(self, newBalance):
        self.balance += newBalance
        print(f"Your acount is credited {newBalance} taka.\nYour updated balance is {self.balance} taka.\n")

    def withdrawal(self, newBalance):
        if newBalance > self.balance:
            print("Sorry! Insufficient balance.\n")
        else:
            self.balance -= newBalance
            print(f"You have successfully withdrawal {newBalance} taka.\nYour updated balance is {self.balance} taka.\n")

#display menu
def display_menu():
    print("Enter 1 to withdraw balance.")
    print("Enter 2 to add balance.")
    print("Enter 3 to view balance.")
    print("Enter 4 to clear console.")
    print("Enter 5 to terminate program.")

#driver code
def main():
    cardHolders_list = []
    cardHolders_list.append(CardHolder(45123567, 1234, "Selim Reza", 50))
    cardHolders_list.append(CardHolder(87452369, 2314, "Sagor Ali", 20))
    cardHolders_list.append(CardHolder(12356248, 5236, "Ramim Ali", 30))
    cardHolders_list.append(CardHolder(32501245, 7895, "Tofazzal", 40))
    cardHolders_list.append(CardHolder(85641230, 6932, "Mnsabbir", 70))

    #get cardNumber as input
    # inputCardNumber = None

    #check cardNumber
    available_cardHolder = None
    while True:
        if available_cardHolder == None:
            inputCardNumber = int(input("Enter your card number : "))
            for cardHolder in cardHolders_list:
                if(inputCardNumber == cardHolder.cardNumber):
                    available_cardHolder = cardHolder
                    break
            else:
                print("CardNumber didn't match! Enter valid card number.\n")
        else:
            break
    
    #check PIN
    while True:
        inputPin = int(input("Enter your PIN number : "))
        if(inputPin == available_cardHolder.pin):
            break
        
    clear()

    choice = None
    print(f"Welcome {available_cardHolder.holderName} :) \n")
    while True:
        display_menu()
        choice = int(input("Please select number 1 to 5 : "))
        if choice == 1:
            clear()
            withdrawalAmount = float(input("Enter amount you want to withdrawal : "))
            cardHolder.withdrawal(withdrawalAmount)
        elif choice == 2:
            clear()
            crediteAmount = float(input("How much taka you want to add : "))
            cardHolder.add_money(crediteAmount)
        elif choice == 3:
            clear()
            cardHolder.view_balance()
        elif choice == 4:
            clear()
        elif choice == 5:
            break
        else:
            print("You have choose the wrong number!\n")
    # while True:

    
if __name__ == "__main__":
    main()