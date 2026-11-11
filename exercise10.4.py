from pathlib import Path

name = input("siapa namamu? ")

path = Path(r"C:\tgs\koding\prokom\pitonchapsepuluhsatu.txt")
path.write_text(name)

print(f"Baik, {name}! Namamu sudah dicatat.")