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

