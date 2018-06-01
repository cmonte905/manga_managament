import unittest
from db import DB

database = DB()  # DB instance
class TestDBMethods(unittest.TestCase):


    def test_insert(self):
        database.add_new_entry('test', '1000', 'mangarock.com', 'finished')


if __name__=='__main__':
    unittest.main()
