import pytest

from server import create_app


@pytest.fixture()
def flask_app():

    app = create_app()
    app_context = app.test_request_context()
    app_context.push()
    client = app.test_client()

    yield client
