from django.test import override_settings


# HELPER
@override_settings(DEBUG=False, DEBUG_PROPAGATE_EXCEPTIONS=False)
def assert_custom_error_page(response, status_code, template_name, message):
    assert response.status_code == status_code

    names = [t.name for t in response.templates]
    assert template_name in names

    if isinstance(message, (list, tuple, set)):
        assert any(msg in response.text for msg in message)
    else:
        assert message in response.text
