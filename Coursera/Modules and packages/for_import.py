from vars import *

# print(vars.x + vars.y)
print(multi(4, 5))  # note that vars.multi won't work (instead needed to import vars, but otherwise __all__ attribute won't work)
# print(div(4, 5))  # to being able to work add the div in __all__ in vars module
