REGIONS = {
    "North": [
        "Delhi",
        "Punjab",
        "Haryana",
        "Uttar Pradesh",
        "Rajasthan"
    ],
    "South": [
        "Karnataka",
        "Tamil Nadu",
        "Kerala",
        "Telangana"
    ],
    "East": [
        "West Bengal",
        "Odisha",
        "Bihar",
        "Jharkhand"
    ],
    "West": [
        "Maharashtra",
        "Gujarat",
        "Goa"
    ]
}

CITIES = {

    "West Bengal": [
        "Kolkata",
        "Howrah",
        "Siliguri",
        "Durgapur"
    ],

    "Maharashtra": [
        "Mumbai",
        "Pune",
        "Nagpur",
        "Nashik"
    ],

    "Karnataka": [
        "Bengaluru",
        "Mysuru",
        "Mangaluru",
        "Udupi"
    ],

    "Delhi": [
        "New Delhi"
    ],

    "Tamil Nadu": [
        "Chennai",
        "Madurai",
        "Coimbatore",
        "Ooty"
    ],
    # ...
}


WAREHOUSES = {
    "East": "Kolkata FC",
    "West": "Mumbai FC",
    "North": "Delhi FC",
    "South": "Bengaluru FC"
}

def get_region(state: str) -> str:
    for region, states in REGIONS.items():
        if state in states:
            return region

    raise ValueError(f"Unknown state: {state}")