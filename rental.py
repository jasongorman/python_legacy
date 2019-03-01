from pricer import Pricer


class Rental(object):

    def __init__(self, customer, imdbID):
        self.customer = customer
        self.video = Pricer().price(imdbID)

    def __str__(self):
        return "Video Rental - customer: " + self.customer \
               + ". Video => title: " + self.video.title \
               + ", price: £" + str(self.video.price)
