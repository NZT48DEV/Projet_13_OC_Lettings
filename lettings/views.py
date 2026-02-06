import logging

from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Letting

logger = logging.getLogger(__name__)


def index(request):
    """
    Display the list of all lettings.
    """
    logger.info("Requesting index")

    lettings_list = Letting.objects.all()

    logger.info("Requesting lettings_list : %s items", lettings_list.count())

    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


def letting(request, letting_id):
    """
    Display the details of a single letting.
    """
    logger.info(
        "Requesting letting detail (letting_id=%s)",
        letting_id,
    )

    try:
        letting_obj = get_object_or_404(Letting, id=letting_id)
    except Http404:
        logger.warning(
            "Letting_id=%s not found", letting_id, extra={"letting_id": letting_id}
        )
        raise

    context = {
        "title": letting_obj.title,
        "address": letting_obj.address,
    }
    return render(request, "lettings/letting.html", context)
