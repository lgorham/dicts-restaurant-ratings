import sys

def zagat():
    """ Function manages the zagat dictionary through a central interface."""

    zagat_content = create_zagat()
    format_zagat(zagat_content)

    response = raw_input('Would you like to add an additional restaurant rating? Y/N\n').upper()
    if response == "Y":
        restaurant, score = add_restaurant_rating(zagat_content)
        zagat_content[restaurant] = score

        return format_zagat(zagat_content)


def create_zagat():
    """ Reads given file, then spits out the ratings in alphabetical order by restaurant."""

    restaurant_data = open(sys.argv[1])
    zagat = {}
    for line in restaurant_data:
        restaurant, score = line.rstrip().split(":")
        zagat[restaurant] = score

    restaurant_data.close()

    return zagat

    
def format_zagat(zagat_dict):
    """Sorts and prints the dictionary by alphabetical order"""

    zagat_sorted = sorted(zagat_dict)
    for restaurant in zagat_sorted:
        print "{} is rated at {}.".format(restaurant , zagat_dict[restaurant])


def add_restaurant_rating(rest_dictionary):
    """Asks the user for a new restaurant and corresponding rating"""

    new_restaurant = raw_input("Please give us the name of a restaurant not in our list: ").title()
    new_score = int(raw_input("What score would you give to that restaurant, 1 - 5: "))
    
    return [new_restaurant, new_score]


    
zagat()


