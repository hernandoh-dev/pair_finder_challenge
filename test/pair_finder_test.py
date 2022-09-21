from argparse import Namespace
from unittest import TestCase
from unittest.mock import patch
from main import main


class PathFinderTest(TestCase):
    """
    Script test cases.
    """

    def setUp(self):
        self.number_list = [1, 9, 5, 0, 20, -4, 12, 16, 7]

    @patch("builtins.print")
    def test_successful_process(self, mock_print):
        args = Namespace(
            target=12,
            numbers=self.number_list,
        )
        main(args)
        mock_print.assert_called()
        self.assertTrue("9 numbers" in mock_print.call_args_list[1][0][0])
        self.assertTrue(len(mock_print.call_args_list[0][0][0]) == 3)

    @patch("builtins.print")
    def test_process_with_only_one_number(self, mock_print):
        args = Namespace(
            target=12,
            numbers=[1]
        )
        main(args)
        mock_print.assert_called()
        mock_print.assert_called_with(
            "at least 2 values are required to carry out the process"
        )

    @patch("builtins.print")
    def test_process_with_none_pairs(self, mock_print):
        args = Namespace(
            target=12,
            numbers=[1,2,3]
        )
        main(args)
        mock_print.assert_called()
        self.assertTrue("3 numbers" in mock_print.call_args_list[1][0][0])
        self.assertTrue(len(mock_print.call_args_list[0][0][0]) == 0)
