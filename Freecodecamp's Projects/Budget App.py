class Category :
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.total = 0

    def deposit(self, amount, description=""):  
        self.total += amount
        self.ledger.append({"amount": float(amount), "description": description})

    def withdraw(self, amount, description="" ): 
        if self.check_funds(amount):   
            self.total -= amount      
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self): 
        return self.total

    def transfer(self, amount, category2):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to "+ category2.category)
            category2.deposit(amount, "Transfer from "+ self.category)
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.total :
            return False
        else:
            return True

    def __str__(self):    
        x = str(self.category).center(30,'*') + '\n'
        for i in self.ledger:
            line = f"{i['description'][:23]:23}{i['amount']:7.2f}"
            x += f'{line}\n'
        x += "Total: " + str(self.get_balance())
        return x

def create_spend_chart(categories):
    names_list = []
    withd_list = []
    for category in categories:
        names = category.category
        names_list.append(names)
        height = (len(max(names_list, key=len)))
        padded = [word.ljust(height)for word in names_list]

        w_total = 0
        for item in category.ledger:
            amount = item['amount']
            if amount < 0:
                w_total += amount
        withd_list.append(w_total)
    total = int(round(sum(withd_list)))
    percentages = []
    for x in withd_list:
        per = x * 100 / total
        per = round(per//10)*10
        percentages.append(per)
      
    chart = "Percentage spent by category\n"
    for x in reversed(range(0, 110, 10)):
        chart += f"{str(x) + '|' :>4}"
        for percent in percentages:
          if percent >= x:
            chart += " o "
          else :
            chart += "   "
        chart += ' \n'
    chart += "    " + ("-" * ((len(names_list) + 2) * 2)) + '\n'

    for row in zip(*padded):
        chart += ('     ' + '  '.join(row)) + '  \n'

    return chart.rstrip("\n")
    


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))
