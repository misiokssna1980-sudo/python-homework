import pytest

# ==========================================
# 1. МЕТОД: Создание проекта (POST /projects)
# ==========================================

def test_create_project_positive(api_client, unique_title):
    """Позитивный тест: Создание проекта с валидным названием"""
    payload = {
        "title": unique_title
    }
    response = api_client.create_project(payload)

    assert response.status_code == 201
    res_data = response.json()
    assert "id" in res_data
    assert res_data.get("title") == unique_title

def test_create_project_negative_missing_title(api_client):
    """Негативный тест: Создание проекта без обязательного поля title"""
    payload = {
        "users": {}
    }
    response = api_client.create_project(payload)

    assert response.status_code in [400, 422]


