# project/test_basic.py

import requests
import unittest
import pytest

TEST_DB = 'test.db'
TEST_URL = 'http://localhost:5000'
CREATE_REMINDER_RESOURCE = '/create_reminder'


class CreateReminderTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_reminder_success(self):
        test_payload = {
            "reminder": "look, a test reminder!",
            "completed": "False"
        }
        successful_request = requests.post(
            TEST_URL + CREATE_REMINDER_RESOURCE,
            data=test_payload
        )
        self.assertEqual(
            successful_request.status_code,
            201,
            "Checking Response == 201 on successful creation..."
        )


if __name__ == "__main__":
    unittest.main()
