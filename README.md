# coffee-shop-challenge.

A basic python object-oriented project that uses the `customer` `coffee`, and `order` models to simulate a coffee shop domain. class relationships, data validation and basic aggregation logic.

# Project structure
coffee-shop-challenge/
├── Pipfile
├── debug.py
├── customer.py
├── coffee.py
├── order.py
├── tests/
│ ├── customer_test.py
│ ├── coffee_test.py
│ └── order_test.py
└── README.md

# domain Overview
- `customer` has many `order`s.
- `coffee` has many `order`s.
- `order` belongs to both `customer` and `coffee`.
- many-to-many relationships between `customer` and `coffee`, via `order`.

### getting started

# 1. clone the repository

```bash
git clone git@github.com:youngpuffy/coffee-shop-challenge.git
cd coffee-shop-challenge

# 2. install dependencies(optional, if using pipenv)

pipenv install
pipenv shell

# 3. how to use
 python debug.py or python3 debug.py


 # 4. testing
 run all tests with:
 pytest


 
 # Features
1. Customer
__init__(self, name)

Store a name (must be a str, 1–15 characters).

Property name

Getter returns the customer’s name.

Setter enforces str type and 1–15 character length.

#2 .Coffee
__init__(self, name)

Store a name (must be a str, at least 3 characters).

Property name

Getter returns the coffee’s name.

Immutable once initialized.

# 3. Order
__init__(self, customer, coffee, price)

Accepts a Customer instance, a Coffee instance, and a price (float, 1.0–10.0).

Property price

Getter returns the order price.

Immutable once initialized; enforces type and range.

### 2. Object Relationships
Order.customer → returns the Customer instance (type-checked)

Order.coffee → returns the Coffee instance (type-checked)

Customer.orders() → all Order instances for that customer

Customer.coffees() → unique list of Coffee instances they’ve ordered

Coffee.orders() → all Order instances for that coffee

Coffee.customers() → unique list of Customer instances who’ve ordered it

### 3. Aggregates & Associations
Customer.create_order(coffee, price)
Instantiate a new Order, link it to this customer and the given coffee.

Coffee.num_orders()
Total count of orders for this coffee (0 if none).

Coffee.average_price()
Mean of all order prices for this coffee (0 if none).

### 4. Bonus (Optional)
Customer.most_aficionado(coffee) (classmethod)
Return the Customer Who’s spent the most on the given coffee (or None If no orders)