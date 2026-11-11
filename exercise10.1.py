from pathlib import Path

path = Path(r"C:\tgs\koding\prokom\pitonchapsepuluhsatu.txt")

contents = path.read_text()
print("Membaca seluruh file:")
print(contents)

lines = contents.splitlines()
print("Looping:")
for line in lines:
    print(line)