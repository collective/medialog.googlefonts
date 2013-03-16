from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName

class CSS(BrowserView):

    @property
    def googlefonts_properties(self):
        properties_tool = getToolByName(self.context, 'portal_properties')
        return getattr(properties_tool, 'googlefonts_properties', None)

    def __call__(self, request=None, response=None):
        """Returns global configuration for googlefonts taken from portal_properties.
        You can change these setting from the control panel"""
        self.request.response.setHeader("Content-type", "text/javascript")

        googlefontfamily = getattr(self.googlefonts_properties, 'googlefontfamily', '')
        googlefontfamilysize = getattr(self.googlefonts_properties, 'googlefontfamilysize', '')
        googlefontcss = getattr(self.googlefonts_properties, 'googlefontcss', '')
        extracss = getattr(self.googlefonts_properties, 'extracss', '')   
        
        return """\
%(googlefonts)s {
    font-family: '%(googlefontfamily)s', arial, serif !important; 
    font-size:    %(googlefontfamilysize)s !important;  
    %(googlefontcss)s;  
}
%(extracss)s      
""" % {
		'googlefonts'    : googlefonts,,
		'googlefontfamily'    : googlefontfamily,
		'googlefontfamilysize': googlefontfamilysize,
		'googlefontcss'       : googlefontcss,
		'extracss'     		  : extracss,
    }