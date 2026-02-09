import logging
import time

access_logger = logging.getLogger("oc_lettings.access")

EXCLUDED_PATH_PREFIXES = (
    "/static/",
    "/media/",
    "/favicon.ico",
)


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.perf_counter()
        response = self.get_response(request)
        duration_ms = (time.perf_counter() - start) * 1000

        path = request.get_full_path()

        if not path.startswith(EXCLUDED_PATH_PREFIXES):
            ip = request.META.get("REMOTE_ADD", "-")
            method = request.method
            status = response.status_code
            access_logger.info(
                "%s %s %s %s %.1fms", ip, method, path, status, duration_ms
            )

        return response
