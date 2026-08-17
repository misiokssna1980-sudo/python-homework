import pytest


# 2. МЕТОД: Получение списка проектов (GET /projects)
# ==========================================

def test_get_projects_positive(api_client):
    """Позитивный тест: Получение списка проектов авторизованным пользователем"""
    response = api_client.get_projects()

    assert response.status_code == 200
    assert isinstance(response.json(), list) or "content" in response.json()

def test_get_projects_negative_unauthorized(api_client):
    """Негативный тест: Запрос списка проектов с невалидным токеном"""
    from api_client import YougileProjectAPI
    bad_client = YougileProjectAPI("https://ru.yougile.com/api-v2", "invalid_token")

    response = bad_client.get_projects()

    assert response.status_code == 401