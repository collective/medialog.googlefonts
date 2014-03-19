from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm


def format_font(font):
    return font.replace (" ", "+")

def FontsVocabulary(context): 
    fonts = ["Abel","Anonymous Pro", "Cabin", "Crafty Girls", "Droid Sans", "Droid Sans Mono", "Droid Serif", "Gruppo", "Inconsolata","Josefin Sans", "Josefin Slab", "Lekton", "Lobster", "News Cycle","PT Sans", "PT Serif","Syncopate", "Tangerine","Ubuntu", "Waiting for the Sunrise", "Vollkorn", "Yanone Kaffeesatz", "Abril Fatface", "Aclonica", "Allan", "Allerta", "Allerta Stencil", "Amaranth", "Annie Use Your Telescope", "Anton", "Architects Daughter", "Arimo", "Arvo", "Astloch", "Bangers", "Bentham", "Bevan", "Buda", "Calligraffitti", "Candal", "Cantarell", "Cardo", "Cherry Cream Soda", "Chewy", "Coda", "Coming Soon", "Copse", "Corben", "Cousine", "Covered By Your Grace", "Crimson Text", "Crushed", "Cuprum", "Damion", "Dancing Script", "Dawning of a New Day", "EB Garamond", "Expletus Sans", "Fontdiner Swanky", "Geo", "Goudy Bookletter 1911", "Homemade Apple", "IM Fell", "Indie Flower", "Irish Grover", "Just Another Hand", "Just Me Again Down Here", "Kenia", "Kranky", "Kreon", "Kristi", "Lato", "League Script", "Luckiest Guy", "Maiden Orange", "Meddon", "MedievalSharp", "Merriweather", "Michroma", "Miltonian", "Molengo", "Montserrat", "Mountains of Christmas", "Neucha", "Neuton", "Nobile", "Nova", "OFL Sorts Mill Goudy TT", "Old Standard TT", "Orbitron", "Oswald", "Over the Rainbow", "Pacifico by Vernon Adams ", "Pacifico", "Permanent Marker", "Philosopher", "Puritan", "Quattrocento", "Quattrocento Sans", "Radley by Vernon Adams", "Radley", "Raleway", "Reenie Beanie", "Rock Salt", "Schoolbell", "Six Caps", "Slackey", "Smythe", "Sniglet", "Special Elite", "Sue Ellen Francisco", "Sunshiney", "Swanky and Moo Moo", "Terminal Dosis Light", "The Girl Next Door", "Tinos", "UnifrakturMaguntia", "Unkempt", "VT323", "Vibur"]
    terms = [SimpleTerm(value=format_font(pair),
            token=format_font(pair),
            title=pair) for pair in fonts]
    return SimpleVocabulary(terms)
    
    
