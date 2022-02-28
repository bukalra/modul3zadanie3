'''
Twojemu szefowi udało się znaleźć informacje o najlepiej sprzedających się modelach samochodów w 2018 roku. Dane, które zdobył nie nadają się niestety do analizy, dlatego poprosił Cię o przetworzenie, aby można było z nich w prosty sposób wyciągać informacje.

Do zmiennej `models` przypisano listę zawierającą najlepiej sprzedające się samochody 2018 roku uszeregowane od najlepiej sprzedającego się w formacie 'producent - model'.

Do zmiennych `sales2018`, `sales2017` oraz `sales2016` przypisano liczbę sprzedanych egzemplarzy tych modeli kolejno w roku 2018, 2017 oraz 2016.

Czyli - najlepiej sprzedającym się modelem samochodu w 2018 roku był: Volkswagen Golf (pierwsza pozycja na liście `models`). Golf w 2018 roku sprzedał się w ilości 445 754 egzemplarzy (pierwsza pozycja na liście `sales2018`). Wiemy też, że w 2017 roku sprzedano 483 105 modeli Golfa (pierwsza pozycja na liście `sales2017`), oraz że w 2016 roku sprzedano 492 952 egzemplarzy Golfa (pierwsza pozycja na liście `sales2016`).

Niektóre samochody nie były sprzedawane przed 2018 rokiem. W takim przypadku dane o ich sprzedaży zastąpione są wartością 'NA'. Zastąp wszystkie 'NA' cyfrą 0.

Na podstawie otrzymanych danych zbuduj słownik o następującej strukturze i **przypisz go do zmiennej `cars`**:

```
cars = {"brand": {"model1":{"sales":{"2016": 123,
```

```
                                     "2017": 456,
```

```
                                     "2018": 789}},
```

```
                  "model2":{"sales":{"2016": 987,
```

```
                                     "2017": 654,
```

```
                                     "2018": 321}}
```

```
                 },
```

```
        "brand2": ... }
```

Czyli na przykładzie rzeczywistych danych powinien wyglądać on następująco:

```
cars = {"Opel": {"Corsa":{"sales":{"2016": 264844,
```

```
                                   "2017": 232738,
```

```
                                   "2018": 217036}},
```

```
                 "Astra":{"sales":{"2016": 253483,
```

```
                                   "2017": 217813,
```

```
                                   "2018": 160275}}
```

```
                 },
```

```
        "Dacia": ... }
```

Następnie postaraj się odpowiedzieć na pytania zaprezentowane poniżej:

1. Który model samochodu z listy najlepiej sprzedawał się w 2017 roku? Odpowiedź przypisz do zmiennej `answer1`.
2. Który producent z listy sprzedał najwięcej egzemplarzy samochodów w 2018 roku? Odpowiedź przypisz do zmiennej `answer2`.
3. Ile modeli samochodów z listy nie sprzedawało się w 2016 roku, a do sprzedaży weszło w roku 2017? Odpowiedź przypisz do zmiennej `answer3`.
4. Który z model samochodu z listy ma najmniej sprzedanych egzemplarzy, jeśli weźmiemy pod uwagę lata 2016, 2017 oraz 2018. Odpowiedź przypisz do zmiennej `answer4`.
5. O ile procent wzrosła sprzedaż modeli Forda w 2018 roku w stosunku do roku 2017? Odpowiedź przypisz do zmiennej `answer5`. Odpowiedź podaj w formacie procentowym jako string. Np. '21%'.

# UWAGA! Na potrzeby zadania potraktuj 'VW' i 'Volkswagen' jako osobnych producentów
'''