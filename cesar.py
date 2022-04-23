alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']


def code(text: str, liczba: int):
    kod = ""
    for litera in text:

        for index, y in enumerate(alfabet):
            if y == litera.lower():
                suma = index + liczba
                if suma >= len(alfabet):
                    suma -= len(alfabet)
                kod += alfabet[suma]

                break
            elif litera == " ":
                kod += " "

                break

    return kod


def decode(text: str, liczba: int):
    kod = ""
    for litera in text:

        for index, y in enumerate(alfabet):
            if y == litera.lower():
                suma = index - liczba
                if suma >= len(alfabet):
                    suma -= len(alfabet)
                kod += alfabet[suma]

                break
            elif litera == " ":
                kod += " "

                break

    return kod


assert code("abcd", 2) == "cdef"
assert decode("cdef", 2) == "abcd"

print(code("sprawdzam poprawnosc kodu", 7))
print(decode("zwyhdkght wvwyhduvzj rvkb", 7))
