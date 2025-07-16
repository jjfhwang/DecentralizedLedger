# test_decentralizedledger.py
"""
Tests for DecentralizedLedger module.
"""

import unittest
from decentralizedledger import DecentralizedLedger

class TestDecentralizedLedger(unittest.TestCase):
    """Test cases for DecentralizedLedger class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DecentralizedLedger()
        self.assertIsInstance(instance, DecentralizedLedger)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DecentralizedLedger()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
