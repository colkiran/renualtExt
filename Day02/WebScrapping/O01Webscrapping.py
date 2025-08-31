
from bs4 import BeautifulSoup

with open("mypage.html", "r") as htmlfile:
    content = htmlfile.read()

    soup = BeautifulSoup(content, 'lxml')
    # print(soup)

    tag = soup.find("h5")
    print(tag)
    print(tag.text)

    print("-" * 60)
    crdTitle = soup.find_all("h5")
    print(crdTitle)

    print("-" * 60)
    for crd in crdTitle:
        print(crd.text)

    print("-" * 60)
    cards = soup.find_all("div", class_="card")
    for card in cards:
        crd_title = card.h5.text
        prc = card.a.text.split()[-1]

        print(f"Training on {crd_title} will cost {prc}")




