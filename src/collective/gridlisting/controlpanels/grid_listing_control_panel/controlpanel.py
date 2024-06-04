# -*- coding: utf-8 -*-
from collective.gridlisting import _
from collective.gridlisting.interfaces import ICollectiveGridlistingLayer
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.restapi.controlpanels import RegistryConfigletPanel
from plone.z3cform import layout
from zope import schema
from zope.component import adapter
from zope.interface import Interface


class IGridListingControlPanel(Interface):
    myfield_name = schema.TextLine(
        title=_(
            "This is an example field for this control panel",
        ),
        description=_(
            "",
        ),
        default="",
        required=False,
        readonly=False,
    )


class GridListingControlPanel(RegistryEditForm):
    schema = IGridListingControlPanel
    schema_prefix = "collective.gridlisting.grid_listing_control_panel"
    label = _("Grid Listing Control Panel")


GridListingControlPanelView = layout.wrap_form(
    GridListingControlPanel, ControlPanelFormWrapper
)


@adapter(Interface, ICollectiveGridlistingLayer)
class GridListingControlPanelConfigletPanel(RegistryConfigletPanel):
    """Control Panel endpoint"""

    schema = IGridListingControlPanel
    configlet_id = "grid_listing_control_panel-controlpanel"
    configlet_category_id = "Products"
    title = _("Grid Listing Control Panel")
    group = ""
    schema_prefix = "collective.gridlisting.grid_listing_control_panel"
