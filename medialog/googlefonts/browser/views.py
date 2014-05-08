from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName

from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from ..interfaces import IGooglefontsSettings
from ..vocabularies import fonts

class Fontsheet(BrowserView):
    
    def settings(self):
        """Returns settings from  registry."""
        return getUtility(IRegistry).forInterface(IGooglefontsSettings)
    
    @property
    def fontfamily(self):
        """Returns  fontfamily taken from registry."""
        return self.settings().googlefontfamily or 'Times'
    
    @property
    def fontfamilies(self):
        """Returns  fontfamilies taken from registry."""
        return  fonts(self)
    
    @property
    def construct_url(self):
        """returns the urls that will be needed for getting the fonts from google 
            the url can not be too long, so we will have to split it up
          """
        size=30
        fontfamilies = fonts(self)
        groupedlist = [fontfamilies[i:i+size] for i  in range(0, len(fontfamilies), size)]
        
        fontlist = []
        
        for lists in groupedlist:
            url = 'http://fonts.googleapis.com/css?family=' +  ("|".join(str(font) for font in lists))
            url.replace(" ", "+")
            fontlist.append(url)
        
        return fontlist


class CSS(BrowserView):
    
    def settings(self):
        """Returns settings from  registry."""
        return getUtility(IRegistry).forInterface(IGooglefontsSettings)
    
    @property
    def fontfamily(self):
        """Returns  fontfamily taken from registry."""
        first_font =  self.settings().googlefontfamily[0]
        return first_font.replace("+", " ") or ' '
    
    @property
    def fonts(self):
        """Returns  fonts taken from registry."""
        return self.settings().googlefonts or ' '
    
    @property
    def fontssize(self):
        """Returns  fontsize taken from registry."""
        return self.settings().googlefontfamilysize or ' '
    
    
    @property
    def fontcss(self):
        """Returns  fontcss taken from registry."""
        return self.settings().googlefontcss or ' '
    
    @property
    def extracss(self):
        """Returns  extracss taken from registry."""
        return self.settings().extracss or ' '
    

    def __call__(self, request=None, response=None):
        """Returns settings from the control panel / registry"""
        self.request.response.setHeader("Content-type", "text/css")
        
        return """\
%(googlefonts)s {
    font-family: '%(googlefontfamily)s', arial, serif !important; 
    font-size:    %(googlefontfamilysize)s !important;  
    %(googlefontcss)s;  
}
%(extracss)s      
""" % {
		'googlefonts'    	  : self.fonts,
		'googlefontfamily'    : self.fontfamily,
		'googlefontfamilysize': self.fontssize,
		'googlefontcss'       : self.fontcss,
		'extracss'     		  : self.extracss,
    }
    
    
