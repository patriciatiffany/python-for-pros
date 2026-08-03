import pytest
from pydantic import ValidationError

from computer import Computer


def test_computer_valid():
    test_computer = Computer(brand="apple", ram_gb=16, hard_drive_gb=512)
    assert test_computer.brand == "apple"
    assert test_computer.ram_gb == 16
    assert test_computer.hard_drive_gb == 512


def test_computer_rejects_string_ram():
    with pytest.raises(ValidationError):
        Computer(brand="apple", ram_gb="16", hard_drive_gb=512)


def test_computer_requires_brand():
    with pytest.raises(ValidationError):
        Computer(ram_gb=16, hard_drive_gb=512)
