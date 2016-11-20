import logging

from pyramid.events import subscriber
from raven.context import get_active_contexts
from websauna.system.core.events import InternalServerError

from websauna.system.core.loggingcapture import get_logging_user_context
from websauna.system.task.events import TaskFinished

logger = logging.getLogger(__name__)


@subscriber(InternalServerError)
def log_internal_server_error(event: InternalServerError):
    """Catch 500 errors and send them to Sentry with additional details."""

    request = event.request

    user_context = get_logging_user_context(event.request)
    request.raven.user_context(user_context)
    request.raven.captureException()


@subscriber(TaskFinished)
def on_task_finished(event: TaskFinished):
    """Clean up raven context when Celery is done with a task."""

    for context in get_active_contexts():
        context.clear()

