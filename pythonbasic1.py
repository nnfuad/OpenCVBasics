# List
colors = ["red", "green", "blue"]
print(colors[1])  # green

# Tuple (immutable) ordered, unchangeable, and allow duplicate values
point = (10, 20)
print(point)

# Dictionary (key-value)
student = {"name": "Fuad", "dept": "ECE", "year": 2}
print(student["name"])  # Fuad

# for loop
for color in colors:
    print(color)

# while loop
i = 0
while i < 3:
    print(i)
    i += 1
    
def greet(name):
    print("Hello, " + name)

s=input("Enter your name: ")
greet(s)  # Hello, _name