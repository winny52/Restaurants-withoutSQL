from Review import Review

class Restaurant:
    def __init__(self, name):
        self._name = name
        self._reviews =[]

    def name(self):
        return self._name
 
    def add_review(self, review):
        self._reviews.append(review)

    def get_reviews(self):
        return Review.all()

    def customers(self):
        customer_set = set()  
        for review in self._reviews:
            customer_set.add(review.customer())
        return list(customer_set)
    
    def average_rating(self):
        total = sum(review.rating() for review in self.get_reviews())  
        if total == 0:
            return 0
        return total / len(self.get_reviews())