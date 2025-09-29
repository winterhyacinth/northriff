# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define void = Character("???")
define norena = Character("Norena (You)")
define seren = Character("Seren")

image seren happy = "seren happy.png"
image seren sad = "seren sad.png"
image seren talk = "seren talk.png"
image bg club = "bg club.png"
image norena neutral2 = "norena neutral2.png"
# The game starts here.

label start:
    scene black with fade

    void "You've lived this once before, haven't you?"
    void "This time you don't get to look away"
    void "Billiam Bart gave his voice. Seren gave her future." 
    void "You? You gave nothing but excuses. Time isn't a mirror. Look into it. And fix what you've done."
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg club

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show norena neutral2 at center

    # These display lines of dialogue.

    norena "....."

    norena "I knew Seren was offered a chance to get out of this decrepit city with that record deal. And I pretended I didn't, because I didn't want our group to fall apart. Of course she's stay if i asked. But is that fair?"

    norena "And Billiam...I should've let him rest, shouldn't have pushed him. It's my fault he lost his voice that night. The pollution from staying in this city only worsened it."

    norena "I know I have to let them go this time. There are more important things than a silly band competition"
    norena "I should've known that back then"
    norena "Should've known that making others sacrifices their futures for my present..even if I didn't mean to...It's not right"
    norena "We lost each other in the end, anyways"
    # This ends the game.

    show norena neutral2 at left
    show seren talk at right
    seren "North! Are you ready for our gig tonight? Vera and I were just fixing our guitars."
    show seren happy at right
    norena "Oh yeah, but can I talk to you about something real quick?"

    menu:
        "stay silent": 
            jump silent
        "tell her you know about the offer and ask her to stay":
            jump stay
        "tell her you know and encourage her to accept it":
            jump encourage
    return
    

label stay:
    scene bg club
    show norena neutral2 at left
    show seren happy at right
    norena"I heard about the agent coming to see you tonight. Your voice and guitar skills are some of the best I've heard, it's nice you gained you some recognition.
    show seren sad at right
    seren "Yeah...but I don't know what to do. I can't leave this place; We all grew up here. I want to watch our band bloom."
    norena "Stay. Please. You can grow here, who cares about all that fancy stuff? If you leave, the band will break up."
    seren "Mhm...I suppose it would be easier to stay. But, for now, I have to go get ready for our gig tonight. I think we have many more in our future. Together."
    hide seren with dissolve
    void "Why are you so eager to sacrifice everyone but yourself?"
    jump nextScene
    return

label silent:
    scene bg club
    show norena neutral2 at left
    show seren happy at right
    norena "...actually, I forgot what I was going to say"
    seren "Fair enough! I'll see you later at our last practice."
    hide seren with dissolve
    void "You stay silent. You fail to change."
    jump nextScene

    return

label encourage:
    scene bg club
    show norena neutral2 at left
    show seren happy at right
    norena "I heard about the deal you got. You should take it."
    show seren talk at right
    seren "Oh..the record deal? It's not going to happen anyways. I don't want to get my hopes up. Plus, I can't leave this place"
    show seren happy at right
    norena "Anyone with the chance to get out of this city should take it"
    norena "You know what? Since that agent's coming tonight to hear our gig-"
    norena "Let's rewrite it, our act. You should be the lead singer this time. Vera always gets that role. You can impress them, then."
    show seren talk at right 
    seren"Oh, really? Thank you. I don't know what decision I'll make"
    show seren sad at right
    seren "But thank you, really. I was scared about telling you guys. Leaving this place...we grew up here together."
    seren "I should go now."
    hide seren with dissolve
    void "Do you think your actions will change what already happened? Tonight is bound to go terrible."
    norena "Isn't that the whole point of this? To change it?"
    jump nextScene

    return

label nextScene:
    scene bg club
    show norena neutral2
    return