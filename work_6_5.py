print('Введите емейл:')
s = input()
if '@' in s and '.' in s:
    print('Корректный')
else:
    print('Некорректный')
