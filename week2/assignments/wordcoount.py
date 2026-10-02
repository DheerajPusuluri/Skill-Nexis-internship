filename = input("Enter the file name: ")
try:
    with open(filename, "r") as file:
        text = file.read()
    lines = text.splitlines()
    line_count = len(lines)
    words = text.split()
    word_count = len(words)
    character_count = len(text)
    print("\n--- File Statistics ---")
    print("Number of lines:", line_count)
    print("Number of words:", word_count)
    print("Number of characters:", character_count)
except FileNotFoundError:
    print("File not found.")