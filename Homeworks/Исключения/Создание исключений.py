class InvalidDataException(Exception):
    """Исключение для случая некорректных данных."""
    pass


class ProcessingException(Exception):
    """Исключение для ошибок при обработке данных."""
    pass


def process_data(data):
    if not isinstance(data, int):
        raise InvalidDataException("Data must be an integer.")
    if data < 0:
        raise ProcessingException("Data must be a positive integer.")
    return data * 2


def handle_data(data):
    try:
        result = process_data(data)
        return result
    except InvalidDataException as e:
        print(f"Ошибка: {e}")
        raise
    except ProcessingException as e:
        print(f"Внимание: {e}")
        raise


def main():
    test_data = ["string", -10, 5]

    for data in test_data:
        try:
            result = handle_data(data)
            print(f"Обработанный результат: {result}")
        except InvalidDataException as e:
            print(f"Обнаружено исключение: {e}")
        except ProcessingException as e:
            print(f"Обнаружено исключение: {e}")


if __name__ == "__main__":
    main()
