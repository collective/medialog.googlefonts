from plone.app.layout.viewlets.common import ViewletBase
from plone.memoize.instance import memoize

from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from ..interfaces import IGooglefontsSettings

class GooglefontsHead(ViewletBase):
    
    def settings(self):
        """Returns settings from  registry."""
        return getUtility(IRegistry).forInterface(IGooglefontsSettings)
            
    @property
    def fontfamily(self):
        """Returns  fontfamily taken from registry."""
        return self.settings().googlefontfamily or 'Times'

    @property
    def construct_url(self):
        """returns the googleapis font url """
        url = 'http://fonts.googleapis.com/css?family=' +  ("|".join(str(font) for font in self.fontfamily))
        return url

    