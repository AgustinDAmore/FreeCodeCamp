import budget
import create_spend_chart

food = budget.Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())

clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.deposit(150, "deposit")

clothing.withdraw(76.25, "hat")
clothing.withdraw(100, "boots")

auto = budget.Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(37.12, "gas")
print(auto.get_balance())

print(food)
print("")
print(clothing)
print("")
print(auto)

print("")
print(create_spend_chart.graphic([food, clothing, auto]))