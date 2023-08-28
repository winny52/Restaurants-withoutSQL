from Customer import Customer
from Restaurant import Restaurant
from Review import Review

# Creating instances of Customer, Restaurant, and Review
customer1 = Customer("Winny", "Sigilai")
customer2 = Customer("Alice", "Smith")
restaurant1 = Restaurant("Zen Garden")
restaurant2 = Restaurant("Fogo Gaucho")

# Adding reviews
review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer2, restaurant1, 3)
review3 = Review(customer1, restaurant2, 5)

# Displaying customer name, restaurant name, and reviews
for review in Review.all():
    customer_name = review.customer().full_name()
    restaurant_name = review.restaurant().name()
    review_rating = review.rating()
    
    print(f"Customer: {customer_name}")
    print(f"Restaurant: {restaurant_name}")
    print(f"Review Rating: {review_rating}\n")
