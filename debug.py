from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Levi")
c2 = Customer("muturi")
coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")


order1 = c1.create_order(coffee1, 4.5)
order2 = c1.create_order(coffee2, 3.0)
order3 = c2.create_order(coffee1, 5.5)


print(f"{c1.name} ordered {[coffee.name for coffee in c1.coffees()]}")
print(f"{c2.name} ordered {[coffee.name for coffee in c2.coffees()]}")
print(f"{coffee1.name} has {coffee1.num_orders()} orders with avg price {coffee1.average_price():.2f}")
print(f"{coffee2.name} has {coffee2.num_orders()} orders with avg price {coffee2.average_price():.2f}")

print(f"Order3: {order3.customer.name} ordered {order3.coffee.name} for ${order3.price}")
