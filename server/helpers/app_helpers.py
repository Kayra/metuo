import os


def is_production() -> bool:
    return os.getenv('PYTHON_ENV') == 'production'
