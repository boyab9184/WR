import unittest
from pandas.testing import *

import assessment as ast


class TestAssessment(unittest.TestCase):

    def test_are_all_client_ids_unique(self):
        res = ast.are_all_client_ids_unique(ast.data_frame)
        self.assertTrue(res, True)

    def test_most_profitable_clients(self):
        res = ast.most_profitable_clients(ast.data_frame, 100)
        expected = ast.data_frame.sort_values(by=['Revenue'], ascending=False)['Client Id'].head(100)
        assert_series_equal(res, expected)

    def test_half_with_most_transactions_by_sessions(self):
        res = ast.half_with_most_transactions_by_sessions(ast.data_frame)
        self.assertTrue(res, 'LONGER' in res)

    def test_revenue_with_less_than_num_sessions(self):
        res = ast.revenue_with_less_than_num_sesions(ast.data_frame, 100)
        self.assertEqual(res, 3586894.02)

    def test_revenue_with_most_transaction_limited(self):
        res = ast.revenue_with_most_transaction_limited(ast.data_frame, 100)
        self.assertEqual(res, 278576.01)

    def test_average_session_duration(self):
        res = ast.avarage_session_duration(ast.data_frame, 100)
        self.assertEqual(str(res), '0:06:59.940057')


if __name__ == '__main__':
    unittest.main()
