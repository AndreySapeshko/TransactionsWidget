from datetime import datetime
from functools import wraps


def log(filename: str = ''):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                start_time = datetime.now()
                result = func(*args, **kwargs)
                finish_time = datetime.now()
                message_log = f'{start_time} {finish_time} {func.__name__} ok. Result: {result}. Input: {args}, {kwargs}'
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
