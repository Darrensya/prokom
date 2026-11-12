import json
from pathlib import Path

path = Path("C:\tgs\koding\prokom\favnum.json")
contents = path.read_text()
number = json.loads(contents)

print(f"Angka favmu adalah{number}.")