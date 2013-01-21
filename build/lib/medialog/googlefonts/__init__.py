from Products.CMFCore.FSFile import FSFile
from Products.CMFCore.DirectoryView import registerFileExtension
from Products.CMFCore.DirectoryView import registerMetaType

registerFileExtension('ttf', FSFile)
registerFileExtension('svg', FSFile)
registerFileExtension('woff', FSFile)
registerFileExtension('eot', FSFile)
registerMetaType('File', FSFile)