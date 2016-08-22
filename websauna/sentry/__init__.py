import logging

from pyramid.config import Configurator

from websauna.utils.autoevent import bind_events


logger = logging.getLogger(__name__)


class AddonInitializer:
    """Configure this addon for websauna."""

    def __init__(self, config:Configurator):
        self.config = config

    def run(self):

        raven_dsn = self.config.registry.settings.get("raven.dsn")

        if not raven_dsn:
            logger.warn("raven.dsn setting missing - does not configure Sentry error handling")
            return

        # This will make sure our initialization hooks are called later
        bind_events(self.config.registry.initializer, self)

        self.config.include("pyramid_raven")

        from . import subscribers
        self.config.scan(subscribers)


def includeme(config: Configurator):
    """Entry point for Websauna main app to include this addon.

    In the Initializer of your app you should have:

        def include_addons(self):
            # ...
            self.config.include("websauna.sentry")

    """
    addon_init = AddonInitializer(config)
    addon_init.run()

