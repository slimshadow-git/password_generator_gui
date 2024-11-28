import unittest
from ..utils.validators import validate_password_length

class TestValidators(unittest.TestCase):
    def test_valid_password_length(self):
        """Test if the password length validation allows valid lengths."""
        self.assertTrue(validate_password_length(8))
        self.assertTrue(validate_password_length(15))
        self.assertTrue(validate_password_length(20))

    def test_invalid_password_length(self):
        """Test if the password length validation rejects invalid lengths."""
        self.assertFalse(validate_password_length(7))  # Too short
        self.assertFalse(validate_password_length(21))  # Too long
        self.assertFalse(validate_password_length(0))  # Edge case
