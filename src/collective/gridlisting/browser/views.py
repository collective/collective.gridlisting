from Acquisition import aq_inner
from plone import api
from plone.app.contenttypes.browser.collection import CollectionView
from plone.app.contenttypes.browser.folder import FolderView
from plone.dexterity.browser.view import DefaultView


class GridListingBase(DefaultView):

    def get_default(self, attr):
        context = aq_inner(self.context)
        val = getattr(context, attr, None)
        if val is None:
            if attr in self.w:
                # return widgets default attribute adapter
                return self.w[attr].value
            return
        return val

    @property
    def show_about(self):
        # use registry setting even if not anonymous
        return api.portal.get_registry_record(
            "plone.allow_anon_views_about", default=False
        )


class FolderGridListing(GridListingBase, FolderView):
    pass


class CollectionGridListing(GridListingBase, CollectionView):
    pass
