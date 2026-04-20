from __future__ import annotations

import psycopg2
import psycopg2.extras

from settings import settings


def get_connection():
    return psycopg2.connect(
        dbname=settings.db_name,
        user=settings.db_user,
        password=settings.db_pass,
        host=settings.db_host,
        port=settings.db_port,
    )


def fetch_account_by_username(username: str):
    with get_connection() as connection:
        with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
            return cursor.fetchone()


def fetch_account_by_id(account_id: int):
    with get_connection() as connection:
        with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute('SELECT * FROM users WHERE id = %s', (account_id,))
            return cursor.fetchone()


def create_account(fullname: str, username: str, password_hash: str, email: str):
    with get_connection() as connection:
        with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute(
                'INSERT INTO users (fullname, username, password, email) VALUES (%s, %s, %s, %s)',
                (fullname, username, password_hash, email),
            )
            connection.commit()
