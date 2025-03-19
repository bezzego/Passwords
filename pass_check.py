def has_digit(pwd):
    return any(char.isdigit() for char in pwd)


def has_upper_letters(pwd):
    return any(char.isupper() for char in pwd)


def has_lower_letters(pwd):
    return any(char.islower() for char in pwd)


def is_very_long(pwd):
    return len(pwd) >= 12


def has_symbols(pwd):
    return any(not char.isalnum() for char in pwd)


checks = [
    has_digit,
    has_upper_letters,
    has_lower_letters,
    is_very_long,
    has_symbols
]


def balls_add_score(pwd):
    return sum(2 for check in checks if check(pwd))


def main():
    password = input('Введите пароль: ')
    score = balls_add_score(password)
    print(f'Введенный вами пароль: {password}')
    print(f'Рейтинг пароля: {score}')


if __name__ == '__main__':
    main()
