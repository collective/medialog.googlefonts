from zope.interface import Interface
from zope import schema
from medialog.googlefonts import messageFactory as _


from z3c.form import interfaces
from zope.interface import alsoProvides
from plone.directives import form
from medialog.controlpanel.interfaces import IMedialogControlpanelSettingsProvider


class IGooglefontsLayer(Interface):
    """ marker interface for googlefont layer """
    

class IGooglefontsSettings(form.Schema):
    """Adds googlefont settings to medialog.controlpanel """

    form.fieldset('googlefonts',
                  label=_(u'Googlefont Settings'),
                  fields=[ 'googlefontfamily',
                           'googlefonts',
                           'googlefontfamilysize', 
                           'googlefontcss', 
                           'extracss',
                           ]
    )

    googlefonts = schema.TextLine(title=_(u"googlefonts", default=u'Google Font on'), 
        description=_(u"googlefonts_on",
        default=u'The divs or classes to put the FIRST Google Fonts on.'),
        required=True,
    )

    googlefontfamily = schema.List(
        value_type=schema.Choice(vocabulary=
            "FontsVocabulary",
        ) ,
        required=True,
        min_length=1,
        title=_(u"label_googlefontfamily", default=u"Enable fonts"),
        description=_(u"help_googlefontfamily", default=u"Select fonts. Preview of fonts at <a href='@@fontsheet' target='_blank' >http://yoursite.com/@@fontsheet</a>"),
    )
   
    googlefontfamilysize = schema.TextLine(title=_(u"label_googlefontfamilysize", default=u'Size of the font'),
        description=_(u"help_googlefontfamilysize", default=u'Font Size for FIRST googlefont'),
        required=False,
        default=_("300%"),
    )

    googlefontcss = schema.Text(title=_(u"label_googlefontcss", default=u'CSS for FIRST Google Font. No typos please....'),
        description=_(u"help_googlefontcss", default=u''),
        required=False,
    )

    extracss = schema.Text(title=_(u"label_extracss", 
     default=u'Extra css. Include classes and divs. No typos please....'),
                           description=_(u"help_extracss",
                                         default=u"Example: #content .sometitle { font-family: \"My Font\", 'Times', 'Sans-Serif' !important; font-size: 300% !important; }"),
        required=False,
    )

    def _on_save(self, data=None):
        cssregistry = getToolByName(self.context, 'portal_css')
        cssregistry.cookResources()
    

alsoProvides(IGooglefontsSettings, IMedialogControlpanelSettingsProvider)


class IGooglefontsLayer(Interface):
    """ marker interface for googlefont layer """
