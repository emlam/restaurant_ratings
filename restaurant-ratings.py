#Pair programming emilymlam & tjhakseth
def restaurant_rating (filename):
    file_to_open = open(filename)
    
    restaurant_list = {}

    for line in file_to_open:
        restaurant_name, rating = line.rstrip().split(":")
        restaurant_list [restaurant_name] = rating


    sorted_keys = sorted(restaurant_list.keys())
    print sorted_keys 

    for key in sorted_keys:






        #key = sorted(restaurant_file[0])
        #restaurant_list = (key: 0)

        # for rating in restaurant_list:
        #     restaurant_list[rating] = sorted(restaurant_list.get(rating, 0))

restaurant_rating("scores.txt")