import sys

from rental import Rental


def main():
    customer = sys.argv[1]
    imdbID = sys.argv[2]

    rental = Rental(customer, imdbID)

    print(rental)

if __name__ == "__main__": main()

    #
    # Example movies:
    #
    # tt0096754 - high rated
    # tt0060666 - low rated
    # tt0317303 - medium rated