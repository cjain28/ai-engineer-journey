developer = {
    "name":"Chirag",
    "skills": ["react", "JS", "Python"],
    "ctc": "23LPA",
    "target_ctc": "35LPA"
}

for key, value in developer.items():
    print(f"{key}:{value}")

salary = developer.get("salary", "Sal not Found")
print(salary)

try:
    print(developer["age"])
except KeyError:
    print("Value does not exist")