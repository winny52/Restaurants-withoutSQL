class Restaurant:
    def __init__(self, name):
        self._name = name
        self.reviews =[]

    def name(self):
        return self._name
 
    def add_review(self, review):
        self._reviews.append(review)

    def get_reviews(self):
        return self._reviews

    def customers(self):
        customer_set = set()  # To store unique customers
        for review in self._reviews:
            customer_set.add(review.customer())
        return list(customer_set)