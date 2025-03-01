# P:
#   Input: An integer, and a list of transactions
#   Output: A list containing only the transactions for the specified inventory item
#   Explicit:
#       Looking at the example its a list of dictionaries where each dictionary contains an id, a movement, and a quantity

def transactions_for(number_id, list_of_trans):
    new_list = []
    for dictionary in list_of_trans:
        if number_id in dictionary.values():
            new_list.append(dictionary)

    return new_list

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

print(transactions_for(101, transactions) ==
      [
          {"id": 101, "movement": "in",  "quantity":  5},
          {"id": 101, "movement": "in",  "quantity": 12},
          {"id": 101, "movement": "out", "quantity": 18},
      ]) # True

# Idk how my solution works
def transactions_for(inventory_item, transactions):
    return [transaction
            for transaction in transactions
            if transaction["id"] == inventory_item]