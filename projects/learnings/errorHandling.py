developer = {"name":"chirag", "ctc":"85000"}

# try:
#     print(developer["salary"])
# except KeyError:
#     print("Key not Found")

salary = developer.get("salary", "Not Found")
print(salary)