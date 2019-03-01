import requests

from video import Video

class Pricer(object):

    def price(self, imdbID):

        response = requests.get("http://www.omdbapi.com/?i=" + imdbID + "&apikey=6487ec62")

        json = response.json()

        title = json["Title"]
        rating = float(json["imdbRating"])

        price = 3.95

        if rating > 7:
            price += 1.0

        if rating < 4:
            price -= 1.0

        return Video(imdbID, title, rating, price)