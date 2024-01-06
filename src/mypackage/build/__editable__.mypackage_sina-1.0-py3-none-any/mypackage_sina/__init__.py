import os
import inspect

def read_file():
    caller = inspect.stack()[1].filename
    caller_name, caller_ext = os.path.basename(caller).split(".")
    caller_input_txt = f'{os.path.dirname(caller)}/{caller_name}.txt'

    return open(caller_input_txt, 'r')