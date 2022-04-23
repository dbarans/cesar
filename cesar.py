alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']


def code(text: str, liczba: int):
    for litera in text:
        for index, y in enumerate(alfabet):
            if y == litera.lower():
                suma = index + liczba
                if suma >= 26:
                    suma -= 26

                print(alfabet[suma], end="")



def decode(text: str, liczba: int):
    for litera in text:
        for index, y in enumerate(alfabet):
            if y == litera.lower():
                suma = index - liczba
                if suma >= 26:
                    suma -= 26

                print(alfabet[suma], end="")

code("abcdef ghijkl", 20)
print("")
decode("uvwxyzabcdef", 20)

