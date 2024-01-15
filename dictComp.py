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
