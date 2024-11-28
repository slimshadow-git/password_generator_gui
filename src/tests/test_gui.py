import unittest
from tkinter import Tk
from ..app.gui import PasswordGeneratorApp
from unittest.mock import patch

class TestPasswordGeneratorApp(unittest.TestCase):
    def setUp(self):
        """Set up the testing environment."""
        self.root = Tk()
        self.app = PasswordGeneratorApp(self.root)

    def tearDown(self):
        """Clean up after each test."""
        self.root.destroy()

    @patch('..app.gui.generate_password')
    def test_generate_password_button(self, mock_generate_password):
        """Test if the Generate Password button calls the generate_password method."""
        mock_generate_password.return_value = "TestPassword123"
        self.app.generate_password()
        mock_generate_password.assert_called_once()
        # Further checks can be made for the password entry update if needed
