"""Init and utils."""

from zope.i18nmessageid import MessageFactory

import logging


PACKAGE_NAME = "apps.contenttype"

_ = MessageFactory(PACKAGE_NAME)

logger = logging.getLogger(PACKAGE_NAME)
