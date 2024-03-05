from plone.app.contenttypes.browser.collection import CollectionView
from plone.app.contenttypes.browser.folder import FolderView

try:
    from plone.app.standardtiles.contentlisting import ContentListingTile
    from plone.event.interfaces import IEvent
    from zope.component import getMultiAdapter
    from zope.contentprovider.interfaces import IContentProvider

    HAS_PAS = True
except ImportError:
    HAS_PAS = False


class FolderGridListing(FolderView):
    pass


class CollectionGridListing(CollectionView):
    pass


if HAS_PAS:
    class ContentlistingTileGridListing(ContentListingTile):
        def is_event(self, obj):
            if getattr(obj, "getObject", False):
                obj = obj.getObject()
            return IEvent.providedBy(obj)

        def formatted_date(self, item):
            provider = getMultiAdapter(
                (self.context, self.request, self), IContentProvider, name="formatted_date"
            )
            return provider(item)
