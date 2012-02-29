from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from plone.memoize.instance import memoize
from Acquisition import aq_inner


class GooglefontsHead(ViewletBase):
    
    render = ViewPageTemplateFile('viewlet.pt')
    
    