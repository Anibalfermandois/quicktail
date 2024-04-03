from pprint import pprint
from typing import Any,Callable

class TailOp:
    """
    A class representing an End-of-Line operator for quick and easy operations at the end of a line.
    
    Attributes:
        f (Callable): The function or callable to be executed with | operator.
        f_args (tuple): The arguments to be passed to the function.
        f_kwargs (dict): The keyword arguments to be passed to the function.
    """

    def __init__(self, f, *args: Any, **kwargs: Any):
        self.f: Callable = f
        self.f_args = args
        self.f_kwargs = kwargs

    def __or__(self, other):
        """
        Defines the behavior of the | operator with TailOp objects.
        Executes self.f
        """
        try:
            return self.f(other, *self.f_args, **self.f_kwargs)
        except TypeError:
            print("TailOp Error")
            return other

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """
        Allows the TailOp to be called with arguments.
        tailprint(width=3)
        """
        self.f_args = args
        self.f_kwargs = kwargs
        return self
    
tailprint = TailOp(pprint)

