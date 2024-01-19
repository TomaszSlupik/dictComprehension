"""
Dict comprehension w Pythonie to wyrażenie, 
które umożliwia tworzenie nowego słownika na podstawie istniejących danych 
lub iteracji. Jest to sposób na generowanie słownika w jednej linii kodu.
"""

# utwórz słownik, który zmapuje liczby od 1 do 7 na ich kwadraty.
key_dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7}
key_dict_seocnd = {key: number ** 2  for key, number in key_dict.items()}
print(key_dict_seocnd)

print('---')

# zbuduj słownik, który zmapuje nazwy spółek na liczbę znaków w jej nazwie. 
stock_names = ['Playway', 'CD Projekt', 'Boombit']

stock_names_len = {values: len(values) for values in stock_names}
print(stock_names_len)

print('---')

# przestaw wartości słownika z kluczami
stock_codes = {'Boombit': '001', 'CD Projekt': '002', 'Playway': '003'}

change_stock_code  = {value: key for key, value in stock_codes.items()}

print(change_stock_code)

print('---')

# wyodrębnij ze słownika pary klucz-wartość o wartości powyżej 100.
stock_prices = {'Boombit': 22, 'CD Projekt': 295, 'Playway': 350}

highStocksPrices = {key: value for key, value in stock_prices.items() if value > 100}

print(highStocksPrices)

#  listę składającą się ze słowników mapujących 
# kolejne cyfry od 1 do 9 włącznie na ich odpowiednie 
# k-te potęgi, dla k = 1, 2, 3 

k1 = 1 
k2 = 2
k3 = 3
myNumber = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
myNumberList = []

myNumberFirst = {key: value ** k1 for key, value in myNumber.items()}
myNumberSecond = {key: value ** k2 for key, value in myNumber.items()}
myNumberThird = {key: value ** k3 for key, value in myNumber.items()}

myNumberList.append(myNumberFirst)
myNumberList.append(myNumberSecond)
myNumberList.append(myNumberThird)

print(myNumberList)

print('---')

# Ustaw wartość domyślną każdej właściwości na None.
stock_indices = ['WIG20', 'mWIG40', 'sWIG80']
properties = ['number of companies', 'companies', 'market capitalization']
properties_none = [None, None, None]

data_stock = {index: {prop: value for prop, value in zip(properties, properties_none)} for index in stock_indices}

print(data_stock)

print('---')

# przekształć listę indices w poniższy słownik:
# {0: 'WIG20', 1: 'mWIG40', 2: 'sWIG80'}

indices = ['WIG20', 'mWIG40', 'sWIG80']
indices_dict = {key: value for key, value in enumerate(indices)}
print(indices_dict)

print('---')

# Potrzebujesz utworzyć nowy słownik, zawierający tylko te produkty, 
# które są dostępne w magazynie i posortować je według ceny w kolejności rosnącej.
products = [
    {'id': 1, 'name': 'Keyboard', 'price': 100, 'in_stock': True},
    {'id': 2, 'name': 'Mouse', 'price': 50, 'in_stock': False},
    {'id': 3, 'name': 'Monitor', 'price': 200, 'in_stock': True},
    {'id': 4, 'name': 'Speakers', 'price': 75, 'in_stock': True},
    {'id': 5, 'name': 'Headphones', 'price': 90, 'in_stock': False},
]

products_available = sorted([myProduct for myProduct in products if myProduct['in_stock'] == True], key= lambda x: x['price'], reverse=False)
dictMyProduct = {}

for myProduct in products_available:
    dictMyProduct [myProduct['name']] = myProduct['price']

print(dictMyProduct)

print('---')

# nowy słownik, który będzie grupował loty według miejsc przylotu, a wartościami będą listy numerów lotów, które przylatują na dane miejsce.
flights = [
    {
        'flight_number': 'ABC123',
        'departure_time': '2023-04-12 08:00',
        'flight_time': 2,
        'departure_city': 'Kraków',
        'arrival_city': 'Warszawa',
    },
    {
        'flight_number': 'DEF456',
        'departure_time': '2023-04-12 10:00',
        'flight_time': 1,
        'departure_city': 'Gdańsk',
        'arrival_city': 'Warszawa',
    },
    {
        'flight_number': 'GHI789',
        'departure_time': '2023-04-12 14:00',
        'flight_time': 3,
        'departure_city': 'Warszawa',
        'arrival_city': 'Kraków',
    },
    {
        'flight_number': 'JKL012',
        'departure_time': '2023-04-12 12:00',
        'flight_time': 2,
        'departure_city': 'Warszawa',
        'arrival_city': 'Gdańsk',
    },
    {
        'flight_number': 'MNO345',
        'departure_time': '2023-04-12 16:00',
        'flight_time': 1,
        'departure_city': 'Kraków',
        'arrival_city': 'Gdańsk',
    },
]

flightGroupe = {}

for flight in flights:
    arrival_city = flight['arrival_city']
    flight_number = flight['flight_number']

    if arrival_city not in flightGroupe:
        flightGroupe[arrival_city] = []

    flightGroupe[arrival_city].append(flight_number)

print(flightGroupe)

print('---')

# grupowanie lotów według miejsc przylotu, a wartościami będą 
# listy lotów, które przylatują na dane miejsce, posortowane według godziny odlotu. 
import json
groupyByCity = {}

for flight in flights:
    city = flight['arrival_city']

    if city not in groupyByCity:
        groupyByCity[city] = []
    
    groupyByCity[city].append(flight)

json_result = json.dumps(groupyByCity, ensure_ascii=False, indent=2)
print(json_result)