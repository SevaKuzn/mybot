def decorator(any_function):
    print('Это декоратор')
    def wrapper():
        print('Bызов функции...')
        any_function()
        print('Функция была успешно вызвана')
    return wrapper

@decorator

def normal_function():
    print('Это обычная функция')

normal_function()