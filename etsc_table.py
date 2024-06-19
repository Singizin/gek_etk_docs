def ECTS(point, mode):
    if mode == 1:
        points = [100, 97, 92, 89, 86, 82, 79, 76, 72, 69, 66, 62, 59, 49, 24];
        chars = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E', 'FX', 'F'];
        for i in range(len(points)):
            if (point > points[i] and point <= points[i - 1]):
                return chars[i - 1]
            if point <= points[-1]:
                return chars[-1]

    if mode == 2:
        points = [100, 86, 72, 49, 0];
        chars = ['Отлично', 'Хорошо', 'Удовлетворительно', 'неуд'];
        for i in range(len(points)):
            if (point > points[i] and point <= points[i - 1]):
                return chars[i - 1]
    if mode == 3:
        points = [100, 49, 0]
        chars = ['зачтено', 'незачтено']
        for i in range(len(points)):
            if (point > points[i] and point <= points[i - 1]):
                return chars[i - 1]
    if mode == 4:
        points = [100, 86, 72, 49, 0]
        chars = [5, 4, 3, 2]
        for i in range(len(points)):
            if (point > points[i] and point <= points[i - 1]):
                return chars[i - 1]


def ending(score):
    n = score
    if n in (11, 12, 13, 14):
        return (f'{n} баллов')
    elif n % 10 == 1:
        return (f'{n} балл')
    elif n % 10 in (2, 3, 4):
        return (f'{n} балла')
    else:
        return (f'{n} баллов')


def text_format(score):
    rus = ECTS(score, 2)
    letter = ECTS(score, 1)

    return f'{rus} ({ending(score)}, {letter})'


for i in range(0, 101):
    print(text_format(i))