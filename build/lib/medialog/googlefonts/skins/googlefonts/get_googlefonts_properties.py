## Script (Python) "get_googlefonts_properties"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
from Products.CMFCore.utils import getToolByName

googlefonts_properties = getToolByName(context, 'portal_properties').googlefonts_properties  
return googlefonts_properties 