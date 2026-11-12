import json
from pathlib import Path

path = Path("C:\tgs\koding\prokom\favnum.json")

if path.exists():
    number = json.loads(path.read_text())
    print(f"Angka favmu adalah {number}.")
else:
    number = input("Apa angka favmu? ")
    path.write_text(json.dumps(number))
    print("Oke aku akan mengingatnya.")