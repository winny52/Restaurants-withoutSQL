class Customer:
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name


    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    all_customers = []

    @classmethod
    def all(cls):
        return cls.all_customers

# Creating instances
customer1 = Customer("John", "Doe")
customer2 = Customer("Jane", "Smith")

# Adding instances to the class variable
Customer.all_customers.append(customer1)
Customer.all_customers.append(customer2)

# Accessing customer data
print(customer1.given_name)  # John
print(customer2.full_name())  # Jane Smith

# Accessing all customer instances
all_customers = Customer.all()
for customer in all_customers:
    print(customer.full_name())

class Restaurant:
    def __init__(self, name):
        self._name = name
        self.reviews = []

    def name(self):
        return self._name

    
class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating_value = rating
        Review.all_reviews.append(self)

    def rating(self):
        return self.rating_value

    @classmethod
    def all(cls):
        return cls.all_reviews

