from collective.gridlisting import _
from collective.gridlisting.vocabularies import LISTING_TITLE_TAGS
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.z3cform import layout
from zope import schema
from zope.interface import Interface


class IGridListingControlPanel(Interface):
    row_css_class = schema.TextLine(
        title=_("Container row"),
        description=_("eg. if you want to set gutter between columns define here."),
        required=False,
    )

    column_css_class = schema.TextLine(
        title=_("Column"),
        description=_(
            "Use grid css class combinations for column. Example: 'col-12 col-md-6 col-xl-3'"
        ),
        required=False,
    )

    column_content_css_class = schema.TextLine(
        title=_("Column content"),
        description=_(
            "If you want borders or backgrounds inside the column define it here."
        ),
        required=False,
        default="row",
    )

    column_content_text_css_class = schema.TextLine(
        title=_("Column content text"),
        description=_("CSS class(es) for title/description/link in column content"),
        default="col",
        required=False,
    )

    column_content_image_css_class = schema.TextLine(
        title=_("Column content image"),
        description=_("CSS class(es) for preview image in column content"),
        default="col-3 text-end",
        required=False,
    )

    item_title_tag = schema.Choice(
        title=_("Listing item title tag"),
        values=LISTING_TITLE_TAGS,
        default="h3",
    )

    preview_scale = schema.Choice(
        title=_("Preview image scale"),
        vocabulary="plone.app.vocabularies.ImagesScales",
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


class GridListingControlPanel(RegistryEditForm):
    schema = IGridListingControlPanel
    schema_prefix = "collective.gridlisting"
    label = _("Grid Listing Settings")


GridListingControlPanelView = layout.wrap_form(
    GridListingControlPanel, ControlPanelFormWrapper
)
