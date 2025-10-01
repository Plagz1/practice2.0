import random
import string

def generate_password(length=8, use_lower=True, use_upper=True, use_digits=True, use_special=True):

    characters = ""

    if use_lower:
        characters += string.ascii_lowercase  # abcdefghijklmnopqrstuvwxyz
    if use_upper:
        characters += string.ascii_uppercase  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    if use_digits:
        characters += string.digits  # 0123456789
    if use_special:
        characters += "!@#$%&*_"
    if characters == "":
        characters = string.ascii_letters + string.digits + "!@#$%&*_"

    password = ""
    for i in range(length):
        password += random.choice(characters)

    return password

def main():

    print("=== ГЕНЕРАТОР ПАРОЛЕЙ ===")
    print()

    try:
        length = int(input("Длина пароля (рекомендуется 8-12): ") or "8")
    except:
        length = 8

    print("\nКакие символы использовать?")
    use_lower = input("Строчные буквы (a-z)? (да/нет) [да]: ").lower() != "нет"
    use_upper = input("Заглавные буквы (A-Z)? (да/нет) [да]: ").lower() != "нет"
    use_digits = input("Цифры (0-9)? (да/нет) [да]: ").lower() != "нет"
    use_special = input("Спецсимволы (!@#$_)? (да/нет) [да]: ").lower() != "нет"

    password = generate_password(
        length=length,
        use_lower=use_lower,
        use_upper=use_upper,
        use_digits=use_digits,
        use_special=use_special
    )

    print("\n" + "=" * 30)
    print("Ваш пароль:", password)
    print("=" * 30)


if __name__ == "__main__":
    main()