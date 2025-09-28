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

    norena "You've created a new Ren'Py game."

    norena "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
