import unittest
from index import client, table, Table_Name

class TestResources(unittest.TestCase):

    def test_client(self):
        self.assertIsNotNone(client)

    def test_table(self):
        self.assertIsNotNone(table)
        self.assertEqual(Table_Name, 'visitor-count-table')

if __name__ == '__main__':
    unittest.main()