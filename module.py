import pprint
from typing import Any

class Postfix:

    def __init__(self, f,*args: Any, **kwargs: Any):
        self.f = f
        self.f_args=args
        self.f_kwargs=kwargs

    def __ror__(self, other):
        return self.f(other,*self.f_args,**self.f_kwargs)
        # try:
        #     return self.f(other,*self.f_args,**self.f_kwargs)
        # except TypeError:
        #     return self.f(other)

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        self.f_args=args
        self.f_kwargs=kwargs
        return self
    
printEoL = Postfix(pprint.pprint)