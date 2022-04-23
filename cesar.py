alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']


def code(text: str, liczba: int):
    for litera in text:
        for index, y in enumerate(alfabet):
            if y == litera.lower():
                suma = index + liczba
                if suma >= len(alfabet):
                    suma -= len(alfabet)
                print(alfabet[suma], end="")
                break
            elif litera == " ":
                print(" ", end="")
                break


def decode(text: str, liczba: int):
    for litera in text:
        for index, y in enumerate(alfabet):
            if y == litera.lower():
                suma = index - liczba
                if suma >= len(alfabet):
                    suma -= len(alfabet)
                print(alfabet[suma], end="")
                break
            elif litera == " ":
                print(" ", end="")
                break


code("sprawdzam poprawnosc kodu", 7)
print("")
decode("zwyhdkght wvwyhduvzj rvkb", 7)
