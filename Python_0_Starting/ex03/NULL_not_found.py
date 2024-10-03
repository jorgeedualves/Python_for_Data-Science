import inspect
import math

def NULL_not_found(object: any) -> int:
    frame = inspect.currentframe()
    try:
        caller_locals = frame.f_back.f_locals

        object = caller_locals.get(object, any)

        if object is None:
            print(f"Nothing: {object} <class '{type(object).__name__}'>")
        elif isinstance(object, float) and math.isnan(object):
            print(f"Cheese: {object} <class '{type(object).__name__}'>")
        elif object == 0:
            print(f"Zero: {object} <class '{type(object).__name__}'>")
        elif object == "":
            print(f"Empty: <class '{type(object).__name__}'>")
        elif object is False:
            print(f"Fake: {object} <class '{type(object).__name__}'>")
        else:
            print("Type not Found")
            return 1

        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1
    finally:
        del frame
