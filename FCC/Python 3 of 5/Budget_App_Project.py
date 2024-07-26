class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []

    def deposit(self,amount,description=''):
        self.ledger.append({"amount": amount, "description":description})

    def withdraw(self,amount,description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount,"description": description})
            return True
        return False

    def get_balance(self):
        return sum([i['amount'] for i in self.ledger])

    def transfer(self,amount,category):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount,"description": f'Transfer to {category.name}'})
            category.ledger.append({"amount": amount,"description": f"Transfer from {self.name}"})
            return True
        return False
    
    def check_funds(self,amount):
        if amount > sum([i['amount'] for i in self.ledger]):
            return False
        return True
    
    def __str__(self):
        result = f'{self.name:*^30}\n'
        for i in self.ledger:
            if len(i['description'])<=23:
                result += f"{i['description']:<23} {i['amount']:>5.2f}\n" 
            else:
                result += f"{i['description']:<.23} {i['amount']:>5.2f}\n"
        
        result += f"Total: {sum([i['amount'] for i in self.ledger]):.2f}"
        return result


def create_spend_chart(categories):
    # Title of the chart
    string = "Percentage spent by category\n"
    
    # Calculate total spent in all categories
    total_spent = sum(sum(-item['amount'] for item in cat.ledger if item['amount'] < 0) for cat in categories)
    
    # Calculate spending percentages for each category
    spending_percentages = []
    for category in categories:
        total_spent_in_category = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        spending_percentages.append((total_spent_in_category / total_spent) * 100)
    
    # Round down to the nearest 10
    rounded_percentages = [int(percent // 10) * 10 for percent in spending_percentages]
    
    # Create the chart with percentages
    for i in range(100, -1, -10):
        string += f"{i:>3}|"
        for percent in rounded_percentages:
            if percent >= i:
                string += " o "
            else:
                string += "   "
        string += " \n"
    
    # Add the bottom line
    string += "    " + "-" * (3 * len(categories) + 1) + "\n"
    
    # Add the category names
    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        string += "    "
        for cat in categories:
            if i < len(cat.name):
                string += f" {cat.name[i]} "
            else:
                string += "   "
        string += " \n"
    
    return string.rstrip("\n")  # Remove the trailing newline
food = Category("Food")
food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
print(food)
print(create_spend_chart([food]))