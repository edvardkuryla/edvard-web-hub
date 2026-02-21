def test_login_user(client):

    # регистрация
    client.post(
        "/auth/register",
        json={
            "name": "Testus",
            "email": "me@test.com",
            "password": "123456789"
        }
    )

    # логин
    response = client.post(
        "/auth/login",
        data={
            "username": "me@test.com",
            "password": "123456789"
        }
    )

    assert response.status_code == 200

    tokens = response.json()
    access_token = tokens["access_token"]

    # доступ к защищённому маршруту
    response = client.get(
        "/auth/me",
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    assert response.status_code == 200