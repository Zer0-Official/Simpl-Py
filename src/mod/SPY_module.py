print('This is a Simpl-Py Example Module')


def init(modin):
    if modin == 'inside':
        temp = 'This is inside the function.'
        return temp
    elif modin == 'test':
        temp = 'example ' * 24
        return temp
    else:
        return 'Not found.'
