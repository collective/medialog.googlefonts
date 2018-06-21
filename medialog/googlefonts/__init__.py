from Products.CMFCore.FSFile import FSFile
from Products.CMFCore.DirectoryView import registerFileExtension
from Products.CMFCore.DirectoryView import registerMetaType
from zope.i18nmessageid import MessageFactory

messageFactory = MessageFactory('medialog.googlefonts')

registerFileExtension('ttf', FSFile)
registerFileExtension('svg', FSFile)
registerFileExtension('woff', FSFile)
registerFileExtension('eot', FSFile)
registerMetaType('File', FSFile)

def initialize(context):
    pass
