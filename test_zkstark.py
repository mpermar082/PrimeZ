# test_zkstark.py
"""
Tests for ZKStark module.
"""

import unittest
from zkstark import ZKStark

class TestZKStark(unittest.TestCase):
    """Test cases for ZKStark class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZKStark()
        self.assertIsInstance(instance, ZKStark)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZKStark()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
