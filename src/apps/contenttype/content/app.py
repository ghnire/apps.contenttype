from plone import schema
from plone.app.dexterity import textindexer
from plone.app.textfield import RichText
from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from zope.interface import implementer


class IApp(model.Schema):
    """Dexterity-Schema for Apps"""

    textindexer.searchable("details")
    details = RichText(
        title="Details",
        description="Description of the Application (max. 2000 characters)",
        max_length=2000,
        required=True,
    )

    applink = schema.URI(
        title="Application URI",
        description="Enter the URI to the application",
    )

    opennew = schema.Bool(
        title="Open App in new Window or Tab",
        description="Enabling this option will open the app in a new tab or window by default",
        default=True,
    )

    openfrommenu = schema.Bool(
        title="Open App directly from menu",
        description="Enabling this option will open the app if you click on it in the menu",
        default=False,
    )

    company = schema.TextLine(
        title="Company",
        required=False,
    )

    appicon = NamedBlobImage(
        title="Icon",
        description="Icon of the application",
        required=False,
    )


@implementer(IApp)
class App(Container):
    """App instance class"""
