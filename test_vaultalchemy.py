# test_vaultalchemy.py
"""
Tests for VaultAlchemy module.
"""

import unittest
from vaultalchemy import VaultAlchemy

class TestVaultAlchemy(unittest.TestCase):
    """Test cases for VaultAlchemy class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VaultAlchemy()
        self.assertIsInstance(instance, VaultAlchemy)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VaultAlchemy()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
