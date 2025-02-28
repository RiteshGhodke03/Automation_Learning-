# Encapsulation protects data by making variables private (__variable).

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  #private Variable

    def get_balance(self):
        return self.__balance


#creating object
account = BankAccount(1000)
print(account.get_balance())  #output:- 1000
#print(account.__balance)  #Error: cannot access private variable
