# test_pulseomen.py
"""
Tests for PulseOmen module.
"""

import unittest
from pulseomen import PulseOmen

class TestPulseOmen(unittest.TestCase):
    """Test cases for PulseOmen class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PulseOmen()
        self.assertIsInstance(instance, PulseOmen)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PulseOmen()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
