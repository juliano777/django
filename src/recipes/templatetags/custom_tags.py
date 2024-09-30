from django.template import Library as template_lib

register = template_lib()


@register.simple_tag
def ul(value: str, n_items: int) -> str:
    s = '<ul>'
    for i in range(n_items):
        s = f'{s}\n    <li><b>{value.lower()}</b> {i + 1}</li>'

    return f'{s}\n</ul>'
