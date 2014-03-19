from plone.app.layout.viewlets.common import ViewletBase
from plone.memoize.instance import memoize


class GooglefontsHead(ViewletBase):    

    def fontproperties(self):
        """Returns  googlefonts taken from portal_properties."""
        
        return ''