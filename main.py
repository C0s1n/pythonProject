import requests
from bs4 import BeautifulSoup as bs


def write_txt(data, f_name='new_file.txt'):
    with open(r"C:\Users\189gl\PycharmProjects\pythonProject\new_file.txt", "a+") as file:
        file.write(data + '\n')
    file.close()
    return f_name


def search_info():
    count = 0
    while 1:
        name = input('\nВведите название криптовалюты, для выхода введите q:\n')
        if name == 'q':
            return
        for item in open('C:\\Users\\189gl\\PycharmProjects\\pythonProject\\new_file.txt'):
            data_fak = item.split()
            if data_fak[0].lower() == name.lower():
                print("рыночная капитализация:", data_fak[1])
                print("стоимость 1 ед. в долларах США:", data_fak[2])
                break
            count += 1


url = 'https://coinmarketcap.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.79 '
           }

r = requests.get(url, headers=headers)
soup = bs(r.text, 'lxml')
trs = soup.find('tbody').find_all('tr', limit=10)
name_f = []
price_f = []
market_cup_f = []
for tr in trs:
    quotes = tr.find_all('div', class_='sc-16r8icm-0 escjiH')
    names = tr.find_all('p', class_='sc-1eb5slv-0 iworPT')
    prices = tr.find_all('div', class_='sc-131di3y-0 cLgOOr')
    market_cups = tr.find_all('span', class_='sc-1ow4cwt-1 ieFnWP')
    for name in names:
        name_f.append(name.text)
    for price in prices:
        price_f.append(price.text)
    for market_cup in market_cups:
        market_cup_f.append(market_cup.text)
print(name_f)
for i in range(0, 10):
    print(name_f[i] + " " + price_f[i] + " " + market_cup_f[i])
    write_txt(name_f[i] + " " + price_f[i] + " " + market_cup_f[i])

if __name__ == "__main__":
    search_info()
