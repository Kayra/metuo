import os


from server.helpers.app_helpers import is_production


class TestAppHelpers:

    def test_is_production(self):
        os.environ['PYTHON_ENV'] = 'production'
        assert is_production() is True

    def test_is_not_production(self):
        os.environ['PYTHON_ENV'] = 'definitely_not_production'
        assert is_production() is False

    def test_is_dev(self):
        os.environ['PYTHON_ENV'] = 'dev'
        assert is_production() is False

    def test_is_production_no_env_set(self):
        assert is_production() is False
