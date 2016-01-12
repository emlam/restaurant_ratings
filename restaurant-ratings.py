#Pair programming emilymlam & tjhakseth
def restaurant_rating (filename):
    file_to_open = open(filename)

    new_restaurant_name, new_restaurant_rating = new_restaurant()
    
    restaurant_list = {}

    restaurant_list[new_restaurant_name] = new_restaurant_rating

    for line in file_to_open:
        restaurant_name, rating = line.rstrip().split(":")
        restaurant_list[restaurant_name] = rating

    sorted_keys = sorted(restaurant_list.keys())
    for key in sorted_keys:
        print key + " : " + restaurant_list[key]

def new_restaurant():

    restaurant_name_input = raw_input("Enter restaurant name: ")
    restaurant_rating_input = raw_input("Enter restaurant score: ")
    return restaurant_name_input, restaurant_rating_input

restaurant_rating("scores.txt")