class cities:

    num_of_cities = 0

    def __init__(self, name, url, list):
        self.name = name
        self.url = url
        self.list = list

        cities.num_of_cities =+ 1

sacramento = cities('Sacramento','sacramento.com',(1, 2, 3))
print(sacramento.url)
