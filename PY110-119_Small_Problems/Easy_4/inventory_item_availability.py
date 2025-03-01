# P:
#   Input: An integer (item id) and a list(transactions)
#   Output: A boolean value if the sum of the quantity values of the item's transactions is greater than 0
#   Explicit:
#       Check all ids based on the input integer
#       For all id's associated with that number, subtract the 'out' quantities from the 'in' quantities
# E:
# D:
#   Lists, dictionary, boolean value,
# A:
#   1. Use the previous function to get the relevant ids
#   2. Set a new variable to 0
#   3. If the movement is set to 'in' add the amount to quantity
#   4. If set to out, subtract it.
#   5. Return the quantity greater than 0



def is_item_available(item, transactions):
    relevant_transactions = transactions_for(item, transactions)
    quantity = 0

    for transaction in relevant_transactions:
        if transaction["movement"] == 'in':
            quantity += transaction["quantity"]
        else:
            quantity -= transaction["quantity"]

    return quantity > 0

def transactions_for(inventory_item, transactions):
    return [transaction
            for transaction in transactions
            if transaction["id"] == inventory_item]

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True