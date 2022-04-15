from inspect import stack
from pathlib import Path
import os

def GetExceptionString(prev_func_num=10):
    i=1
    func_list = []
    max_prev_func = len(stack())
    if prev_func_num > max_prev_func:
        prev_func_num == max_prev_func

    for i in range(1, prev_func_num):
        iExec = ""
        iExec = stack()[i]
        if iExec.function == "":
            break
        pfilename = Path(iExec.filename)
        filename = os.path.join(*pfilename.parts[-2:])
        iExecText = "{}:{}:{}".format(filename,iExec.function,iExec.lineno)
        func_list.append(iExecText)

    excText = ""

    for iText in reversed(func_list):
        excText = excText + " -> " + iText
        i = i + 1
    return excText