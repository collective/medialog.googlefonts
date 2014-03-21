from Products.CMFCore.utils import getToolByName

def uninstall(self, reinstall=False):
    if not reinstall:
        ps = getToolByName(self, 'portal_setup')
        ps.runAllImportStepsFromProfile('profile-medialog.googlefonts:uninstall')