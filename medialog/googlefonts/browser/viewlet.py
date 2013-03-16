from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from plone.memoize.instance import memoize
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName


class GooglefontsHead(ViewletBase):    
    render = ViewPageTemplateFile('viewlet.pt')

    def fontproperties(self):
        """Returns global configuration for googlefonts taken from portal_properties."""
        
        properties_tool = getToolByName(self.context, 'portal_properties')
        return getattr(properties_tool, 'googlefonts_properties', None)        
        googlefontfamily = getattr(self.googlefonts_properties, 'googlefontfamily', '')

        return """\
WebFontConfig = {
	google: { families: [ '%(googlefontfamily)s' ] }
};
(function() {
	var wf = document.createElement('script');
	wf.src = ('https:' == document.location.protocol ? 'https' : 'http') +
		'://ajax.googleapis.com/ajax/libs/webfont/1/webfont.js';
	wf.type = 'text/javascript';
	wf.async = 'true';
	var s = document.getElementsByTagName('script')[0];
	s.parentNode.insertBefore(wf, s);
})();
""" % {
		'googlefontfamily':googlefontfamily,
    }
