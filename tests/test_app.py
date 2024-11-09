from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_studies.app import app

clinte = TestClient(app)


def read_root_return_ok_and_helloworld():
    client = TestClient(app)  # Arrange(Corpo do teste)

    response = client.get('/')  # Act(Acao)

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Ola Mundo!'}  # Assert
