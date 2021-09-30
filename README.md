## Functionipy
FunctioniPy implements functional error handling as [seen](https://docs.scala-lang.org/overviews/scala-book/functional-error-handling.html#trysuccessfailure) in scala, using the Try/Success/Failure trio.

## How to use
The package provides three main structures: Try (function), Success (object) and Failure (object).

Try simulates a try-except block, but instead of raising the exception, it returns a Failure object that contains the exception. In case the passed function doesn't raises an exception, Try retuns a Success object containing the return value of the function.

Example failure:
```python
def raises_exception(exc_message):
    raise RuntimeException(exc_message)

result = Try(lambda: raises_exception("Example exception"))

print(result.error)
```
```
>>> Example exception
>>> 
```



Example Failure:
```python
def doesnt_raise_exception(my_arg):
    return f"{my_arg} World"

result = Try(lambda: doesnt_raise_exception("Hello"))

print(result.val)
```
```
>>> Hello World
>>> 
```

Since ```Success``` and ```Failure``` are both objects, you can use pattern matching:

```python
if isinstance(result, Success):
    do_something()
elif isinstance(result, Failure):
    do_something_else()
```

On python 3.10+ you can use the new match/case keywords.

You can also use partial evaluation from the functools module instead of the less elegant lambdas:
```python
import functools

p_do_something = functools.partial(do_something, "Hello World")

res = Try(p_do_something)
...
```

## Extra functionality

### Failure.```throw```(*args):

Throws the captured exception, if args is passed, arguments of the original exception are overriden.
