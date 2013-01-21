from medialog.googlefonts.interfaces import IGooglefontsConfiguration
from Products.CMFCore.utils import getToolByName
from plone.app.controlpanel.form import ControlPanelForm
from Products.CMFCore.interfaces import IPropertiesTool
from Products.CMFDefault.formlib.schema import ProxyFieldProperty
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFPlone.interfaces import IPloneSiteRoot
from zope.component import adapts, getUtility
from zope.formlib.form import FormFields
from zope.i18nmessageid import MessageFactory
from zope.interface import implements

_ = MessageFactory('medialog.googlefonts')

class GooglefontsControlPanelAdapter(SchemaAdapterBase):
    adapts(IPloneSiteRoot)
    implements(IGooglefontsConfiguration)
    
    def __init__(self, context):
        super(GooglefontsControlPanelAdapter, self).__init__(context)
        self.context = getUtility(IPropertiesTool).googlefonts_properties

    googlefonts = ProxyFieldProperty(IGooglefontsConfiguration['googlefonts'])
    googlefontfamilysize = ProxyFieldProperty(IGooglefontsConfiguration['googlefontfamilysize'])
    googlefontfamily = ProxyFieldProperty(IGooglefontsConfiguration['googlefontfamily'])
    googlefontcss = ProxyFieldProperty(IGooglefontsConfiguration['googlefontcss'])
    extracss = ProxyFieldProperty(IGooglefontsConfiguration['extracss'])


class GooglefontsControlPanel(ControlPanelForm):
    form_fields = FormFields(IGooglefontsConfiguration)
    label = _(u"Googlefonts configuration.")
    description = _(u'Settings to configure googlefonts.')
    form_name = _(u'Googlefontssettings')
    def _on_save(self, data=None):
        jsregistry = getToolByName(self.context,
                                   'portal_javascripts')
        cssregistry = getToolByName(self.context,
                                   'portal_css')
        jsregistry.cookResources()
        cssregistry.cookResources()

