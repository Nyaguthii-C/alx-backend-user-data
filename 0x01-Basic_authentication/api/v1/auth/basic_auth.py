#!/usr/bin/env python3
"""Class that inherits from Auth"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """A basic auth class"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Args:
             authorization_header: str - authorization string
        Returns:
             the Base64 part of the Authorization header
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if authorization_header.startswith("Basic "):
            return authorization_header.split(" ")[1]
        else:
            return None
