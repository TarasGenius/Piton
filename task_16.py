import requests
from bs4 import BeautifulSoup as Bs
from datetime import datetime


class Bankomat():
    def set(self, balans, sysbalans):
        with open('balans.txt', 'w', encoding='utf-8') as balans_file:
            balans_file.write(str(balans))
        with open('system balans.txt', 'w', encoding='utf-8') as balans_file:
            balans_file.write(str(sysbalans))

    def get(self):
        with open('balans.txt', 'r', encoding='utf-8') as balans_file:
            balans = balans_file.readline()
        with open('system balans.txt', 'r', encoding='utf-8') as balans_file:
            sysbalans = balans_file.readline()
        return int(balans), int(sysbalans)

    def log(self, arg):
        with open('log.txt', 'w', encoding='utf-8') as log:
            now = datetime.now()
            log.write(f'{now.strftime("%Y-%m-%d %H:%M:%S")}: {arg}\n')

    def currency_rate(self):
        url = 'https://www.oschadbank.ua/currency-rate'
        response = requests.get(url)
        html = Bs(response.content, 'html.parser')
        lst = []
        for i in html.select('.heading-block-currency-rate__table-row'):
            a = i.select('.heading-block-currency-rate__table-col')
            for n in a:
                b = n.findAll('span', class_='heading-block-currency-rate__table-txt body-regular')[0].text  # 5 4 3
                lst.append(b)
        del lst[0:6]
        del lst[18:-1]
        del lst[-1]
        for i in range(3):
            lst.remove('1')
        return lst


class Dother(Bankomat):
    def __init__(self, pin, balans):
        self.__pin = pin
        self.__balans = balans
        with open('balans.txt', 'w', encoding='utf-8') as balans_file:
            balans_file.write(str(balans))
        self.what()

    @staticmethod
    def valid(pin):
        n = 0
        while n != 3:
            if pin == 1234:
                return int(pin)
            else:
                n += 1
                print('incorrect pin')
        else:
            print('card is blocked')

    def what(self):
        answer = input('What do you want to do?\nWithdraw - 1\nReplenichment - 2\nCheck currency rate - 3\n'
                       'Convert money - 4\n')
        if answer == '1':
            self.withdraw_money()
        elif answer == '2':
            self.replenishment()
        elif answer == '3':
            self.request_currency_rate()
        elif answer == '4':
            self.converting()

    def withdraw_money(self):
        how_many = int(input('How many do you wand withdraw: '))
        balans, sysbalans = self.get()
        if how_many <= balans and how_many <= sysbalans:
            balans -= how_many
            sysbalans -= how_many
            self.set(balans, sysbalans)
            self.log('Withdraw')
        else:
            print('insufficient funds')
            self.log('Withdraw - insufficient funds')

    def replenishment(self):
        how_many = int(input('How many do you wand replenishment: '))
        balans, sysbalans = self.get()
        balans += how_many
        sysbalans += how_many
        self.set(balans, sysbalans)
        self.log('Replenishment')

    def request_currency_rate(self):
        a = self.currency_rate()
        print(f'Rate: {a}')
        self.log('Request current rate')

    def converting(self):
        how_many = int(input('How many do you wand convert: '))
        currency = input('What currency:(USD/EUR/GBP): ')
        balans, sysbalans = self.get()
        balans -= how_many
        sysbalans -= how_many
        self.set(balans, sysbalans)
        lst = self.currency_rate()
        self.log('Converting')
        if currency == 'USD':
            with open('balansUSD.txt', 'w', encoding='utf-8') as balans_file:
                result = float(how_many / float(lst[3]))
                balans_file.write(str(result))
        elif currency == 'EUR':
            with open('balansEUR.txt', 'w', encoding='utf-8') as balans_file:
                result = float(how_many / float(lst[8]))
                balans_file.write(str(result))
        elif currency == 'GBT':
            with open('balansGBT.txt', 'w', encoding='utf-8') as balans_file:
                result = float(how_many / float(lst[-2]))
                balans_file.write(str(result))


obj = Dother(Dother.valid(1234), 120000)
print(obj.__dict__)