
import sys

def ratings_output():
    """ Reads given file, then spits out the ratings in alphabetical order by restaurant. 
    """

    restaurant_data = open(sys.argv[1])
    zagat = {}
    for line in restaurant_data:
        restaurant, score = line.rstrip().split(":")
        zagat[restaurant] = score
    for restaurant in sorted(zagat):
        print "{} is rated at {}.".format(restaurant, zagat[restaurant])

ratings_output()