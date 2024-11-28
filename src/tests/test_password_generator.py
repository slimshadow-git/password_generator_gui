import unittest
from ..utils.password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_generate_password_length(self):
        """Test if the password generated has the correct length."""
        password = generate_password(12)
        self.assertEqual(len(password), 12)

    def test_generate_password_invalid_length(self):
        """Test if ValueError is raised for invalid password lengths."""
        with self.assertRaises(ValueError):
            generate_password(5)  # Invalid length (less than 8)
        
        with self.assertRaises(ValueError):
            generate_password(21)  # Invalid length (greater than 20)
