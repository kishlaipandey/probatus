import unittest
from probatus import verifier
from colorama import Fore, Style

class TestVerifyResponses(unittest.TestCase):
    def setUp(self):
        self.test_results = [
            {'name': 'Test 1', 'response': {'key': 'value'}, 'status_code': 200},
            {'name': 'Test 2', 'response': {'key': 'wrong'}, 'status_code': 404}
        ]
        self.expected_results = [
            {'response_body': {'key': 'value'}, 'status_code': 200},
            {'response_body': {'key': 'value'}, 'status_code': 200}
        ]

    def test_verification_success(self):
        verified = verifier.verify_responses([self.test_results[0]], [self.expected_results[0]])
        self.assertTrue(verified[0]['passed'])
        self.assertIn('PASS', verified[0]['message'])

    def test_verification_failure(self):
        verified = verifier.verify_responses([self.test_results[1]], [self.expected_results[1]])
        self.assertFalse(verified[0]['passed'])
        self.assertIn('FAIL', verified[0]['message'])

    def test_mismatched_length(self):
        with self.assertRaises(ValueError):
            verifier.verify_responses(self.test_results, self.expected_results[:1])

    def test_missing_keys_in_test_results(self):
        incomplete_test = [{'name': 'Test 3', 'response': {'key': 'value'}}]
        with self.assertRaises(KeyError):
            verifier.verify_responses(incomplete_test, [self.expected_results[0]])

    def test_missing_keys_in_expected_results(self):
        incomplete_expected = [{'response_body': {'key': 'value'}}]
        with self.assertRaises(KeyError):
            verifier.verify_responses([self.test_results[0]], incomplete_expected)

if __name__ == '__main__':
    unittest.main()