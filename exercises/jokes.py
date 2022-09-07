import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

header = figlet_format("DAD JOKES")
header = colored(header, color = "magenta")
print(header)

usr_input = input("What would you like to search for?")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url, 
    headers = {"Accept": "application/json"},
    params ={"term":usr_input}
).json()

num_jokes = res["total_jokes"]
results = res["results"]
if num_jokes > 1:
    print(f"I found {num_jokes} jokes about {usr_input}. Here's one:")
    print(choice(results)["joke"])
elif num_jokes == 1:
    print(f"I found one joke about {usr_input}")
    print(results[0]['joke'])
else:
    print(f"Sorry, couldn't find a joke with your term: {usr_input}")