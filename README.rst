This is a Python package for websauna.sentry addon for `Websauna framework <https://websauna.org>`_.

Features
========

* Extra logging context like user email and country

* Internally uses `pyramid_raven <https://github.com/thruflo/pyramid_raven>`_.

.. image:: https://raw.githubusercontent.com/websauna/websauna.sentry/master/screenshots/user_context.png
    :width: 640px;

Installation
============

Install package from PyPi.

We assume you have Sentry configured with self-signed certificates that the system cannot verify.

**Note**: When you create a new Pyramid project in Sentry. It gives you some sane settings to use below.

In your ``production.ini`` settings configure::

    [app:main]
    # ...

    # This is where our internal server errors go.
    # Exceptions are logged with extra user details.
    raven.dsn = https://x:y@sentry.example.com:443/1?verify_ssl=0&timeout=30

    #
    # Sentry
    #

    # debugtoolbar may interfere with exception capturance
    debugtoolbar.enabled = false

    # Only use special internal server error capture,
    # and do not post (twice) internal server errors to
    # sentry through Python logging system.
    # HOWEVER this means the exceptions do not appear in console/log files either.
    websauna.log_internal_server_error = false

    #
    # Logger configuration
    #


    # Also add Sentry to normal Python logging configuration, so you catch
    # warns and errors from loggers.
    [handlers]
    keys = console, sentry

    # The root error capture
    [logger_root]
    level = DEBUG
    handlers = console, sentry, logfile

    [handler_sentry]
    class = raven.handlers.logging.SentryHandler
    args = ('https://x:a61b30d8871c44948db57de377d5ff5f@sentry.example.com/2?verify_ssl=0&timeout=30',)
    level = WARNING
    formatter =

In your application Initializer do::

    def include_addons(self):
        # ...
        self.config.include("websauna.sentry")

For Raven client options (URL parameters) see

* https://docs.sentry.io/hosted/clients/python/transports/

Usage
=====

Test in production by going to the Websauna internal error trigger URL::

    http://yoursite.example.com/error-trigger

Or on local development::

    http://localhost:6543/error-trigger

This will trigger test exception and logging messages you should see in Sentry.

Extra logging context
---------------------

Examples::

    import logging

    from websauna.system.core.loggingcapture import get_logging_user_context

    logger = logging.getLogger(__name__)

    def my_view(request):
        # If you're actually catching an exception, use `exc_info=True`
        logger.error('There was an error, with a stacktrace!', exc_info=True)

        user_context = get_logging_user_context(request)
        logger.error("Logging message on error level", exc_info=True, extra={"user": user_context})

More information
----------------

* https://docs.sentry.io/hosted/clients/python/integrations/logging/


More information
================

Please see https://websauna.org/