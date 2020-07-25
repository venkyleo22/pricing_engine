import unittest
from models import wheel, handle, chain, seating, frame, cycle


class Testframe(unittest.TestCase):
    def test_fun1(self):
        f = frame(2,25,5,50)
        result = f.price()
        assert result==200, "failed to calculate price" 


if __name__ == "__main__":
    unittest.main()
