# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define void = Character("???")
define norena = Character("Norena (You)")
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

    norena "I knew Seren was offered a chance to get out of this decrepit city. And I pretended I didn't. Of course she's stay if i asked. But is that fair?"

    norena "And Billiam...I should've let him rest, shouldn't have pushed him. It's my fault he lost his voice that night. The pollution from staying in this city only worsened it."

    norena "I know I have to let them go this time. There are more important things than a silly band competition"
    norena "I should've known that back then"
    norena "Should've known that making others sacrifices their futures for my present..even if I didn't mean to...It's not right"
    norena "We lost each other in the end, anyways"
    # This ends the game.

    return
