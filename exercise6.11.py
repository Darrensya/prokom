kota = {
    'jakarta': {
        'negara': 'indonesia',
        'populasi': 10500000,
        'fact': 'Ibukota Indonesia.',
    },
    'tokyo': {
        'negara': 'jepang',
        'populasi': 14000000,
        'fact': 'Ibukota Jepang.',
    },
    'Berlin': {
        'negara': 'german',
        'populasi': 3700000,
        'fact': 'Ibukota German.',
    },
}

for city, info in kota.items():
    print(f"{city.title()}:")
    print(f"  NEgara: {info['negara'].title()}")
    print(f"  Populasi: sekitar {info['populasi']:,}")
    print(f"  Fact: {info['fact']}")
    print()