from logic import postfix_to_instructions


def print_menu():
    print()
    print("ПРЕОБРАЗОВАТЕЛЬ ПОСТФИКСНЫХ ВЫРАЖЕНИЙ")
    print()
    print("1. Ввести выражение")
    print("2. Показать пример")
    print("0. Выход")


def convert_expression():

    expression = input(
        "\nВведите постфиксное выражение: "
    ).strip()

    try:
        instructions = postfix_to_instructions(
            expression
        )

        print("\nИнструкции:\n")

        for command in instructions:
            print(command)

    except ValueError as error:
        print(f"\nОшибка: {error}")


def show_example():

    example = "ABC*+DE-/"

    print("\nВыражение:")
    print(example)

    try:
        instructions = postfix_to_instructions(
            example
        )

        print("\nИнструкции:\n")

        for command in instructions:
            print(command)

    except ValueError as error:
        print(error)


def main():

    while True:

        print_menu()

        choice = input(
            "\nВыберите пункт меню: "
        ).strip()

        if choice == "1":
            convert_expression()

        elif choice == "2":
            show_example()

        elif choice == "0":
            print("\nПрограмма завершена.")
            break

        else:
            print(
                "\nОшибка: выберите пункт от 0 до 2."
            )


if __name__ == "__main__":
    main()