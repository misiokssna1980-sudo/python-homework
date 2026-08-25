# Тесты для работы с таблицей students
# - Каждый создаёт уникальную запись (для изоляции)
# - В блоке finally выполняется явная очистка (удаление созданных данных)
# - Используется fixture db_session из conftest.py

import uuid
from sqlalchemy import insert, select, update, delete
from database import students


def _unique_email():
    """Генерирует уникальный email для тестовой записи."""
    return f"test_{uuid.uuid4().hex}@example.com"


def test_add_student(db_session):
    """
    Тест добавления студента.
    Шаги:
    1. Вставляем запись.
    2. Читаем её обратно и проверяем поля.
    3. В finally удаляем запись по email.
    """
    email = _unique_email()
    name = "John Doe"
    try:
        # Вставляем студента и получаем id через RETURNING
        res = db_session.execute(
            insert(students).
            values(name=name, email=email).
            returning(students.c.id)
        )
        student_id = res.scalar_one()

        # Читаем запись по id и проверяем поля
        row = db_session.execute(select(students).
                                 where(students.c.id == student_id)).first()
        assert row is not None
        assert row._mapping["name"] == name
        assert row._mapping["email"] == email
    finally:
        # Очистка: удаляем созданную запись по email
        db_session.execute(delete(students).where(students.c.email == email))
        db_session.commit()


def test_update_student(db_session):
    """
    Тест обновления студента.
    Шаги:
    1. Создаём начальную запись.
    2. Обновляем имя.
    3. Читаем и проверяем обновлённое значение.
    4. Удаляем запись в finally.
    """
    email = _unique_email()
    name = "Nastya"
    new_name = "Nastya Updated"
    try:
        # Создаём запись и получаем id
        res = db_session.execute(
            insert(students).
            values(name=name, email=email).
            returning(students.c.id)
        )
        student_id = res.scalar_one()

        # Обновляем поле name
        db_session.execute(
            update(students).
            where(students.c.id == student_id).values(name=new_name)
        )

        # Читаем запись и проверяем, что имя изменилось
        row = db_session.execute(select(students).
                                 where(students.c.id == student_id)).first()
        assert row is not None
        assert row._mapping["name"] == new_name
    finally:
        # Удаляем тестовую запись
        db_session.execute(delete(students).where(students.c.email == email))
        db_session.commit()


def test_delete_student(db_session):
    """
    Тест удаления студента.
    Шаги:
    1. Создаём запись.
    2. Удаляем её (операция под тест).
    3. Проверяем, что запись отсутствует.
    4. В finally повторно пытаемся удалить на случай, если тест упал раньше.
    """
    email = _unique_email()
    name = "To Be Deleted"
    try:
        # Создаём запись и получаем id
        res = db_session.execute(
            insert(students).
            values(name=name, email=email).
            returning(students.c.id)
        )
        student_id = res.scalar_one()

        # Удаляем запись — это действие под тест
        db_session.execute(delete(students).where(students.c.id == student_id))

        # Проверяем, что запись больше не существует
        row = db_session.execute(select(students).
                                 where(students.c.id == student_id)).first()
        assert row is None
    finally:
        # Гарантированная очистка: на случай, если удаление не сработало
        db_session.execute(delete(students).where(students.c.email == email))
        db_session.commit()