from pathlib import Path

path = Path(r"C:\tgs\koding\prokom\pitonchapsepuluhsatu.txt")
contents = path.read_text()

for line in contents.splitlines():
    print(line.replace("Python", "C"))