from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parent
CONTENT_DIR = BASE_DIR / "content"
TEMPLATE_PATH = CONTENT_DIR / "portfolio.template.json"
DEFAULT_PROFILE_PATH = CONTENT_DIR / "portfolio.local.json"


def _read_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as file_handle:
        return json.load(file_handle)


def _build_navigation_sections(profile: dict[str, Any]) -> list[dict[str, str]]:
    sections: list[dict[str, str]] = [{"id": "about", "title": "About"}]

    if profile.get("experience"):
        sections.append({"id": "experience", "title": "Experience"})
    if profile.get("education"):
        sections.append({"id": "education", "title": "Education"})
    if profile.get("skills", {}).get("items"):
        sections.append({"id": "skills", "title": "Skills"})
    if profile.get("interests"):
        sections.append({"id": "interests", "title": "Interests"})

    return sections


def load_portfolio_profile() -> dict[str, Any]:
    configured_path = os.environ.get("PORTFOLIO_PROFILE_PATH")
    local_path = Path(configured_path).expanduser() if configured_path else DEFAULT_PROFILE_PATH
    source_path = local_path if local_path.exists() else TEMPLATE_PATH

    profile = _read_json(source_path)
    profile["using_template"] = source_path == TEMPLATE_PATH
    profile["source_path"] = str(source_path.relative_to(BASE_DIR)) if source_path.is_relative_to(BASE_DIR) else str(source_path)
    profile["navigation_sections"] = _build_navigation_sections(profile)

    resume_url = profile.get("profile", {}).get("resume_url") or "#"
    profile["profile"]["resume_url"] = resume_url
    profile["profile"]["resume_available"] = resume_url != "#"

    return profile
