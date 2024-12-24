import random

def read_names_from_file():
    try:
        with open("names.txt", "r") as file:
            names = [line.strip() for line in file if line.strip()]
        return names
    except FileNotFoundError:
        print("Error: 'names.txt' file not found. Please ensure it is in the same directory as the program.")
        return []

def match_names(names):
    random.shuffle(names)
    matches = list(zip(names, names[1:] + [names[0]]))
    return matches

def main():
    print("Reading names from 'names.txt'...")
    names = read_names_from_file()

    if len(names) < 4:
        print("Error: Please add at least 4 names to 'names.txt'.")
        return

    matches = match_names(names)

    print("\nMatches:")
    for match in matches:
        print(f"{match[0]} -> {match[1]}")

if __name__ == "__main__":
    main()
