import logging

from pyramid.events import subscriber
from websauna.system.core.events import InternalServerError

from websauna.system.core.loggingcapture import get_logging_user_context


logger = logging.getLogger(__name__)


@subscriber(InternalServerError)
def log_internal_server_error(event: InternalServerError):
    """Catch 500 errors and send them to Sentry with additional details."""

    request = event.request

    user_context = get_logging_user_context(event.request)
    request.raven.user_context(user_context)
    request.raven.captureException()


