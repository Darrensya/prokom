def make_sandwich(*items):
    print("\nMembuat sandwhich dari bahan-bahan berikut:")
    for item in items:
        print(f"  - {item}")


make_sandwich('turkey', 'selada')
make_sandwich('beef', 'keju', 'tomat', 'ketchup')
make_sandwich('mustard', 'pickle', 'timun')