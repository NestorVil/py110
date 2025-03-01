# P:
#   Input: A list
#   Output: A print statement: "element of list" => "the number of occurances of each element"
# Explicit:
#   If an element appears more than once, it needs to be "element: amount of times"
# E:
    # vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
    #             'motorcycle', 'motorcycle', 'car', 'truck']

    # count_occurrences(vehicles)
    # # your output sequence may appear in a different sequence
    # car => 4
    # truck => 3
    # SUV => 1
    # motorcycle => 2

#   Never empty, will need to print myself
# D:
#   For this I might want to use a dictionary to keep track then printt the "{key} => {value}"
#   Will then probably need f-strings
# A:
#   1. Create a new empty dictionary "new_dict"
#   2. Iterate over the input list
#   3. Count the amount of times one of those elements appears and add the count to the dictionary
#   4. Print out the key and value of the dictionary

def count_occurrences(vehicle_list):
    veh_occurances = dict()

    for vehicle in vehicle_list:
        veh_occurances[vehicle] = veh_occurances.get(vehicle, 0) + 1

    for key, value in veh_occurances.items():
        print(f"{key} => {value}")


vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)
# your output sequence may appear in a different sequence
# car => 4
# truck => 3
# SUV => 1
# motorcycle => 2

# I like this one
def count_occurrences(lst):
    for element in set(lst):                         # iterate over new set without duplicates
        print(f'{element} => {lst.count(element)}')  # use original list argument to count occurrences