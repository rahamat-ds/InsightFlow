import random
from datetime import datetime, timedelta
import pandas as pd
from faker import Faker
from core.geo import REGIONS, CITIES, WAREHOUSES, get_region
from core.products import PRODUCTS, CATEGORY_COST_RATIO
from core.customers import (
    GENDERS,
    LOYALTY_TIERS,
    PAYMENT_METHODS,
)

fake = Faker("en_IN")


def generate_customer():
    customer_id = f"CUST-{random.randint(1, 99999):05d}"
    customer_name = fake.name()
    gender = random.choice(GENDERS)
    age = random.randint(18, 70)
    state = random.choice(list(CITIES.keys()))
    city = random.choice(CITIES[state])
    region = get_region(state)
    loyalty_tier = random.choices(
    population=LOYALTY_TIERS,
    weights=[50, 30, 15, 5],
    k=1
)[0]
    payment_method = random.choices(
    population=PAYMENT_METHODS,
    weights=[45, 20, 15, 10, 10],
    k=1
)[0]
    
    return {
    "customer_id": customer_id,
    "customer_name": customer_name,
    "gender": gender,
    "age": age,
    "state": state,
    "city": city,
    "region": region,
    "loyalty_tier": loyalty_tier,
    "payment_method": payment_method,
}


def generate_product():

    # Choose a product category
    category = random.choice(list(PRODUCTS.keys()))

    # Choose a subcategory within that category
    subcategory = random.choice(
        list(PRODUCTS[category].keys())
    )

    # Choose a product from the selected subcategory
    product = random.choice(
        PRODUCTS[category][subcategory]
    )

    # Generate quantity
    quantity = random.randint(1, 4)

    # Selling price fluctuates ±5% around the base price
    selling_price = int(
        product["base_price"] *
        random.uniform(0.95, 1.05)
    )

    # Estimate unit cost
    unit_cost = int(
        selling_price *
        CATEGORY_COST_RATIO[category]
    )

    return {
        "category": category,
        "subcategory": subcategory,
        "product_name": product["name"],
        "manufacturer": product["brand"],
        "sku": product["sku"],
        "quantity": quantity,
        "selling_price": selling_price,
        "unit_cost": unit_cost,
    }

if __name__ == "__main__":

    print("CUSTOMER")
    print(generate_customer())

    print("\nPRODUCT")
    print(generate_product())