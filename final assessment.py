#Bank System
class Bank:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Balance:", self.balance)

b = Bank()
b.deposit(1000)
b.withdraw(400)
b.show_balance()


#Simple E-commerce cart system
cart = []

while True:
    print("\n1.Add Product  2.View Cart  3.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        product = input("Enter product name: ")
        cart.append(product)
        print("Product added")

    elif choice == "2":
     if not cart:
        print("Your cart is empty.")
     else:
        print("Cart Items:")
        for item in cart:
            print("-", item)


    elif choice == "3":
        break
