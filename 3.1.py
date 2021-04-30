def div(arc_1, arc_2):
    try:
        arc_1, arc_2 = int(arc_1), int(arc_2)
        div_num = arc_1 / arc_2
    except ValueError:
        return 'ValueError'
    except ZeroDivisionError:
        return 'Делить на 0 незьзя!'
    return round(div_num, 4)

print(div(input('Введите первое число - '), input('Введите второе число - ')))