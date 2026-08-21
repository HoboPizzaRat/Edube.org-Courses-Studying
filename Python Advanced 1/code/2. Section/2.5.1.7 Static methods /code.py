class Bank_Account:
    def __init__(self, iban):
        print('__init__ called')
        self.iban = iban

    # example of static method, take a note that it
    # doesnt require an self parameter, it doesnt affect the class
    # if the input parameter isnt the class itself
    @staticmethod
    def validate(iban):
        if len(iban) == 20:
            return True
        else:
            return False


account_numbers = ['8' * 20, '7' * 4, '2222']

# testig all the account numbers on account_numbers
# do they fit the validate functins defined correctness of
# what is a correct account_number
for element in account_numbers:
    if Bank_Account.validate(element):
        print('We can use', element, ' to create a bank account')
    else:
        print('The account number', element, 'is invalid')
