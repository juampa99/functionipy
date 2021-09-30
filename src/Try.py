from src.Failure import Failure
from src.Success import Success

def Try(func):
    try:
        return Success(func())
    except Exception as e:
        return Failure(e)