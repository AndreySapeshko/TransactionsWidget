from datetime import datetime
from functools import wraps
from typing import Any, Callable, TypeVar

T = TypeVar('T')


def log(filename: str = '') -> Callable[[Callable[..., T]], Callable[..., bool]]:
    """ декоратор логирует разультаты работы функции и входные параметры
        если передано имя и адрес файла, пишет в файл, если нет, в консоль """

    def decorator(func: Callable[..., T]) -> Callable[..., bool]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> bool:
            try:
                start_time = datetime.now()
                result = func(*args, **kwargs)
                finish_time = datetime.now()
                message_log = (f'{start_time} {finish_time} {func.__name__} ok. '
                               f'Result: {result}. Input: {args}, {kwargs}')
            except Exception as e:
                finish_time = datetime.now()
                message_log = f'{start_time} {finish_time} erorr: {e.__context__}. Input: {args}, {kwargs}'
            finally:
                if filename == '':
                    print(message_log)
                else:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(message_log + '\n')
            return True
        return wrapper
    return decorator
