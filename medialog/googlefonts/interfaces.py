from zope.interface import Interface
from zope import schema
from zope.i18nmessageid import MessageFactory


_ = MessageFactory('medialog.googlefonts')

class IGooglefontsConfiguration(Interface):
  """This interface defines the configlet for Googlefonts."""

  googlefonts = schema.ASCIILine(title=_(u"googlefonts", default=u'Googlefonts on'),
                              description=_(u"googlefonts_on",
                                            default=u'The divs or classes to put googlefont on.'),
                              required=True,
                              default="")
                              
  googlefontfamily = schema.Choice(title=u"Font", description=u"The Font that should be used. You can see preview of the fonts by going to http://yoursite.com/@@fontsheet", values=["Abel", "Abril Fatface", "Aclonica", "Allan", "Allerta", "Allerta Stencil", "Amaranth", "Annie Use Your Telescope", "Anonymous Pro", "Anton", "Architects Daughter", "Arimo", "Arvo", "Astloch", "Bangers", "Bentham", "Bevan", "Buda", "Cabin", "Calligraffitti", "Candal", "Cantarell", "Cardo", "Cherry Cream Soda", "Chewy", "Coda", "Coming Soon", "Copse", "Corben", "Cousine", "Covered By Your Grace", "Crafty Girls", "Crimson Text", "Crushed", "Cuprum", "Damion", "Dancing Script", "Dawning of a New Day", "Droid Sans", "Droid Sans Mono", "Droid Serif", "EB Garamond", "Expletus Sans", "Fontdiner Swanky", "Geo", "Goudy Bookletter 1911", "Gruppo", "Homemade Apple", "IM Fell", "Inconsolata", "Indie Flower", "Irish Grover", "Josefin Sans", "Josefin Slab", "Just Another Hand", "Just Me Again Down Here", "Kenia", "Kranky", "Kreon", "Kristi", "Lato", "League Script", "Lekton", "Lobster", "Luckiest Guy", "Maiden Orange", "Meddon", "MedievalSharp", "Merriweather", "Michroma", "Miltonian", "Molengo", "Montserrat", "Mountains of Christmas", "Neucha", "Neuton", "News Cycle", "Nobile", "Nova", "OFL Sorts Mill Goudy TT", "Old Standard TT", "Orbitron", "Oswald", "Over the Rainbow", "PT Sans", "PT Serif", "Pacifico by Vernon Adams ", "Pacifico", "Permanent Marker", "Philosopher", "Puritan", "Quattrocento", "Quattrocento Sans", "Radley by Vernon Adams ", "Radley", "Raleway", "Reenie Beanie", "Rock Salt", "Schoolbell", "Six Caps", "Slackey", "Smythe", "Sniglet", "Special Elite", "Sue Ellen Francisco", "Sunshiney", "Swanky and Moo Moo", "Syncopate", "Tangerine", "Terminal Dosis Light", "The Girl Next Door", "Tinos", "Ubuntu", "UnifrakturMaguntia", "Unkempt", "VT323", "Vibur", "Vollkorn", "Waiting for the Sunrise", "Wallpoet", "Walter Turncoat", "Yanone Kaffeesatz"], default='Yanone Kaffeesatz')

  googlefontfamilysize = schema.ASCIILine(title=_(u"label_googlefontfamily", default=u'Size of the font'),
                              description=_(u"help_googlefontfamily", default=u''),
                              required=False,
                              default="")                         

  googlefontcss = schema.ASCIILine(title=_(u"label_googlefontcss", default=u'Extra for css. No typos please....'),
                              description=_(u"help_googlefontcss", default=u''),
                              required=False,
                              default="")     

  extracss = schema.ASCII(title=_(u"label_extracss", default=u'Extra css. Include classes and divs. No typos please....'),
                              description=_(u"help_extracss", default=u''),
                              required=False)    

class IGooglefontsLayer(Interface):
    """
    marker interface for googlefont layer
    """