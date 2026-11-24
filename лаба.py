UA = "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ"
EN = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar(text, shift, alphabet=UA):
    result = ""
    for symbol in text.upper():
        if symbol in alphabet:
            position = alphabet.index(symbol)
            result += alphabet[(position + shift) % len(alphabet)]
        else:
            result += symbol
    return result


def columnar_transposition(text, key):
    text = text.upper().replace(" ", "_")
    key = key.upper()
    if not key:
        raise ValueError("Ключове слово не може бути порожнім")

    width = len(key)
    while len(text) % width != 0:
        text += "_"

    rows = []
    for i in range(0, len(text), width):
        rows.append(text[i:i + width])

    def alphabet_order(index):
        letter = key[index]
        if letter in UA:
            return (0, UA.index(letter), index)
        return (1, letter, index)

    order = sorted(range(width), key=alphabet_order)
    result = ""
    for index in order:
        for row in rows:
            result += row[index]
    return result


def brute_force_caesar(text, alphabet=EN):
    for key in range(1, len(alphabet)):
        print(f"k={key:2}: {caesar(text, -key, alphabet)}")


def main():
    while True:
        print("\n1 - Шифрування Цезаря (український алфавіт)")
        print("2 - Розшифрування Цезаря (український алфавіт)")
        print("3 - Стовпчикова транспозиція")
        print("4 - Злом Цезаря повним перебором (англійський алфавіт)")
        print("5 - Перевірити приклади лабораторної")
        print("0 - Вихід")
        choice = input("Ваш вибір: ").strip()

        if choice == "0":
            break
        elif choice in ("1", "2"):
            text = input("Введіть текст: ")
            try:
                shift = int(input("Введіть зсув k: "))
            except ValueError:
                print("Помилка: зсув має бути цілим числом")
                continue
            if choice == "2":
                shift = -shift
            print("Результат:", caesar(text, shift))
        elif choice == "3":
            text = input("Введіть текст: ")
            key = input("Введіть ключове слово: ")
            try:
                print("Результат:", columnar_transposition(text, key))
            except ValueError as error:
                print("Помилка:", error)
        elif choice == "4":
            text = input("Введіть шифротекст: ")
            brute_force_caesar(text)
        elif choice == "5":
            print("1:", caesar("ЗАХИСТ ІНФОРМАЦІЇ 2026", 7))
            print("2:", columnar_transposition("БЕЗПЕКА МЕРЕЖІ", "КРИПТО"))
            print("3а: k=3")
            print("3б:", caesar("KHOOR ZRUOG", -3, EN))
        else:
            print("Такого пункту меню немає")


if __name__ == "__main__":
    main()
