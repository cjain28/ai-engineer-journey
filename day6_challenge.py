class Skill:
    def __init__(self, name, years_experience):
        self.name = name
        self.years_experience = years_experience

    def level(self):
        if self.years_experience < 1:
            return "Beginner"
        elif self.years_experience < 3:
            return "Mid"
        elif self.years_experience >= 3:
            return "Senior"

React = Skill("React", 5)
Python = Skill("Python", 0)
Js = Skill("JS", 6)
print(f"{React.name}: {React.level()}")
print(f"{Python.name}: {Python.level()}")
print(f"{Js.name}: {Js.level()}")

class AISkill(Skill):
    def __init__(self, name, years_experience, framework):
        super().__init__(name, years_experience)
        self.framework = framework

    def describe(self):
        print(f"{self.framework} ({self.name}): {self.level()} level")

new_Skill = AISkill("AI", 5, "langChain")
new_Skill.describe()
