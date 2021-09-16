import requests
from bs4 import BeautifulSoup
import webbrowser
while True:
    url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    soup = BeautifulSoup(url.content, "html.parser")
    title = soup.find(class_="firstHeading").text
    print(f"{title} \nDo you want to view it? (Y/N)")
    ans = input("").lower()
    if ans == "y":
        url = "https://en.wikipedia.org/wiki/%s" % title
        webbrowser.open(url)
        break
    elif ans == "n":
        sj = input('what do you want to view ? ')
        url_ = "https://en.wikipedia.org/wiki/%s" % sj
        webbrowser.open(url_)
        print('if you want to exit type Exit try again type anything.... ')
        end = input('> ') 
        if end == 'EXIT' or 'exit' or 'Exit':
            print('good bay')
        continue
    else:
        print("Wrong choice!")
        break


