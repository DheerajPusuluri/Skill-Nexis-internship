import json
filename = input("Enter JSON file name: ")
try:
    with open(filename, "r") as file:
        data = json.load(file)
    print("\n--- JSON Data ---")
    print(json.dumps(data, indent=4))
except FileNotFoundError:
    print("File not found.")
except json.JSONDecodeError:
    print("Invalid JSON file.")