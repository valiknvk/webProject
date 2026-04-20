from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    secret_key: str = os.environ.get("FLASK_SECRET_KEY", "change-me-before-production")
    db_host: str = os.environ.get("POSTGRES_DB_HOST", "localhost")
    db_name: str = os.environ.get("POSTGRES_DB_NAME", "web")
    db_user: str = os.environ.get("POSTGRES_DB_USER", "postgres")
    db_pass: str = os.environ.get("POSTGRES_DB_PASS", "postgres")
    db_port: str = os.environ.get("POSTGRES_DB_PORT", "5432")
    session_lifetime_minutes: int = int(os.environ.get("SESSION_LIFETIME_MINUTES", "5"))
    app_host: str = os.environ.get("FLASK_RUN_HOST", "0.0.0.0")
    app_port: int = int(os.environ.get("FLASK_RUN_PORT", "80"))
    debug: bool = os.environ.get("FLASK_DEBUG", "false").lower() == "true"


settings = Settings()
