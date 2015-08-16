#-----------------------------
# Trader
#-----------------------------
init 1: 
    $crt_trader = GameCharacter("Denmar", "Gildclaw", "trader", Character("crt_trader.name", dynamic = True, color = "#5ca75c"), "characters/trader.png", False, True, "traderTN.png")
    $crt_trader.addPreference(CharacterPreference("art", True, "This is truely delightful!"))
    $crt_trader.addPreference(CharacterPreference("gold", True, "Oh my, my, my. Yes, yes, gold... "))
    $crt_trader.addPreference(CharacterPreference("peace", True, "Ah, this is so nice."))
    $crt_trader.addPreference(CharacterPreference("dirt", False, "This is a bit too grimy..."))
    $crt_trader.addPreference(CharacterPreference("action", False, "Thats too much for me I'm afrade."))
    $crt_trader.addPreference(CharacterPreference("scary", False, "That is too scary, I don't like it!"))
    define t = crt_trader.c
    
    # Special topics
    $crt_trader.addTopic(Topic("repeat", "repeat"))
    $crt_trader.addTopic(Topic("late", "late"))
    
    # Regualr topics
    $crt_trader.addTopic(Topic("How are you doing?", "howYouDoing", False))
    $crt_trader.addTopic(Topic("Do you like this place?", "thisPlace", False))
    $crt_trader.addTopic(Topic("What are you into?", "whatInto", False))
    
label trader_howYouDoing: 
    t "I-I'm ok I think."
    t "Th-Thanks for a-asking."
    t "How are y-you doing may I a-ask?"
    
    menu: 
        "I'm doing fine. Thanks for asking.": 
            t "That is w-wonderful to h-hear"
            
        "Not so good really.": 
            "Oh d-dear. I-I really am s-sorry, I h-hope I-I am not the c-cause of your ill f-feelings."
            
    return
            
label trader_thisPlace:
    
    # Allow the player to talk about the new place
    
    # A loved place
    if game.currentLocation.name == "Tent": 
        t "Th-This truley is a marvel to behold."
        t "From the incense in the air to the exotic trophies on display; this truely is a wonder to behold."
        $crt_trader.addRP(5)
        
        return
        
    # A hated place
    if game.currentLocation.name == "Arena":
        t "Th-This i-is a place o-of decay a-and dispare."
        t "I-I do not feel at all c-comfortable in a s-setting such as th-this."
        t "I-Is that somebodies b-b-blood over there?"
        $crt_trader.addRP(-5)
        
        return
    
    # Everything else
    t "I c-can't comment r-really."
    
    return
    
label trader_whatInto: 
    t "I-I am interested in ge-geniology, and economics, apand fine jewelery."
    
    return
    
label trader_repeat:
    t "Y-you d-didn't hear m-me the first t-time I guess."
    
label trader_late:
    t "I r-really h-have to g-go now, T-Temesh wants us to s-study trade tarrifs t-tomorrow."