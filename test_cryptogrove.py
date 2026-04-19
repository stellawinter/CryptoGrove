# test_cryptogrove.py
"""
Tests for CryptoGrove module.
"""

import unittest
from cryptogrove import CryptoGrove

class TestCryptoGrove(unittest.TestCase):
    """Test cases for CryptoGrove class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoGrove()
        self.assertIsInstance(instance, CryptoGrove)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoGrove()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
