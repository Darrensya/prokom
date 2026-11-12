from pathlib import Path

filenames = ["C:\tgs\koding\buku.txt"]

for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Sorry, the file {filename} is missing.")
        continue

    lowered = contents.lower()
    count_the = lowered.count("the")
    count_the_space = lowered.count("the ")

    print(f"\n{filename}:")
    print(f"  'the'  appears about {count_the:,} times.")
    print(f"  'the ' appears about {count_the_space:,} times.")
