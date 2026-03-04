class Atm:
   
    def __init__(self):
      self.pin = "123"
      self.balance = 0

      self.menu()
      

    def menu(self):
       user_input = input('''
                          Welcome to the ATM. Please choose an option: 
                          \n1. Create Pin
                          \n2. Check Balance
                          \n3. Deposit
                          \n4. Withdraw
                          \n5. Exit\n''')
       
       if user_input == '1':
          print("Create Pin")
        
       elif user_input == '2':
            print("Deposit")

       elif user_input == '3':
            print("Withdraw")
        
       elif user_input == '4':
           print("Withdraw")
       
       elif user_input == '5':
           print("Exit")