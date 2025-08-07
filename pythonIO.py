# Read from file
with open("assets/note.txt", "r") as file:
    content = file.read()

s = input("Enter your name: ")

# Write to file
with open("output.txt", "a") as file:
    file.write("Hello from "+s+"!\n")