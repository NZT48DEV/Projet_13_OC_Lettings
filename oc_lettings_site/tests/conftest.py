import copy
import logging
import logging.config

import pytest


def _close_logger_handlers(logger: logging.Logger) -> None:
    """
    Flush, close and remove all handlers attached to a given logger.

    This is required to avoid file locking issues (especially on Windows)
    and to ensure a clean logging state between tests.
    """
    for handler in list(logger.handlers):
        try:
            handler.flush()
            handler.close()
        except Exception:
            pass
        logger.removeHandler(handler)


@pytest.fixture
def configure_test_logging(settings, tmp_path):
    """
    Reconfigure Django logging to write all log files
    into a temporary directory for the duration of a test.

    This fixture:
    - removes existing logging handlers configured by Django/pytest
    - redirects file-based handlers to a temporary directory
    - reapplies the logging configuration using dictConfig
    - cleans up all handlers after the test

    It guarantees isolation between tests and prevents
    file locking issues on Windows.
    """
    # --- PRE-TEST CLEANUP (remove existing handlers) ---
    _close_logger_handlers(logging.getLogger())  # root logger
    for name in ["django", "django.request", "oc_lettings.access", "django.server"]:
        _close_logger_handlers(logging.getLogger(name))

    # --- SETUP ---
    test_log_dir = tmp_path / "logs"
    test_log_dir.mkdir()

    cfg = copy.deepcopy(settings.LOGGING)

    cfg["handlers"]["file"]["filename"] = str(test_log_dir / "django.log")
    cfg["handlers"]["errors_file"]["filename"] = str(test_log_dir / "errors.log")
    cfg["handlers"]["access_file"]["filename"] = str(test_log_dir / "access.log")

    logging.config.dictConfig(cfg)

    yield test_log_dir

    # --- POST-TEST CLEANUP ---
    _close_logger_handlers(logging.getLogger())
    for name in ["django", "django.request", "oc_lettings.access", "django.server"]:
        _close_logger_handlers(logging.getLogger(name))
