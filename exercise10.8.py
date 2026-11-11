from pathlib import Path

filenames = [(r"C:\tgs\koding\prokom\kucing.txt"), (r"C:\tgs\koding\prokom\anjing.txt")]

for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"maaf {filename} hilang.")
    else:
        print(f"isi dari {filename}:")
        print(contents)