#!/usr/bin/env python3
"""API authentication"""

from flask import request
from typing import List, TypeVar


class Auth:
    """a class to manage the API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Check if authentication is required for the given path.

        Args:
            path (str): The path to be checked for authentication.
            excluded_paths (List[str]): paths exempted from authentication.

        Returns:
            bool: True if authentication required, False otherwise
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Generate an authorization header for the given request"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Verify user"""
        return None
