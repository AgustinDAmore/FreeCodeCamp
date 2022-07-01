def graphic(categories):
    listSpent = []
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        listSpent.append(round(spent, 2))

    spent_percentage = list(map(lambda amount: int((((amount / sum(listSpent)) * 10) // 1) * 10), listSpent))

    structure = ""
    for value in reversed(range(0, 101, 10)):
        structure += str(value).rjust(3) + '|'
        for percent in spent_percentage:
            if percent >= value:
                structure += " o "
            else:
                structure += "   "
        structure += " \n"

    footer = "    " + "_" * ((3 * len(categories)) + 1) + "\n"
    descriptions = list(map(lambda category: category.description, categories))
    descriptions = list(map(lambda description: description.ljust(max(map(lambda description: len(description), descriptions))), descriptions))
    for x in zip(*descriptions):
        footer += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"

    return ("Percentage spent by category\n" + structure + footer).strip("\n")