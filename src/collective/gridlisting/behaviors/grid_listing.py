# -*- coding: utf-8 -*-

from collective.gridlisting import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from plone.supermodel import directives
from Products.CMFPlone.utils import safe_hasattr
from zope.component import adapter
from zope.interface import implementer
from zope.interface import Interface
from zope.interface import provider


class IGridListingMarker(Interface):
    pass


@provider(IFormFieldProvider)
class IGridListing(model.Schema):
    """ """

    column_css_class = schema.TextLine(
        title=_("Column CSS Class"),
        description=_(
            "Use grid css class combinations for column. Example: 'col-12 col-md-6 col-xl-3'"
        ),
        required=False,
    )

    enable_masonry = schema.Bool(
        title=_("Enable masonry layout"),
        description=_("See masonry documentation."),
        required=False,
        default=False,
    )

    masonry_options = schema.TextLine(
        title=_("Additional masonry options"),
        description=_(
            'Options for "pat-masonry" see https://patternslib.com/demos/masonry.'
        ),
        required=False,
    )

    directives.fieldset(
        "gridlisting",
        label=_("Grid listing"),
        description=_(
            "Define grid listing properties. For further information see https://getbootstrap.com/docs/5.3/layout/grid/"
        ),
        fields=[
            "column_css_class",
            "enable_masonry",
            "masonry_options",
        ],
    )


@implementer(IGridListing)
@adapter(IGridListingMarker)
class GridListing(object):
    def __init__(self, context):
        self.context = context

    @property
    def column_css_class(self):
        if safe_hasattr(self.context, "column_css_class"):
            return self.context.column_css_class
        return None

    @column_css_class.setter
    def column_css_class(self, value):
        self.context.column_css_class = value

    @property
    def enable_masonry(self):
        if safe_hasattr(self.context, "enable_masonry"):
            return self.context.enable_masonry
        return None

    @enable_masonry.setter
    def enable_masonry(self, value):
        self.context.enable_masonry = value

    @property
    def masonry_options(self):
        if safe_hasattr(self.context, "masonry_options"):
            return self.context.masonry_options
        return None

    @masonry_options.setter
    def masonry_options(self, value):
        self.context.masonry_options = value
