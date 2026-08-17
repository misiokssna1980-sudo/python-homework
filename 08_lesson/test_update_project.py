import pytest


# ==========================================
# 3. МЕТОД: Обновление проекта (PUT /projects/{id})
# ==========================================

def test_update_project_positive(api_client, unique_title):
    """Позитивный тест: Изменение названия существующего проекта"""
    # Шаг 1: Создаем проект для теста
    create_payload = {"title": unique_title}
    create_res = api_client.create_project(create_payload).json()
    project_id = create_res["id"]

    # Шаг 2: Обновляем его
    new_title = f"{unique_title}_updated"
    update_payload = {"title": new_title}

    response = api_client.update_project(project_id, update_payload)

    assert response.status_code == 200
    assert response.json().get("title") == new_title

def test_update_project_negative_not_found(api_client):
    """Негативный тест: Обновление несуществующего проекта"""
    fake_id = "00000000-0000-0000-0000-000000000000"
    payload = {"title": "Новое имя"}

    response = api_client.update_project(fake_id, payload)

    assert response.status_code in [404, 400]