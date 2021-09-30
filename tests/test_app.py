import unittest
from src.Try import Try
from src.Success import Success
from src.Failure import Failure

class Test(unittest.TestCase):

    def test_failure(self):
        errorstr = "Error!"
        res = Try(lambda: self.throwsException(RuntimeError(errorstr), True))
        
        self.assertIsInstance(res, Failure)
        self.assertIsInstance(res.error, RuntimeError)
        self.assertEqual(res.error.args[0], errorstr)
    

    def test_success(self):
        sucstr = "Success!"
        res = Try(lambda: self.throwsException(None, False))

        self.assertIsInstance(res, Success)
        self.assertIsInstance(res.val, str)
        self.assertEqual(res.val, sucstr)


    def test_failure_throws(self):
        res = Try(lambda: self.throwsException(RuntimeError, True))

        with self.assertRaises(RuntimeError):
            res.throw()


    def throwsException(self, exception: Exception, throw: bool):
        if throw:
            raise exception
        else:
            return "Success!"
