import re
from typing import Optional

def validate_phone_number(phone: str) -> bool:
    """Проверка корректности номера телефона"""
    pattern = r'^\+?[1-9]\d{1,14}$'
    return bool(re.match(pattern, phone))

def validate_username(username: str) -> bool:
    """Проверка корректности username"""
    pattern = r'^@[a-zA-Z0-9_]{5,32}$'
    return bool(re.match(pattern, username))

def sanitize_message(message: str, max_length: int = 4096) -> str:
    """Очистка и обрезка сообщения"""
    if len(message) > max_length:
        message = message[:max_length-3] + "..."
    return message