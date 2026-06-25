def get_profile(name, ctc):
    new_ctc = ctc*1.30
    return name, new_ctc

person, salary = get_profile("Chirag", 23)
print(f"{person} after 30% hike {salary:.2f} LPA")