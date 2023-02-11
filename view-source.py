import requests
URL = input("Enter the URL of the page you want to see the code for: ")
print("\n")
page = requests.get(URL)
print(page.text)
