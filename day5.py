import requests


# print(response.status_code)
# print(response.json())
try:
    # response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    response = requests.get("https://fakeurl123456.com/todos/1")
    response.raise_for_status()

    data = response.json()

    print(f"Title: {data['title']}")
    print(f"Completed: {data['completed']}")
    print(f"User Id: {data['userId']}")

except requests.ConnectionError:
    print("No Internet Connection!")
except requests.exceptions.HTTPError:
    print("API returned an error")
except Exception as e:
    print(f"Something went wrong at {e}")