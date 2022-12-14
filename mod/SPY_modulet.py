print('This Module is a Simpl-Py Speed Testing Module')

def init(modin):
    if modin == 'inside':
        temp = 'This is inside the function.'
        return temp
    else:
        return 'not found'