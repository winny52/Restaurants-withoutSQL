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
# # Creating instances
# customer1 = Customer("John", "Doe")
# customer2 = Customer("Jane", "Smith")

# # Adding instances to the class variable
# Customer.all_customers.append(customer1)
# Customer.all_customers.append(customer2)

# # Accessing customer data
# print(customer1.given_name)  # John
# print(customer2.full_name())  # Jane Smith

# # Accessing all customer instances
# all_customers = Customer.all()
# for customer in all_customers:
#     print(customer.full_name())
