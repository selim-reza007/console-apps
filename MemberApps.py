


import os
clear = lambda : os.system('cls')

class Member:
    def __init__(self, name, bill, month):
        self.name = name
        self.bill = bill
        self.month = month

class Mess:
    def __init__(self):
        self.members = []
    
    def add_member(self, member):
        self.members.append(member)
        print(f"New member {member.name} is joined our mess")

    def all_members(self):
        for member in self.members:
            print("name : ", member.name)
            print("bill : ", member.bill)
            print("month : ", member.month)
            print("-----------------------------------")

    def delete_member(self):
        pass


def display_menu():
    print("Press 1 to add new member --")
    print("Press 2 to delete member --")
    print("Press 3 to see all members --")
    print("Press 4 to clear colsole --")
    print("Press 5 to terminate program --")

def main():
    mess = Mess()
    display_menu()
    while True:
        choice = input("-- Enter choice from 1 to 4 -- : ")
    
        if choice == "1":
            name = input("Enter name : ")
            bill = input("Enter bill : ")
            month = input("Enter month : ")
            member = Member(name, bill, month)
            mess.add_member(member)
        elif choice == "2":
            pass
        elif choice == "3":
            mess.all_members()
        elif choice == "4":
            clear()
            display_menu()
        elif choice == "5":
            break
        else:
            print("Not a valid number! --")

if __name__ == "__main__":
    main()