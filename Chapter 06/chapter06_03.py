
from functools import wraps 

def style(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        new_result = ["++++++", result, "++++++"]
        return "\n".join(new_result)

    return wrapper

@style
def my_code_doc(obj):
    """ My own documentation extraction tool """
    typename = type(obj).__name__
    if typename == "type":
        title = obj.__name__
    else:
        title = f"{obj.__name__} ({typename})" 

    description = obj.__doc__
    if description.endswith("\n"):
        description = description[:-1]

    return f"{title}: {description}"


if __name__ == "__main__":

    print(my_code_doc(len))
    print()

    import os
    print(my_code_doc(os))
    print()

    from datetime import datetime
    print(my_code_doc(datetime))
