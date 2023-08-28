from customer import Customer
from restaurant import Restaurant
from review import Review


#instances
customer1 = Customer("Brian", "Boss")
customer2 = Customer("Mike", "Moringa")
restaurant1 = Restaurant("Avocado Corner")
restaurant2 = Restaurant("Kibanasky")
review1 = Review(customer1, restaurant1, 4)
review2 = Review(customer2, restaurant1, 5)
review3 = Review(customer1, restaurant2, 3)

# Test the code here
print(customer1.get_full_name())
print(customer2.get_first_name())
print(restaurant1.get_name())
print(review1.get_rating())
print(review2.get_customer().get_full_name())
print(review3.get_restaurant().get_name())

