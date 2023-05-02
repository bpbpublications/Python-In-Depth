
from functools import wraps 

def style(motif="+"):
    def style_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            new_result = [6*motif, result, 6*motif]
            return "\n".join(new_result)

        return wrapper
    return style_wrapper


@style(motif="*")
def my_code_doc(obj):
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
