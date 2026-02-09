import logging

from django.http import HttpResponse
from django.urls import path


def ok_view(request):
    """Minimal view used by tests to return a 200 OK response."""
    return HttpResponse("OK", status=200)


def _flush_access_logger() -> None:
    """Flush access logger handlers to ensure logs are written to disk."""
    logger = logging.getLogger("oc_lettings.access")
    for handler in logger.handlers:
        try:
            handler.flush()
        except Exception:
            pass


def _read_access_log(log_dir) -> str:
    """Read access.log content after flushing handlers."""
    _flush_access_logger()
    access_path = log_dir / "access.log"
    assert access_path.exists()
    return access_path.read_text(encoding="utf-8")


def test_access_middleware_logs_request(client, settings, configure_test_logging):
    """The access middleware should log standard requests."""
    test_urls = type(
        "TestUrls",
        (),
        {"urlpatterns": [path("test-access/", ok_view)]},
    )
    settings.ROOT_URLCONF = test_urls

    response = client.get("/test-access/")
    assert response.status_code == 200

    content = _read_access_log(configure_test_logging)

    assert content.strip()
    assert "GET" in content
    assert "/test-access/" in content
    assert "200" in content


def test_access_middleware_does_not_log_static(
    client, settings, configure_test_logging
):
    """The access middleware should not log requests to /static/."""
    test_urls = type(
        "TestUrls",
        (),
        {"urlpatterns": [path("static/test.css", ok_view)]},
    )
    settings.ROOT_URLCONF = test_urls

    client.get("/static/test.css")

    content = _read_access_log(configure_test_logging)

    assert "/static/" not in content
