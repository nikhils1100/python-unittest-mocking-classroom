from unittest import TestCase
from unittest.mock import patch
from unittest import mock
from src.db_helper import DbHelper

class TestDbHelper(TestCase):
    def setUp(self):
        self.db_helper = DbHelper()

    @patch('src.db_helper.DbHelper')
    def test_max_salary_is_greater_than_min_salary(self, Mock_db_helper):
        db_helper = Mock_db_helper()

        db_helper.get_maximum_salary.return_value = 100

        db_helper.get_minimum_salary.return_value = 0

        self.assertGreater(db_helper.get_maximum_salary(), db_helper.get_minimum_salary())