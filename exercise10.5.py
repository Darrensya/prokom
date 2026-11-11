from pathlib import Path

names = []

print("MAsukkan nama.")
print("(Enter 'q' at any time to quit.)")

while True:
    name = input("\nName: ")
    if name == "q":
        break
    names.append(name)
    print(f"Selamat datang, {name}!")


contents = "\n".join(names)
path = Path("C:\tgs\koding\prokom\pitonchapsepuluhsatu.txt")
path.write_text(contents)

print(f"\nSaved {len(names)} name(s) to {path}.")