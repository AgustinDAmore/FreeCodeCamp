import Budget
import CreateSpendChart

food = Budget.Category("Food")

food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())

clothing = Budget.Category("Clothing")

food.transfer(50, clothing)
clothing.withdraw(25.55, "clothing")
clothing.withdraw(100)

auto = Budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15, "gas")
print(auto.get_balance())

print(food)
print("")
print(clothing)
print("")
print(auto)

print("")
print(CreateSpendChart.create_spend_chart([food, clothing, auto]))