import random

UKRAINIAN_ALPHABET = 'АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЬьЮюЯя0123456789, .!?:;-\"\'()[]{}<>'


def caesar_cipher(message, shift):
    encrypted_message = ""
    for char in message:
        if char in UKRAINIAN_ALPHABET:
            char_index = UKRAINIAN_ALPHABET.index(char)
            shifted_index = (char_index + shift) % len(UKRAINIAN_ALPHABET)
            encrypted_char = UKRAINIAN_ALPHABET[shifted_index]
            encrypted_message += encrypted_char
        else:
            print("Ошибка: символ", char, "не принадлежит украинскому алфавиту или цифрам")
            return

    return encrypted_message


def caesar_decipher(message, shift):
    decrypted_message = ""

    for char in message:
        if char in UKRAINIAN_ALPHABET:
            char_index = UKRAINIAN_ALPHABET.index(char)
            shifted_index = (char_index - shift) % len(UKRAINIAN_ALPHABET)
            decrypted_char = UKRAINIAN_ALPHABET[shifted_index]
            decrypted_message += decrypted_char
        else:
            print("Ошибка: символ", char, "не принадлежит украинскому алфавиту или цифрам")
            return

    return decrypted_message

# Получение выбора от пользователя
choice = input("Выберите операцию (1 - шифрование, 2 - расшифровка): ")

if choice == "1":
    message = input("Введите сообщение на украинском языке: ")
    shift = random.randint(1, 30)
    encrypted_message = caesar_cipher(message, shift)
    if encrypted_message:
        print("Зашифрованное сообщение:", encrypted_message)
        print("Номер шифра Цезаря:", shift)
elif choice == "2":
    message = input("Введите зашифрованное сообщение: ")
    shift = int(input("Введите номер шифра Цезаря: "))
    decrypted_message = caesar_decipher(message, shift)
    if decrypted_message:
        print("Расшифрованное сообщение:", decrypted_message)
else:
    print("Ошибка: некорректный выбор операции. Пожалуйста, введите 1 для шифрования или 2 для расшифровки.")

