class Developer:
    def __init__(self, name, ctc):
        self.name = name
        self.ctc = ctc

    def introduce(self):
        print(f"Hi I am {self.name} and my ctc is {self.ctc} LPA")

    def get_Hike(self, target_ctc):
        hike = ((target_ctc - self.ctc)/self.ctc) *100
        return f"{self.name} needs {hike:.1f}% hike to reach {target_ctc} LPA"

chirag = Developer("Chirag", 23) #/*creating an object*/
chirag.introduce()
print(chirag.get_Hike(30))

class AIEngineer(Developer):
    def __init__(self, name, ctc, specialization):
        super().__init__(name, ctc) # calls the Developer class init
        self.specialization = specialization

    def introduce(self):
        print(f"Hi I am {self.name}, {self.specialization} engineer at {self.ctc} LPA")

future_chirag = AIEngineer("Chirag", 30, "AI")
future_chirag.introduce()
print(future_chirag.get_Hike(50))