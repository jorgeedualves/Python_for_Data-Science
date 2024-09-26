import inspect

def NULL_not_found(object: any) -> int:

    # Get the current frame and the caller's local variables
    frame = inspect.currentframe()
    try:
        caller_locals = frame.f_back.f_locals
        # Find the variable name that matches the value
        var_name = [name for name, value in caller_locals.items() 
                    if value is object and not name.startswith("__")]
        
        if (not var_name):
            print('Type not Found')
        else:
            response = var_name[0] + ":"
            print(response, object, type(object))
    finally:
        del frame  # Clean up to avoid reference cycles
    
    return 1
