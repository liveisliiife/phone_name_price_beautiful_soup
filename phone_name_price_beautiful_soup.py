import requests
from bs4 import BeautifulSoup

for sayfa in range(1,13):
    url = "https://www.vatanbilgisayar.com/cep-telefonu-modelleri/?page={}".format(sayfa)
    html = requests.get(url).content
    soup = BeautifulSoup(html,"html.parser")

    veri = soup.find("div",{"class":"wrapper-product wrapper-product--list-page clearfix"}).find_all("div",{"class":"product-list product-list--list-page"})

    print("\n\n")
    print("   Sayfa Numarası {}   ".format(sayfa).center(49, "*"),"\n")

    for current in veri:
        name = current.find("div",{"class":"product-list__content"}).find("a",{"class":"product-list__link"}).find("div",{"class":"product-list__product-name"}).find("h3").string
        price = current.find("div", {"class": "product-list__content"}).find("div", {"class": "product-list__cost"}).find("span",{"class":"product-list__price"}).string
        print(name.ljust(65),price)




