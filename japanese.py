## Japanese.py a rudimentary translator.
import requests

def translate (word):
    pass

def req ():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    print(response.status_code)


def main():
    for i in range(0,10):
        req()

main()
