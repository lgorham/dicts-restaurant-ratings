import sys

def ratings_output():
    """ Reads given file, then spits out the ratings in alphabetical order by restaurant. 

    """

    restaurant_data = open(sys.argv[1])
    zagat = {}
    for line in restaurant_data:
        line = line.rstrip().split(":")
        zagat[line[0]] = line[1]
    zagat_sorted = sorted(zagat)
    for restaurant in zagat_sorted:
        print "{} is rated at {}.".format(restaurant , zagat[restaurant])

ratings_output()