class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.all_restaurants.append(self)

    def get_name(self):
        return self.name

    def get_reviews(self):
        return self.reviews

    def get_customers(self):
        customer_list = []
        for review in self.reviews:
            customer_list.append(review.get_customer())
        return customer_list

    @classmethod
    def get_all_restaurants(cls):
        return cls.all_restaurants
