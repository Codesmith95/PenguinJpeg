import json
import os
import sys

allSubfolders = []

def main():
    print("Welcome to the generalizer! A program that attempts to generalize everything!")

    running = True
    while running:
        print("What would you like to generalize?")
        print("1. Pictures")
        print("2. JSON")
        print("3. Exit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            generalizePictures(allSubfolders)
        elif choice == "2":
            generalizeJSON(allSubfolders)
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            running = False
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def generalizeJSON(folder):
    word = input("Enter the word you want to replace all strings with: ")
    JSONFile = input("Enter the FULL path to the JSON file you want to generalize (e.g. C:\\Users\\Username\\Documents\\input.json): ")
    # Load the JSON file
    with open(JSONFile, "r") as f:
        data = json.load(f)

    def replace_strings(obj):
        if isinstance(obj, dict):
            return {k: replace_strings(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [replace_strings(v) for v in obj]
        elif isinstance(obj, str):
            return word
        else:
            return obj

    # Replace all strings with the specified word
    new_data = replace_strings(data)

    # Save back to a file
    with open(JSONFile, "w") as f:
        json.dump(new_data, f, indent=4)


def generalizePictures(folder):
    image = input("Enter the FULL path to the image you want to use as a generalizer (e.g. C:\\Users\\Username\\Pictures\\generalizer.png): ")

    folder = input("Enter the FULL path to the folder you want to generalize (e.g. C:\\Users\\Username\\Pictures\\Folder): ")

    allSubfolders = getAllSubfolders(folder)

    with open(image, "rb") as generalizer:
        generalizer_data = generalizer.read()

    for folder in allSubfolders:
        print(f"Folder: {folder}")
        for file in os.listdir(folder):
            if file.endswith(".png"):
                print(f"Generalizing {file}...")
                fileName = os.path.join(folder, file)

                newFile = open(fileName, "wb")
                newFile.write(generalizer_data)
                newFile.close()

def getAllSubfolders(folder):
    return [f.path for f in os.scandir(folder) if f.is_dir()]

if __name__ == "__main__":    main()