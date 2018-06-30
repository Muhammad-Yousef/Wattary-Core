from nltk import CFG



greeting = CFG.fromstring("""

    S -> NN
    NN -> "Hello" | "Hi" | "Howdy" | "Hey"

""")

statusQuery = CFG.fromstring("""

    S -> PRP VBP JJ
    PRP -> "I"
    VBP -> "am"
    JJ -> "good" | "fine" | "ok"
    
    S -> NN VBZ VB RB R
    NN -> "Everything"
    VBZ -> "is"
    VB -> "going"
    RB -> "extremely"
    R -> "well"
    
    S -> PR NND CC DD NNS VbP J
    PR -> "My"
    NND -> "logic"
    CC -> "and"
    DD -> "cognitive"
    NNS -> "functions"
    VbP -> "are"
    J -> "Normal" | "working well"
    
    S -> P VBZ DT JJJ
    P -> "It"
    VBZ -> "is"
    DT -> "all"
    JJJ -> "good"
    
    S -> W
    W -> "Good" | "Fine"

""")

nameQuery = CFG.fromstring("""

    S -> PRP NN VBZ JJ
    PRP -> "My"
    NN -> "name"
    VBZ -> "is"
    JJ -> "Wattary"
    
    S -> P VBP JJ
    P -> "I"
    VBP -> "am"
    JJ -> "Wattary"
    
    S -> PR VBZ JJ
    PR -> "It"
    VBZ -> "is"
    JJ -> "Wattary"
    
    S -> "Wattary"

""")

disability = CFG.fromstring("""

    S -> NNP PRP MD RB VB IN
    NNP -> "Sorry"
    PRP -> "I"
    MD -> "can"
    RB -> "not"
    VB -> "do"
    IN -> "that"
    
    
""")


lightOn = CFG.fromstring("""

    S -> PRP VBP VBN RP DT NN
    PRP -> 'I'
    VBP -> 'have'
    VBN -> 'turned' | 'switched'
    RP -> 'on'
    DT -> 'the'
    NN -> 'light'

    S -> PR VBD P
    PR -> "You"
    VBD -> "got"
    P -> "it"

    S -> W
    W -> "Done" | "OK" | "All right"

""")

lightOff = CFG.fromstring("""

    S -> PRP VBP VBN RP DT NN
    PRP -> 'I'
    VBP -> 'have'
    VBN -> 'turned' | 'switched'
    RP -> 'off'
    DT -> 'the'
    NN -> 'light'
    
    S -> PR VBD P
    PR -> "You"
    VBD -> "got"
    P -> "it"
    
    S -> W
    W -> "Done" | "OK" | "All right"

""")

oneWord = CFG.fromstring("""
    
    S -> PRP VBD P
    PRP -> "You"
    VBD -> "got"
    P -> "it"
    
    S -> NNP NN
    NNP -> "Ok"
    NN -> "Man"
    
    S -> W
    W -> "Done" | "OK" | "All right"

""")

pastSimpleQuery = CFG.fromstring("""

    S -> UH PRP VBD
    UH -> "Yes"
    PRP -> "I"
    VBD -> "did"

    S -> W
    W -> "Yeah" | "Yes" | "Yup"

""")

presentPerfectQuery = CFG.fromstring("""

    S -> UH PRP VBP
    UH -> "Yes"
    PRP -> "I"
    VBP -> "Have"

    S -> W
    W -> "Yeah" | "Yes" | "Yup"

""")

elevatorCalling = CFG.fromstring("""

    S -> NN VBZ VBG RB
    NN -> "Elevator" | "It"
    VBZ -> "is"
    VBG -> "coming"
    RB -> "now"

""")

