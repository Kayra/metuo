import os


def is_production() -> bool:

    if os.getenv('PYTHON_ENV') == 'production':
        return True
    else:
        return False
