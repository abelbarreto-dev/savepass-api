from re import match


def regex(key: str) -> str | None:
    reg_ex = {
        'username': r'^([a-z._]+)([a-z0-9_]+)$',
        'email': r'([a-z0-9]+[.-_])*[a-z0-9]+@[a-z0-9-]+(\.[a-z]{2,})+',
        'password': r'^([A-Za-z0-9._+-/!|\\?¿@#$%)&*(}={]+)$',
        'mobile': r'^\\+([0-9]{2})([0-9]{2})([0-9]{5})([0-9]{4})$',
        'tag': r'^([a-z]+)([a-z_]+)([a-z]+)$',
    }
    return reg_ex[key] if key in reg_ex.keys() else None


def username_checker(username: str) -> bool:
    return bool(match(regex(key='username'), username))


def email_checker(email: str) -> bool:
    return bool(match(regex(key='email'), email))


def password_checker(password: str) -> bool:
    return bool(match(regex(key='password'), password))


def mobile_checker(mobile: str) -> bool:
    return bool(match(regex(key='mobile'), mobile))


def tag_checker(tag: str) -> bool:
    return bool(match(regex(key='tag'), tag))
