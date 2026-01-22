"""
Base test class for all test automation.
Provides common setup and teardown functionality.
"""
import pytest
from infra.browser import Browser


class TestBase:
    """Base class for all test classes"""
    
    def setup_method(self):
        """Setup method called before each test method"""
        pass
    
    def teardown_method(self):
        """Teardown method called after each test method"""
        pass


class TestWebBase(TestBase):
    """Base class for web tests"""
    
    def setup_method(self):
        """Setup method for web tests"""
        super().setup_method()
        # Initialize browser here if needed
        
    def teardown_method(self):
        """Teardown method for web tests"""
        # Clean up browser resources here if needed
        super().teardown_method()
