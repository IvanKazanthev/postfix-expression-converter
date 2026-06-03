class Node:
    """Узел односвязного списка."""

    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """Стек на основе односвязного списка."""

    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.top is None:
            raise ValueError("Стек пуст.")

        value = self.top.data
        self.top = self.top.next
        self._size -= 1

        return value

    def size(self):
        return self._size


def is_operand(symbol):
    return symbol.isupper() and symbol.isascii()


def postfix_to_instructions(expression):
    """Преобразование постфиксного выражения в набор инструкций."""

    if not expression:
        raise ValueError("Пустое выражение.")

    stack = Stack()
    instructions = []

    operations = {
        "+": "AD",
        "-": "SB",
        "*": "ML",
        "/": "DV"
    }

    temp_counter = 1

    for symbol in expression:
        if not (is_operand(symbol) or symbol in operations):
            raise ValueError(
                "Разрешены только заглавные "
                "латинские буквы A-Z и операции + - * /"
            )

    for i, symbol in enumerate(expression):

        if is_operand(symbol):
            stack.push(symbol)

        elif symbol in operations:

            if stack.size() < 2:
                raise ValueError(
                    "Некорректное постфиксное выражение: "
                    "недостаточно операндов для выполнения операции."
                )

            right = stack.pop()
            left = stack.pop()

            instructions.append(f"LD {left}")
            instructions.append(
                f"{operations[symbol]} {right}"
            )

            # Переиспользуем уже существующую
            # временную переменную результата.
            if left.startswith("T"):
                result_name = left

            elif right.startswith("T"):
                result_name = right

            else:
                result_name = f"T{temp_counter}"
                temp_counter += 1

            # Промежуточный результат сохраняется,
            # если впереди ещё есть операции.
            remaining_operations = sum(
                1
                for ch in expression[i + 1:]
                if ch in operations
            )

            if remaining_operations > 0:
                instructions.append(
                    f"ST {result_name}"
                )

            stack.push(result_name)

    if stack.size() > 1:
        raise ValueError(
            "Некорректное постфиксное выражение: "
            "операндов больше, чем операций."
        )

    if stack.size() == 0:
        raise ValueError(
            "Некорректное постфиксное выражение."
        )

    if len(instructions) == 0:
        operand = stack.pop()
        return [f"LD {operand}"]

    return instructions