
import random
from datetime import datetime, timedelta
from pathlib import Path
import pandas as pd
from faker import Faker

from core.geo import CITIES, WAREHOUSES, get_region
from core.products import PRODUCTS, CATEGORY_COST_RATIO
from core.customers import GENDERS, LOYALTY_TIERS, PAYMENT_METHODS
from core.logistics import (
    DELIVERY_PARTNERS,
    RTO_REASONS,
    SHIPPING_MODES,
    DELIVERY_DAYS,
    RTO_RATE,
    DISCOUNT_RANGE,
)

fake = Faker("en_IN")


def generate_customer():
    state = random.choice(list(CITIES.keys()))
    city = random.choice(CITIES[state])
    region = get_region(state)

    return {
        "customer_id": f"CUST-{random.randint(1,99999):05d}",
        "customer_name": fake.name(),
        "gender": random.choice(GENDERS),
        "age": random.randint(18,70),
        "state": state,
        "city": city,
        "region": region,
        "loyalty_tier": random.choices(LOYALTY_TIERS,[50,30,15,5])[0],
        "payment_method": random.choices(PAYMENT_METHODS,[45,20,15,10,10])[0],
    }


def generate_product():
    category = random.choice(list(PRODUCTS.keys()))
    subcategory = random.choice(list(PRODUCTS[category].keys()))
    p = random.choice(PRODUCTS[category][subcategory])
    qty = random.randint(1,4)
    selling = int(p["base_price"]*random.uniform(0.95,1.05))
    cost = int(selling*CATEGORY_COST_RATIO[category])
    return {
        "category":category,
        "subcategory":subcategory,
        "product_name":p["name"],
        "manufacturer":p["brand"],
        "sku":p["sku"],
        "quantity":qty,
        "selling_price":selling,
        "unit_cost":cost,
    }


def generate_shipping(region):
    warehouse = WAREHOUSES[region]
    partners = DELIVERY_PARTNERS[region]
    courier = random.choices(list(partners.keys()), weights=list(partners.values()))[0]
    mode = random.choices(list(SHIPPING_MODES.keys()), weights=list(SHIPPING_MODES.values()))[0]
    days = random.randint(*DELIVERY_DAYS[mode])
    rto = random.random() < RTO_RATE
    return {
        "warehouse":warehouse,
        "courier":courier,
        "shipping_mode":mode,
        "delivery_days":days,
        "rto":rto,
        "rto_reason": random.choice(RTO_REASONS) if rto else None,
    }


def calculate_finance(product):
    discount = random.randint(*DISCOUNT_RANGE)
    gross = product["selling_price"]*product["quantity"]
    revenue = int(gross*(100-discount)/100)
    cost = product["unit_cost"]*product["quantity"]
    return {
        "discount_percent":discount,
        "revenue":revenue,
        "cost":cost,
        "profit":revenue-cost,
    }


def generate_dates(shipping):
    start = datetime(2024,1,1)
    end = datetime(2025,12,31)
    order_date = start + timedelta(days=random.randint(0,(end-start).days))
    dispatch = order_date + timedelta(days=1)
    delivery = dispatch + timedelta(days=shipping["delivery_days"])
    return {
        "order_date":order_date.date(),
        "dispatch_date":dispatch.date(),
        "delivery_date":delivery.date(),
    }


def generate_order():
    customer=generate_customer()
    product=generate_product()
    shipping=generate_shipping(customer["region"])
    finance=calculate_finance(product)
    dates=generate_dates(shipping)
    return {**customer,**product,**shipping,**finance,**dates}


def generate_dataset(n_orders=1000):
    rows=[generate_order() for _ in range(n_orders)]
    df=pd.DataFrame(rows)
    outdir=Path("data/generated")
    outdir.mkdir(parents=True, exist_ok=True)
    outfile=outdir/"retail_orders.csv"
    df.to_csv(outfile,index=False)
    print(f"Saved {len(df)} rows to {outfile}")
    return df


if __name__=="__main__":
    order=generate_order()
    print(order)
    generate_dataset(1000)
