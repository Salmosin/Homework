import time


def log(message, filename='log.txt'):
    with open(filename, 'a') as log_file:
        log_file.write(message + '\n')


def search_recursive(func, interval, epsilon=1e-5, log_file='log.txt'):
    a, b = interval
    f_a = func(a)
    f_b = func(b)

    log(f'Starting Recursive for [{a}, {b}]', log_file)

    if f_a * f_b > 0 :
        log('No root found. ', log_file)
        return None

    start_time = time.time()

    def recursive(a, b):
        nonlocal start_time
        mid = (a + b) / 2
        f_mid = func(mid)

        log(f'check mid: {mid}, f(mid): {f_mid}, time: {time.time() - start_time:.6f}s', log_file)

        if abs(f_mid) < epsilon:                #проверяем найдено ли решение
            return mid
        elif f_a * f_mid < 0:
            return recursive(a, mid)     #возвращаем рекурсивную функцию сдвигаем правую границу
        else:
            return recursive(mid, b)     #возвращаем рекурсивную функцию сдвигаем левую границу

    return recursive(a, b)


def search_iterative(func, interval, epsilon=1e-5, log_file='log.txt'):
    a, b = interval
    f_a = func(a)
    f_b = func(b)

    log(f'Starting Iterative for [{a}, {b}]', log_file)

    if f_a * f_b > 0 :
        log('No roots found ', log_file)
        return None

    start_time = time.time()

    while True:
        mid = (a + b) / 2
        f_mid = func(mid)

        log(f'checking mid: {mid}, f(mid): {f_mid}, time : {time.time() - start_time:.6f}s', log_file)

        if abs(f_mid) < epsilon:
            return mid
        elif f_a * f_mid < 0:
            b = mid
            f_b = f_mid
        else:
            a = mid
            f_a = f_mid


# Пример использования
if __name__ == '__main__':
    def example_function(x):
        return x**5-x**4 +156 - 245*x + 7*x**2 # Пример функции, корень которой мы ищем


    interval = [-40 , 40]

    # Рекурсивный метод
    start_recursive = time.time()
    root_recursive = search_recursive(example_function, interval)
    print(f'Root  (recursive): {root_recursive}, Time : {time.time() - start_recursive:.6f}s')

    # Итеративныей метод
    start_iterative = time.time()
    root_iterative = search_iterative(example_function, interval)
    print(f'Root (iterative): {root_iterative}, Time : {time.time() - start_iterative:.6f}s')