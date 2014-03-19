from zope.interface import Interface
from zope import schema
from zope.i18nmessageid import MessageFactory


from z3c.form import interfaces
from zope.interface import alsoProvides
from plone.directives import form
from medialog.controlpanel.interfaces import IMedialogControlpanelSettingsProvider


_ = MessageFactory('medialog.googlefonts')

class IGooglefontsLayer(Interface):
    """ marker interface for googlefont layer """
    

class IGooglefontsSettings(form.Schema):
    """Adds googlefont settings to medialog.controlpanel """
    
    form.fieldset('googlefonts',
                  label=_(u'Googlefont Settings'),
                  fields=['googlefonts',
                           'googlefontfamily', 
                           'googlefontfamilysize', 
                           'googlefontcss', 
                           'extracss',
                           ]
    )

    googlefonts = schema.TextLine(title=_(u"googlefonts", default=u'Googlefonts on'), 
        description=_(u"googlefonts_on",
        default=u'The divs or classes to put googlefont on.'),
        required=True,
    )

    googlefontfamily = schema.Choice(title=u"Font", 
        description=u"Fontname. Preview of fonts at http://yoursite.com/@@fontsheet",
        vocabulary="medialog.googlefonts.fonts",
    )
   
    googlefontfamilysize = schema.TextLine(title=_(u"label_googlefontfamily", default=u'Size of the font'),
        description=_(u"help_googlefontfamilysizs", default=u'Font Size'),
        required=False,
        default=_("300%"),
    )

    googlefontcss = schema.TextLine(title=_(u"label_googlefontcss", default=u'Extra for css. No typos please....'),
        description=_(u"help_googlefontcss", default=u''),
        required=False,
    )

    extracss = schema.TextLine(title=_(u"label_extracss", 
     default=u'Extra css. Include classes and divs. No typos please....'),
        description=_(u"help_extracss", default=u''),
        required=False,
    )

    def _on_save(self, data=None):
        cssregistry = getToolByName(self.context, 'portal_css')
        cssregistry.cookResources()
    

alsoProvides(IGooglefontsSettings, IMedialogControlpanelSettingsProvider)


class IGooglefontsLayer(Interface):
    """ marker interface for googlefont layer """
    