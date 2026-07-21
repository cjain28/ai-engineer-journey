import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    print(response.status_code)

    data = response.json()
    name = data["name"]
    email = data["email"]
    city = data["address"]["city"]
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"City: {city}")

except requests.ConnectionError:
    print("No Internet Connection!")