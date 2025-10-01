def detect_language(text):
    ru_chars = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    en_chars = "abcdefghijklmnopqrstuvwxyz"

    ru_count = sum(1 for char in text.lower() if char in ru_chars)
    en_count = sum(1 for char in text.lower() if char in en_chars)

    if ru_count > en_count:
        return 'ru'
    elif en_count > ru_count:
        return 'en'
    else:
        return 'en'

def get_alphabet(language):
    if language == 'ru':
        return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    else:
        return 'abcdefghijklmnopqrstuvwxyz'


def caesar_cipher(text, shift, operation):
    language = detect_language(text)
    alphabet = get_alphabet(language)
    result = []

    for char in text:
        if char.lower() not in alphabet:
            result.append(char)
            continue

        is_upper = char.isupper()
        char_lower = char.lower()

        char_index = alphabet.index(char_lower)

        if operation == 'encrypt':
            new_index = (char_index + shift) % len(alphabet)
        else:
            new_index = (char_index - shift) % len(alphabet)

        new_char = alphabet[new_index]

        if is_upper:
            new_char = new_char.upper()

        result.append(new_char)

    return ''.join(result)

print("=== Шифр Цезаря ===")
print("1. Зашифровать текст")
print("2. Расшифровать текст")

choice = input("Выберите операцию (1 или 2): ")

if choice not in ['1', '2']:
    print("Неверный выбор!")
else:
    text = input("Введите текст: ")
    shift = int(input("Введите ключ (сдвиг): "))

    if choice == '1':
        result = caesar_cipher(text, shift, 'encrypt')
        print(f"\nЗашифрованный текст: {result}")
    else:
        result = caesar_cipher(text, shift, 'decrypt')
        print(f"\nРасшифрованный текст: {result}")