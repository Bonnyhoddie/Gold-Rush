#characters
define mc = Character("[mcname]")
define viridianrose = Character("@viridianrose", color = "#8ce99a")
define percypiper = Character("@percypiper", color = "#d899be")
define BH = Character("Bonnyhoddie", color = "#ffc6e5")

#music

define P_theme = "audio/bgm/Mazit Music Loop.ogg"
define Aoi_theme = "audio/bgm/LandingPage Loop.ogg"
define Se_theme = "audio/bgm/Mexico Loop.ogg"
define T_theme = "audio/bgm/Mr Snarky Destructoid Loop.ogg"
define H_theme = "audio/bgm/8Bit Tragic Loop.ogg"
define F_theme = "audio/bgm/Of Far Different Nature - Dream Factory (CC-BY).ogg"
define S_theme = "audio/bgm/The Puzzle Loop.ogg"

#bg images
image old_mc_room = "Images/backgrounds/old mc room.png"
image Letter = "Images/Letter.png"
image fadeout ="Images/Fade-out.png"

#player name input code begins

default openedletter = False
default repliedtopp = False
default packed = False
default energy = 3

$renpy.music.set_volume (0.1, 0, 'music')

while True:

    if energy == 3:
        call day from _call_day
    elif energy == 0:
        call night from _call_night



transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

init: ### just setting variables in advance so there are no undefined variable problems
    $ timer_range = 0
    $ timer_jump = 0
    $ time = 0

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)]) 
        ### ^this code decreases variable time by 0.01 until time hits 0, at which point, the game jumps to label timer_jump (timer_jump is another variable that will be defined later)

    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve 
        # ^This is the timer bar.



label start:
    $ mcname = renpy.input("what is your name?", default = "Emerald")

    $ mcname = mcname.strip()

    if mcname == "":

        $mcname = "Emerald"
    
    if mcname == "Chari":

        BH "Hey, that's me!"

        jump start

    if mcname == "Bonnyhoddie":

        BH "Hey, that's me!"

        jump start         
        
    mc "Are you sure this is the name you want to use?"

    menu:

        "Yes.":
            jump scene_one

        "No, lemme change.":

            jump start

    label name_yes:

        $ menu_flag = True

        jump scene_one

    label name_no:

        $ menu_flag = False

        jump start

    label name_done:


#player name input code ends

