from random import choice as r_choice
from string import ascii_letters as s_ascii_letters
from string import digits as s_digits
from string import punctuation as s_punctuation

from django.template import Library as template_lib

register = template_lib()


@register.simple_tag
def randpass(plength: int, digits: bool, special: bool) -> str:

    # Characters
    c = s_ascii_letters

    if digits:
        c += s_digits

    if special:
        c += s_punctuation

    pw = ''

    for _ in range(int(plength)):
        pw += r_choice(c)

    return pw
