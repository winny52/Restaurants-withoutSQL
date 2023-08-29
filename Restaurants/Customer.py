from Review import Review        
class Customer:
    # Constructor
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self._reviews = []

    # Reader methods
    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    # Class variable to store all instances
    all_customers = []

    @classmethod
    def all(cls):
        return cls.all_customers
    
    def add_review(self, restaurant, rating):
        review = review(self, restaurant, rating)
        self._reviews.append(review)
        restaurant.add_review(review)

    def restaurants(self):
        restaurant_set = set()  # To store unique restaurants
        for review in self._reviews:
            restaurant_set.add(review.restaurant())
        return list(restaurant_set)
    

    def num_reviews(self):
        return len([review for review in Review.all() if review.customer() == self])
    
    @classmethod
    def find_by_name(cls, full_name):
        for customer in cls.all():
            if customer.full_name() == full_name:
                return customer
        return None
    
    @classmethod
    def find_all_by_given_name(cls, given_name):
        matching_customers = []
        for customer in cls.all():
            if customer.given_name() == given_name:
                matching_customers.append(customer)
        return matching_customers

