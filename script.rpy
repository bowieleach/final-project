
define you = Character("You", color = "7dffd0")
define doll = Character("Doll")


label start:

    scene bg 1
    "A visual novel by Bowie Leach"

    play music "audio/music/ominous_droning.mp3" fadein 1.0 volume 0.5

    ""
    ""
    ""
    ""
    ""
    stop music

    ""
    show bg 3

    you "Woah."

    "You sit up, not knowing what woke you so suddenly."

    "It's quiet. Even the fan is off."

    you "I guess the sleep timer works..."

    you "What time is it?"

    "Glancing around your old room,"
    "you don't see your phone,"
    "and that alarm clock has been stuck at 4:03 for years."

    you "Maybe I left it downstairs.."
    
    label choice1:
    "Turn on the lights?"
    $ choice1_timespicked = 0
    menu:
        "I'm still tired.":
            $ choice1_timespicked = choice1_timespicked + 1
            jump choice1_a
        "I'm up now, no matter what time it is.":
            jump youre_up

    label choice1_a:
        if choice1_timespicked > 3:
            jump sleepEnding
        else:
            "."
            ".."
            "..."
            "...."
            "....."
            you "Sigh."
            you "I should just start my day"
            jump choice1
    
    label sleepEnding:
        you "zzzzz"
        return

    label youre_up:

        "You toggle the lightswitch,"

        play sound "audio/sound/lightswitch_on.mp3"
        
        "to no avail."

        play sound "audio/sound/lightswitch_off.mp3"
        you "Awesome."

        #play music "audio/music/ominous_droning.mp3" fadein 2.0 volume 0.01 fadeout 2.0

        you "I guess I'll come back here after I get my phone."

        menu:
            "Go find your phone.":
                jump goFindPhone
            "I don't need a light to get dressed":
                jump stayInRoom
    
    label stayInRoom:
        you "Now where is my bag..."
        menu:
            "To the right.":
                jump roomToTheRight
            "To the left.":
                jump roomToTheLeft
            "I'm just going straight forward.":
                jump roomStraightForward
    
    label roomToTheRight:
        play sound "audio/sound/fallingdown.mp3"
        you "Ow."
        you "I guess I do need a light."
        jump goFindPhone
    
    label roomToTheLeft:
        "You feel around for your bag."
        play sound "audio/sound/cup_breaking.mp3"
        you "..."
        you "I should get a light"
        jump goFindPhone
    
    label roomStraightForward:
        play sound "audio/sound/clatter_cathiss.mp3"
        you "Oh wow."
        # you "??"
        you "Oh my god."
        you "This feels excessive."
        you "..."
        you "..."
        you "..."
        you "This was a mistake."
        you "This feels like a joke that didn't quite land but 
        too much time was spent editing sounds together that it had to be included..."
        you "I don't even have a cat..."
        you "Wait-"
        play sound "audio/sound/rumaging.mp3"
        you "I forgot I had this!"
        show utilitytool
        "You now have a small utility tool. You can't see the flashlight in the free image, but trust me it's there."
        "You forget all about getting dressed and go to find a clock somewhere in the house."
 
    label goFindPhone:

        scene bg 4

        you "Okay phone, phone, phone."
        you "This hallway never looked {i}this{/i} creepy as a kid..."
        "Where are you searching first?"
        you "Hmm."

        label choiceHall:
            menu:
                "Go to the left":
                    jump hallLeft
                "Go to the right":
                    jump hallRight
        
    label hallLeft:
        show creepy_doll
        you "!!!"
        you "Oh my god that thing is so scary."
        "The doll is staring you down. Any longer and you feel like it will try to harm you."
        menu:
            "Continue down the hall.":
                jump hallLeftContinue
            "Turn back.":
                jump choiceHalls
            "Stare into the doll's eyes.":
                jump dollEyes

    label hallLeftContinue:
        hide creepy_doll
        ""

    label dollEyes:
        hide creepy_doll
        show creepy_doll close
        you "..."
        doll "..."
        you "...."
        doll "...."
        you "....."
        you "I can't do this anymore you win"
        doll "^__^"
        you "?? How did you say that outlou-"
        you ":0"


    label hallRight:
        ""

    #"find t"
    #menu:
        #"look left"

    scene

    # This ends the game.

    return
