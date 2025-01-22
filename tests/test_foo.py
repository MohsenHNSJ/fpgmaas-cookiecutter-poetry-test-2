"""This module handles testing functionality"""

from fpgmaas_cookiecutter_poetry_test_2.main_func import main_func


def test_foo() -> None:
    """Initial test function"""
    assert main_func("test") == "test"
