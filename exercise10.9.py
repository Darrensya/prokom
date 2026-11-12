from pathlib import Path

filenames = [(r"C:\tgs\koding\prokom\kucing.txt"), (r"C:\tgs\koding\prokom\anjing.txt")]
for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        pass
    else:
        print(f"Contents of {filename}:")
        print(contents)