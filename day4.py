developer ={
    "name": "Chirag",
    "current_ctc": 23,
    "skills": ["React", "JS", "Python"],
    "target": {
        "role": "AI Engineer",
        "ctc": 30,
        "deadline": "October 2026"
    }
}

print(developer["name"])
print(developer["target"]["role"])
print(developer["skills"][0])

for key, value in developer.items():
    print(f"{key}:{value}")