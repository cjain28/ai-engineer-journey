developer = {
    "name":"Chirag",
    "skills": ["react", "JS", "Python"],
    "ctc": "85000",
    "target_ctc": "110000"
}

for key, value in developer.items():
    print(f"{key}:{value}")

salary = developer.get("salary", "Sal not Found")
print(salary)

try:
    print(developer["age"])
except KeyError:
    print("Value does not exist")