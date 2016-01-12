#Pair programming emilymlam & tjhakseth
def restaurant_rating (filename):
    file_to_open = open(filename)
    
    restaurant_list = {}

    for line in file_to_open:
        restaurant_name, rating = line.rstrip().split(":")
        restaurant_list[restaurant_name] = rating

    sorted_keys = sorted(restaurant_list.keys())
    for key in sorted_keys:
        print key + " : " + restaurant_list[key]

restaurant_rating("scores.txt")