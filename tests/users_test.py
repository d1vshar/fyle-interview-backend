def test_get_user_by_id(client, h_teacher_1):
    """
    get user by id
    """
    response = client.get(
        '/user/id',
        json={
            "id": 1
        }
    )

    assert response.status_code == 200
    data = response.json['data']

    assert data['id'] == 1

def test_get_user_by_email(client, h_teacher_1):
    """
    get user by email
    """
    response = client.get(
        '/user/email',
        json={
            "email": "student1@fylebe.com"
        }
    )

    assert response.status_code == 200
    data = response.json['data']

    assert data['id'] == 1
