from django.template import Library as template_Lib

register = template_Lib()

# Cube a number
@register.filter(name='cube')
def cube(value: int) -> int:
    try:
        return value ** 3
    except TypeError as e:
        print(f'Error!:\n{e}')

# First letter
@register.filter(name='first_letter')
def first_letter(value: str) -> str:
    return value[0]

# Slicing
@register.filter(name='slicer')
def slicer(value: str, intrvl: str) -> str:    
    intrvl = intrvl.split(',')
    start = intrvl[0]
    end = intrvl[1]
    return value[int(start):int(end)]
