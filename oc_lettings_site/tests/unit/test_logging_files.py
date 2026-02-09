import logging


def _flush_all():
    """
    Flush all handlers for the main loggers used in tests.

    This ensures that log records are physically written to disk
    before assertions read log files.

    This is especially important on Windows, where file buffers
    may not be flushed immediately, leading to empty or missing
    log files during tests.
    """
    for logger_name in ["", "django.request", "oc_lettings.access"]:
        logger = logging.getLogger(logger_name)  # "" refers to the root logger
        for h in logger.handlers:
            try:
                h.flush()
            except Exception:
                pass


def test_root_logs_go_to_django_log(configure_test_logging):
    """
    Ensure that logs emitted via the root logger are written
    to the main django.log file.
    """
    log_dir = configure_test_logging
    logging.getLogger().info("ROOT_INFO_TEST")

    _flush_all()

    assert (log_dir / "django.log").exists()
    content = (log_dir / "django.log").read_text(encoding="utf-8")
    assert "ROOT_INFO_TEST" in content


def test_django_request_warning_goes_to_errors_log(configure_test_logging):
    """
    Ensure that WARNING-level logs emitted by the 'django.request'
    logger are written to the errors.log file.
    """
    log_dir = configure_test_logging
    logging.getLogger("django.request").warning("REQUEST_WARNING_TEST")

    _flush_all()

    assert (log_dir / "errors.log").exists()
    content = (log_dir / "errors.log").read_text(encoding="utf-8")
    assert "REQUEST_WARNING_TEST" in content


def test_access_logger_goes_to_access_log(configure_test_logging):
    """
    Ensure that logs emitted by the custom access logger
    are written to the access.log file.
    """
    log_dir = configure_test_logging
    logging.getLogger("oc_lettings.access").info("ACCESS_TEST")

    _flush_all()

    assert (log_dir / "access.log").exists()
    content = (log_dir / "access.log").read_text(encoding="utf-8")
    assert "ACCESS_TEST" in content
