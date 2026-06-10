name = "Chirag"
age = 30
skills = ["JS", "React", "CSS"]
new_Skill = "Python"
skills.append(new_Skill)

person = {
    "Name": name,
    "Age": age,
    "Goal": "AI-Engineer"
}
print(person["Goal"])

def greet(name):
    return f"Hello {name}, Go for it"

print(greet(name))

# Addition of second function

def additional(n1, n2):
    return n1+n2

print(additional(10,40))

print(f"Hello! My name is {name}, my age is {age} and know the following skills:{','.join(skills)}")