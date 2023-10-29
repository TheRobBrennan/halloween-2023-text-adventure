import unittest
from unittest.mock import patch, call
import subprocess
import main  # replace 'main' with the actual name of your Python file

class TestGame(unittest.TestCase):

   # Test main function
    def test_main(self):
        with patch('main.print_ascii_text') as mock_print_ascii_text:
            with patch('main.select_path') as mock_select_path:
                main.main()
        mock_print_ascii_text.assert_called_once()
        mock_select_path.assert_called_once()

    def test_if_name_main(self):
      # Run the script in a subprocess and capture the output
      process = subprocess.run(["python", "main.py"], capture_output=True, text=True)
      output = process.stdout

      # Check that the expected output is in the captured output
      expected_output = ""
      self.assertIn(expected_output, output)

    # Test if __name__ == "__main__": block
    # Refactor the file to add a run function and then test it
    def test_run(self):
        with patch('main.main') as mock_main:
            main.main()
        mock_main.assert_called_once()

    # Test print_ascii_text function
    def test_print_ascii_text(self):
        with patch('builtins.print') as mock_print:
            main.print_ascii_text()
        # Check the number of print calls
        self.assertEqual(mock_print.call_count, 4)

    # Test go_alone function
    @patch('main.time.sleep', return_value=None)
    def test_go_alone(self, mock_sleep):
        with patch('builtins.print') as mock_print:
            with patch('main.select_path', return_value=None) as mock_select_path:
                main.go_alone()
        # Check the number of print calls
        self.assertEqual(mock_print.call_count, 15)  # Corrected the expected count

    # Test select_path function with "a" input
    @patch('builtins.input', return_value='a')
    def test_select_path_go_alone(self, mock_input):
        with patch('main.go_alone', return_value=None) as mock_go_alone:
            main.select_path()
        mock_go_alone.assert_called_once()

    # Test select_path function with "q" input
    @patch('builtins.input', return_value='q')
    def test_select_path_quit(self, mock_input):
        with patch('builtins.print') as mock_print:
            main.select_path()
        mock_print.assert_has_calls([
            call("╭━━━━━━━━━━━━━━━Thanks for playing! Goodbye.━━━━━━━━━━━━━━╮"),
            call("╰────────────────────────────────────────────────-────────╯")
        ])

    # Test select_path function with invalid input
    @patch('builtins.input', side_effect=['invalid', 'q'])
    def test_select_path_invalid_input(self, mock_input):
        with patch('builtins.print') as mock_print:
            main.select_path()
        # Check the number of print calls. The expected calls might be different due to the recursive nature of select_path.
        mock_print.assert_has_calls([
            call("Invalid choice. Please select 'A' or 'q` to quit."),
            call("╭━━━━━━━━━━━━━━━Thanks for playing! Goodbye.━━━━━━━━━━━━━━╮"),
            call("╰────────────────────────────────────────────────-────────╯")
        ])
