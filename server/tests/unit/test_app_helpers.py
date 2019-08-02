import os


from server.helpers.app_helpers import is_production


class TestAppHelpers:

    def test_is_production(self):

        os.environ['PYTHON_ENV'] = 'production'

        assert is_production() is True

    def test_is_not_production(self):
        pass

    def test_is_dev(self):
        pass
