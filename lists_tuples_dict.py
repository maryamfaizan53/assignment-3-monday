# list
#mutable
fruits = ["Apple", "Banana", "Mango", "Orange"]
fruits.append("Pineapple")
fruits.pop(1)
fruits.remove("Mango")

for i in fruits:
    print(i)
    
def check_fruit(name):
     return name in fruits
     print(check_fruit("Apple"))   
     
     
# tuple 
# immutable... we can change tuple into list also
fruits = ("Apple", "Banana", "Mango", "Orange")
for i in fruits:
    print(i)

# dictionary

student = {
    "name": "Maryam",
    "age": 20,
    "courses": ["Math", "Science"]
}

print(student["name"])
print(student.get("phone", "Not Found"))
student["phone"] = "555-5555"
student["name"] = "John"
print(student["phone"])