
PRODUCTS = {
    "Electronics": {
        "Smartphones": [
            {
                "name": "Apple iPhone 16",
                "brand": "Apple",
                "sku": "ELE-SP-001",
                "base_price": 79999
            },
            {
                "name": "Samsung Galaxy S25",
                "brand": "Samsung",
                "sku": "ELE-SP-002",
                "base_price": 74999
            },
            {
                "name": "OnePlus 13",
                "brand": "OnePlus",
                "sku": "ELE-SP-003",
                "base_price": 54999
            },
            {
                "name": "Google Pixel 10",
                "brand": "Google",
                "sku": "ELE-SP-004",
                "base_price": 69999
            }
        ],

        "Laptops": [
            {
                "name": "MacBook Air M4",
                "brand": "Apple",
                "sku": "ELE-LP-001",
                "base_price": 109999
            },
            {
                "name": "Dell Inspiron 15",
                "brand": "Dell",
                "sku": "ELE-LP-002",
                "base_price": 64999
            },
            {
                "name": "HP Pavilion 14",
                "brand": "HP",
                "sku": "ELE-LP-003",
                "base_price": 58999
            },
            {
                "name": "Lenovo ThinkPad E16",
                "brand": "Lenovo",
                "sku": "ELE-LP-004",
                "base_price": 72999
            }
        ],

        "Accessories": [
            {
                "name": "Wireless Mouse",
                "brand": "Logitech",
                "sku": "ELE-AC-001",
                "base_price": 1299
            },
            {
                "name": "Mechanical Keyboard",
                "brand": "Keychron",
                "sku": "ELE-AC-002",
                "base_price": 5499
            },
            {
                "name": "USB-C Hub",
                "brand": "Anker",
                "sku": "ELE-AC-003",
                "base_price": 2499
            },
            {
                "name": "Noise Cancelling Headphones",
                "brand": "Sony",
                "sku": "ELE-AC-004",
                "base_price": 12999
            }
        ]
    },

    "Fashion": {
        "Men": [
            {
                "name": "Cotton T-Shirt",
                "brand": "Levi's",
                "sku": "FAS-MN-001",
                "base_price": 799
            },
            {
                "name": "Slim Fit Jeans",
                "brand": "Wrangler",
                "sku": "FAS-MN-002",
                "base_price": 1999
            },
            {
                "name": "Running Shoes",
                "brand": "Puma",
                "sku": "FAS-MN-003",
                "base_price": 3499
            }
        ],

        "Women": [
            {
                "name": "Kurti",
                "brand": "Biba",
                "sku": "FAS-WM-001",
                "base_price": 1499
            },
            {
                "name": "Handbag",
                "brand": "Lavie",
                "sku": "FAS-WM-002",
                "base_price": 2499
            },
            {
                "name": "Sneakers",
                "brand": "Nike",
                "sku": "FAS-WM-003",
                "base_price": 4299
            }
        ]
    },

    "Home & Kitchen": {
        "Kitchen": [
            {
                "name": "Mixer Grinder",
                "brand": "Prestige",
                "sku": "HM-KT-001",
                "base_price": 3999
            },
            {
                "name": "Pressure Cooker",
                "brand": "Hawkins",
                "sku": "HM-KT-002",
                "base_price": 2499
            },
            {
                "name": "Air Fryer",
                "brand": "Philips",
                "sku": "HM-KT-003",
                "base_price": 6999
            }
        ],

        "Home Decor": [
            {
                "name": "Wall Clock",
                "brand": "Ajanta",
                "sku": "HM-HD-001",
                "base_price": 899
            },
            {
                "name": "Table Lamp",
                "brand": "Wipro",
                "sku": "HM-HD-002",
                "base_price": 1499
            },
            {
                "name": "Indoor Plant",
                "brand": "Ugaoo",
                "sku": "HM-HD-003",
                "base_price": 599
            }
        ]
    },

    "Books": {
        "Programming": [
            {
                "name": "Python Crash Course",
                "brand": "No Starch Press",
                "sku": "BK-PR-001",
                "base_price": 899
            },
            {
                "name": "Hands-On Machine Learning",
                "brand": "O'Reilly",
                "sku": "BK-PR-002",
                "base_price": 1099
            },
            {
                "name": "Designing Data-Intensive Applications",
                "brand": "O'Reilly",
                "sku": "BK-PR-003",
                "base_price": 1199
            }
        ],

        "Fiction": [
            {
                "name": "The Hobbit",
                "brand": "HarperCollins",
                "sku": "BK-FC-001",
                "base_price": 499
            },
            {
                "name": "1984",
                "brand": "Penguin",
                "sku": "BK-FC-002",
                "base_price": 399
            },
            {
                "name": "The Alchemist",
                "brand": "HarperOne",
                "sku": "BK-FC-003",
                "base_price": 350
            }
        ]
    }
}


CATEGORY_COST_RATIO = {
    "Electronics": 0.72,
    "Fashion": 0.45,
    "Home & Kitchen": 0.60,
    "Books": 0.55,
}

