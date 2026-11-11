from pathlib import Path

path = Path(r"C:\tgs\koding\prokom\pitonchapsepuluhsatu.txt")

contents = path.read_text()
print("Membaca seluruh file:")
print(contents)

print("Looping:")
for line in contents.splitlines():
    print(line)