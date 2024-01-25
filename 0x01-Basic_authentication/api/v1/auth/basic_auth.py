#!/usr/bin/env python3
"""Class that inherits from Auth"""
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar


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

    def decode_base64_authorization_header(
                      self, base64_authorization_header: str) -> str:
        """
        Args:
             base64_authorization_header - base64 string
        Returns:
             the decoded value of a Base64 string
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            decoded_str = decoded_bytes.decode('utf-8')
            return decoded_str
        except base64.binascii.Error:
            return None

    def extract_user_credentials(
                self, decoded_base64_authorization_header: str) -> (str, str):
        """
        Args:
             decoded_base64_authorization_header - decoded base64 string
        Returns:
             username and password from base64 decoded value
        """
        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ":" in decoded_base64_authorization_header:
            email, pswd = decoded_base64_authorization_header.split(":", 1)
            return email, pswd
        else:
            return None, None

    def user_object_from_credentials(
                self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
        Args:
            user_email, user_pwd - user credential to look up user
        Return:
            the User instance based on his email and password
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            Users = User.search({'email': user_email})
        except Exception:
            return None

        for user in Users:
            if user.is_valid_password(user_pwd):
                return user
            else:
                return None
                return user
