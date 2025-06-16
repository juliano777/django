from typing import Any


def type_cast(value: str, type_: Any, default: str) -> Any:
    '''
    Convert any value to any type.
    If this is not possible a default value will assume.
    '''
    try:
        if value is not None:
            return type_(value)
        else:
            return type_(default)

    except (ValueError, TypeError):
        return type_(default)
