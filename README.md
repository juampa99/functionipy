## Functionipy
FunctioniPy implements functional error handling as [seen](https://docs.scala-lang.org/overviews/scala-book/functional-error-handling.html#trysuccessfailure) in scala, using the Try/Success/Failure trio.

## How to use
The package provides three main structures: Try (function), Success (object) and Failure (object).

Try simulates a try-except block, but instead of raising the exception, it returns a Failure object that contains the exception. In case the passed function doesn't raises an exception, Try retuns a Success object containing the return value of the function.

Example failure:
```python
def raises_exception():
    raise RuntimeException("Example exception")

result = Try(lambda: raises_exception())

print(result.error)
```
```
>>> Example exception
>>> 
```



Example Failure:
```python
def doesnt_raise_exception():
    return "Hello World"

result = Try(lambda: doesnt_raise_exception())

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

## Extra functionality

### Failure.```throw```(*args):

Throws the captured exception, if args is passed, arguments of the original exception are overriden.
