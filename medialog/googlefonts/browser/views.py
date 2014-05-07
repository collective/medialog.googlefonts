from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName

from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from ..interfaces import IGooglefontsSettings

class Fontsheet(BrowserView):
    
    def settings(self):
        """Returns settings from  registry."""
        return getUtility(IRegistry).forInterface(IGooglefontsSettings)
    
    @property
    def googlefontfamily(self):
        """Returns  fontfamilies taken from registry."""
        return  self.settings().googlefontfamily
    

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
    
    
