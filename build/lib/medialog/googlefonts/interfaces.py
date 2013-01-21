from zope.interface import Interface
from zope import schema
from zope.i18nmessageid import MessageFactory

_ = MessageFactory('medialog.googlefonts')

class IGooglefontsConfiguration(Interface):
    """This interface defines the configlet for Googlefonts."""
    
    googlefonts = schema.TextLine(title=_(u"googlefonts", default=u'Googlefonts on'),
                              description=_(u"googlefonts_on",
                              default=u'The divs or classes to put googlefont on.'),
                              required=True,
                              default="")
                              
    googlefontfamily = schema.Choice(title="Font", description=u"The Font that should be used. You can see preview of the fonts by going to http://yoursite.com/@@fontsheet", values=["Abel","Anonymous Pro", "Cabin", "Crafty Girls", "Droid Sans", "Droid Sans Mono", "Droid Serif", "Gruppo", "Inconsolata","Josefin Sans", "Josefin Slab", "Lekton", "Lobster", "News Cycle","PT Sans", "PT Serif","Syncopate", "Tangerine","Ubuntu", "Waiting for the Sunrise", "Vollkorn", "Yanone Kaffeesatz", "Abril Fatface", "Aclonica", "Allan", "Allerta", "Allerta Stencil", "Amaranth", "Annie Use Your Telescope", "Anton", "Architects Daughter", "Arimo", "Arvo", "Astloch", "Bangers", "Bentham", "Bevan", "Buda", "Calligraffitti", "Candal", "Cantarell", "Cardo", "Cherry Cream Soda", "Chewy", "Coda", "Coming Soon", "Copse", "Corben", "Cousine", "Covered By Your Grace", "Crimson Text", "Crushed", "Cuprum", "Damion", "Dancing Script", "Dawning of a New Day", "EB Garamond", "Expletus Sans", "Fontdiner Swanky", "Geo", "Goudy Bookletter 1911", "Homemade Apple", "IM Fell", "Indie Flower", "Irish Grover", "Just Another Hand", "Just Me Again Down Here", "Kenia", "Kranky", "Kreon", "Kristi", "Lato", "League Script", "Luckiest Guy", "Maiden Orange", "Meddon", "MedievalSharp", "Merriweather", "Michroma", "Miltonian", "Molengo", "Montserrat", "Mountains of Christmas", "Neucha", "Neuton", "Nobile", "Nova", "OFL Sorts Mill Goudy TT", "Old Standard TT", "Orbitron", "Oswald", "Over the Rainbow", "Pacifico by Vernon Adams ", "Pacifico", "Permanent Marker", "Philosopher", "Puritan", "Quattrocento", "Quattrocento Sans", "Radley by Vernon Adams", "Radley", "Raleway", "Reenie Beanie", "Rock Salt", "Schoolbell", "Six Caps", "Slackey", "Smythe", "Sniglet", "Special Elite", "Sue Ellen Francisco", "Sunshiney", "Swanky and Moo Moo", "Terminal Dosis Light", "The Girl Next Door", "Tinos", "UnifrakturMaguntia", "Unkempt", "VT323", "Vibur"], default=u'Yanone Kaffeesatz')


    googlefontfamilysize = schema.TextLine(title=_(u"label_googlefontfamily", default=u'Size of the font'),
                              description=_(u"help_googlefontfamily", default=u''),
                              required=False,
                              default="")                         

    googlefontcss = schema.TextLine(title=_(u"label_googlefontcss", default=u'Extra for css. No typos please....'),
                              description=_(u"help_googlefontcss", default=u''),
                              required=False,
                              default="")     

    extracss = schema.Text(title=_(u"label_extracss", default=u'Extra css. Include classes and divs. No typos please....'),
                              description=_(u"help_extracss", default=u''),
                              required=False)    

class IGooglefontsLayer(Interface):
    """
    marker interface for googlefont layer
    """
    pass