# The game starts here.
label scene_one:

    play music "audio/bgm/1_Menu_Master.mp3" fadeout 1

    BH "Hi! I'm BonnyHoddie"
    BH "But you can also call me Chari!"
    BH "And welcome to Gold Rush!"
    BH "Before we begin the story, I'd like to tell you something."
    BH "Well, a few things, actually."
    BH "This game is a demo since I made this as a College project."
    BH "I also have no prior experience as a game developer."
    BH "So, while I can hope that there are no mistakes..."
    BH "It might not be the case and you may notice a game flaw or bug."
    BH "This game is also {color=#ffef9f}in development{/color}."
    BH "That means anything and everything can change."
    BH "From the backgrounds, all the way to the art style."
    BH "We will change everything except how characters act."
    BH "Unless we find their personalities to be too boring or similar, anyway."
    BH "Though expect that to be the case for some characters right now."
    BH "Because how you feel about the characters changes everything about your judgement of them."
    BH "Yes, that's right!"
    BH "Your judgements are important!"
    BH "Your opinions of characters matter a lot in deciding who wins..."
    BH "And who loses..."
    BH "Every so often in the game, there is a popularity poll."
    BH "You can find this {a=https://gold-rush-official.tumblr.com/}here{/a}."
    BH "The polls will last for a {color=#ffef9f}month or 2{/color}, depending on the amount of votes, and game development process."
    BH "And then we'll decide the winner and continue the story from there."
    BH "Once the game is finished, there will be no more polls and the game will be complete."
    BH "Everything that happens to a character and the winner is {color=#ffef9f}final{/color} after that point."
    BH "So if you like a certain character..."
    BH "... Well..."
    BH "Make sure they win!"
    BH "So..."
    BH "Are you ready, [mcname]?"
    BH "..."
    BH "You don't have to answer that."
    BH "I know you are."
    BH "So let's begin!"

    play music "audio/bgm/Friday Afternoon Loop.ogg" fadeout 1
    
    scene old_mc_room
    with Dissolve(.5)

    pause .5

    mc "hmm... That's odd."

    "I was just collecting the post that went through my letter box."

    show Letter

    "And now I'm wondering about this weird letter."

    hide Letter

    mc "It has my name on it..."
    mc "Well, of course it has my name, it's directed towards me, but..."
    mc "I don't know where this could be from."
    mc "..."
    mc "Maybe this is a prank from my family."
    
    "Only one way to find out."

    menu:

        "Open the letter.":
            jump choice1_yes

        "Yeah, no, let's not.":
            jump choice1_no

    label choice1_yes:

        $ menu_flag = True

        mc "Obviously you're gonna read a mysterious letter of mysterious origins."
        mc "You'd be dumb not to."
        mc "Who knows? Maybe it's actually a portal that'll suck me into a fantasy world and take me away from my boring life."
        
        "..."

        mc "No, that's dumb."
        
        "..."

        mc "Still wouldn't hurt to open it, though."

        "I slowly open the envelope, with some hesitance."
        
        show Letter

        

        "Dear [mcname],"

        "I, Alicanto, formally invite you to the very first season of our TV show!" 
        "You were one of the 11 lucky enough to be selected by us!"
        "So pack your things, and we will collect you in a few days to explain everything!"
        "Yours sincerely,
        Alicanto"
        "..."

        hide Letter
        
        play music "audio/bgm/vntrack04.mp3" fadeout 1

        mc "What the fuck?"

        "Well that explained absolutely nothing."
        "And no portal."
        "I think it's safe to say..."
        "That I have been officially pranked."
        "And by a dumb letter too."

        "Although..."
        "Maybe it's not a prank?"
        "I'll be getting my hopes up."
        "BUT..."
        "There's no harm in investigating, right?"

        $ openedletter = True

        menu:

            "Detective time!":
                jump choice2_yes

            "No thanks, I need to sleep.":
                jump choice2_no

        label choice2_yes:

                $ menu_flag = True

                mc "Alright, Alicanto, let's play investigator."

                "Let's start with the internet."

                scene fadeout
                with Dissolve(.5)

                pause .5

                play music "audio/bgm/Friday Afternoon Loop.ogg" fadeout 1

                scene old_mc_room
                with Dissolve(.5)

                pause .5

                "It felt like an hour passed, before..."

                mc "Oh! A lead!"

                "It was a tweeter post, so nothing much, but still a lead."

                mc "Let's see... A post from an account called 'Percy Piper'."

                mc "Hah, that's so silly."

                percypiper "I just got this in the mail today, inviting me to a TV show. It's kinda creepy. Anyone else get this?"

                "It wouldn't hurt to respond, right?"

                menu:

                    "Respond!":
                        jump choice3_yes

                    "No way.":
                        jump choice3_no

                label choice3_yes:

                    $ menu_flag = True

                    "Yeah, let's do it. Why not?"

                    mc "Yeah, I got this too. I originally thought it was a prank, but, seems not now."

                    "..."
                    "Ooh! A response already!"

                    percypiper "Glad to know I'm not the only one who got this!" 
                    percypiper "I tried looking into it, but I got nothing..." 
                    percypiper "Even if this is just a scam, it's very worrying."

                    "Yeah, it is. Especially with the threat of being kidnapped."
                    "And them knowing our addresses."
                    "..."
                    "I just felt a chill go down my spine."
                    "..."

                    $ repliedtopp = True

                    jump choice1_done

                label choice3_no:

                    $ menu_flag = False

                    "Nah, It's getting late. I need to sleep, and replying won't make me learn anything new."

                    $ repliedtopp = False

                    jump choice1_done 

        label choice2_no:

                $ menu_flag = False

                mc "I'm not even going to entertain that dumb thought." 
                mc "It's CLEARLY just a prank."

                $ repliedtopp = False

                jump choice1_done

    label choice1_no:

        $ menu_flag = False

        "Yeah... No... Let's not... You don't know anything about this letter or where it came from."
        "I mean, it could have anything inside... Though, it does just look like a normal and perfectly safe letter."

        $ openedletter = False
        $ repliedtopp = False

        jump choice1_done

    label choice1_done:

        # ... the game continues here.
 
    "It's been a long day... Let's just sleep..."

    scene fadeout
    with Dissolve(.5)
    
    pause .5


jump ch02
