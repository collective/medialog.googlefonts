from Products.CMFCore.utils import getToolByName
from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from medialog.googlefonts.interfaces import IGooglefontsSettings
from medialog.controlpanel.interfaces import IMedialogControlpanelSettingsProvider
from zope.interface import noLongerProvides, alsoProvides


def upgrade_to_21(context):
    
    properties_tool = getToolByName(context, 'portal_properties')
    googlefonts_properties = getattr(properties_tool, 'googlefonts_properties', None)


    #context.runImportStepFromProfile('profile-medialog.googlefonts:default', 'registry')
    context.runAllImportStepsFromProfile('profile-medialog.googlefonts:default')

    #registry = getUtility(IRegistry)
    registry = getUtility(IRegistry).forInterface(IGooglefontsSettings)


    #copy settings from properties to registry
    registry.googlefonts          = getattr(googlefonts_properties, 'googlefonts', 'h1').decode('ascii')
    registry.googlefontcss        = getattr(googlefonts_properties, 'googlefontcss', ' ').decode('ascii')
    registry.googlefontfamilysize = getattr(googlefonts_properties, '/Users/griegmedialog/.Trash/actionicons.xmlgooglefontfamilysize', '3em').decode('ascii')
    registry.extracss             = getattr(googlefonts_properties, 'extracss', ' ').decode('ascii')  
    googlefontfamily              = getattr(googlefonts_properties, 'googlefontfamily', 'Gruppo').replace(" ", "+").decode('ascii')
    registry.googlefontfamily     = googlefontfamily.split()
    
    #remove things we dont need any more
    context.runImportStepFromProfile('profile-medialog.googlefonts:uninstall', 'jsregistry')
    context.runImportStepFromProfile('profile-medialog.googlefonts:uninstall', 'controlpanel')
    context.runImportStepFromProfile('profile-medialog.googlefonts:uninstall', 'skins')
    #context.runImportStepFromProfile('profile-medialog.googlefonts:uninstall', 'actionicons')
    
    #leave properties in case something goes wrong
    #portal.portal_properties.manage_delObjects(['googlefonts_properties'])
    
    #cook javascript and css if site is not in debug mode
    portal_javascripts = getToolByName(context, 'portal_javascripts')
    portal_javascripts.cookResources()
    css = getToolByName(context, 'portal_css')
    css.cookResources()


def also_provides(context):
    """ add settings to control panel"""
    
    if context.readDataFile('medialog.subskins.install.txt') is None:
    # Not your add-ons install profile
        return
    
    alsoProvides(IGooglefontsSettings, IMedialogControlpanelSettingsProvider)


def no_longer_provides(context):
    """ remove settings from control panel"""
    
    if context.readDataFile('medialog.subskins.uninstall.txt') is None:
    # Not your add-ons uninstall profile
        return

    noLongerProvides(IGooglefontsSettings, IMedialogControlpanelSettingsProvider)

