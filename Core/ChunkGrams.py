# Chunking Grammar

# Switching ChunkGram [Controlling devices On/Off]

switchGram = r"""

# A grammar for the pattern [Switch/Turn on/off the device in the place]
               
        chunk:
        {<DT><NN>+<VBG>|<DT><NN>+}
        }<DT>{
       
        chunk:
        {<NN><IN><DT>}
        }<NN>{
        }<DT>{
       
        chunk:
        {<RP>}
               
"""

# Controlling Temperature

tempGram = r"""
            
        chunk:
        {<VB><DT><NN><TO><CD><IN><DT><NN>+}
        }<VB>{
        }<DT>{
        }<TO>{
        }<IN>{
            
"""

# Elevator Calling

elevGram = r"""
            
        chunk:
        {<VB><DT><NN>}
        }<VB>{
        }<DT>{
            
"""

# Weather Query

weatherGram = r"""
            
        chunk:
        {<WP><VBZ><DT><NN><NN><IN><NN|NP>+}
        }<WP>{
        }<VBZ>{
        }<DT>{
        }<IN>{
        <NN>}{<NN>
            
"""