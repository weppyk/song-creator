import os
from typing import Optional
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("suno")

SUNO_API_BASE = "https://api.sunoapi.org"


def _get_api_key() -> str:
    key = os.environ.get("SUNO_API_KEY")
    if not key:
        raise RuntimeError("SUNO_API_KEY environment variable is not set")
    return key


@mcp.tool()
def get_credits() -> dict:
    """Get remaining Suno API credits for the account."""
    response = httpx.get(
        f"{SUNO_API_BASE}/api/v1/generate/credit",
        headers={"Authorization": f"Bearer {_get_api_key()}"},
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


@mcp.tool()
def generate_music(
    prompt: str,
    custom_mode: bool = False,
    instrumental: bool = False,
    model: str = "V4",
    callback_url: str = "",
    style: Optional[str] = None,
    title: Optional[str] = None,
    negative_tags: Optional[str] = None,
    vocal_gender: Optional[str] = None,
) -> dict:
    """Generate music via Suno API.

    In non-custom mode: only prompt is needed (max 500 chars), lyrics are auto-generated.
    In custom mode + instrumental: style and title are required.
    In custom mode + vocal: style, title, and prompt (used as exact lyrics) are required.

    Returns a taskId to poll for results.

    Args:
        prompt: Description of desired audio (non-custom) or exact lyrics (custom+vocal).
        custom_mode: Enable custom mode for manual style/title/lyrics control.
        instrumental: Generate music without vocals.
        model: Model version — V4, V4_5, V4_5PLUS, V4_5ALL, V5, V5_5.
        callback_url: URL to receive completion webhook (optional for manual polling).
        style: Music style/genre. Required in custom mode.
        title: Track title. Required in custom mode.
        negative_tags: Comma-separated styles to exclude e.g. "Heavy Metal, Upbeat Drums".
        vocal_gender: Preferred vocal gender — "m" or "f".
    """
    body: dict = {
        "customMode": custom_mode,
        "instrumental": instrumental,
        "model": model,
        "callBackUrl": callback_url,
        "prompt": prompt,
    }
    if style is not None:
        body["style"] = style
    if title is not None:
        body["title"] = title
    if negative_tags is not None:
        body["negativeTags"] = negative_tags
    if vocal_gender is not None:
        body["vocalGender"] = vocal_gender

    response = httpx.post(
        f"{SUNO_API_BASE}/api/v1/generate",
        headers={"Authorization": f"Bearer {_get_api_key()}"},
        json=body,
        timeout=30,
    )
    response.raise_for_status()
    return response.json()


@mcp.tool()
def get_task_status(task_id: str) -> dict:
    """Get the status and results of a music generation task.

    Poll this after generate_music to check progress and retrieve audio URLs.
    Status values: PENDING → TEXT_SUCCESS → FIRST_SUCCESS → SUCCESS (or FAILED variants).

    Args:
        task_id: The taskId returned by generate_music.
    """
    response = httpx.get(
        f"{SUNO_API_BASE}/api/v1/generate/record-info",
        headers={"Authorization": f"Bearer {_get_api_key()}"},
        params={"taskId": task_id},
        timeout=10,
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    mcp.run()
