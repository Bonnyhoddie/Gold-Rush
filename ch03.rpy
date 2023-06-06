#characters
define mc = Character("[mcname]")
define u = Character("Unknown")
define hk1 = Character("Maid", color = "#FFFFFF")
define hk2 = Character("Butler", color = "#FFFFFF")
 

#bg images
image fadeout = "Images/Fade-out.png"
image flashback = "Images/Flashback.png"
image Alicanto:

    "Images/backgrounds/Alicanto 1.png"
    pause .3
    "Images/backgrounds/Alicanto 2.png"
    pause .3
    "Images/backgrounds/Alicanto 3.png"
    pause .3
    repeat 

image mcroom = "images/backgrounds/new mc room.jpg"
image mcbalcony = "Images/backgrounds/Balcony.jpg"
image FMaid_smile = "Images/FMaid Smiling.png"
image FMaid_neutral = "Images/FMaid neutral.png"
image FMaid_annoyed = "Images/Maid annoyed.png"
image FMaid_surprised = "Images/Maid surprise.png"
image FMaid_nervous = "Images/Maid nervous.png"
image Butler_serious1 = "Images/Tabby Maid.png"
image Butler_serious2 = "Images/Tabby Maid2.png"
image Butler_annoyed = "Images/Tabby Maid annoyed.png"

#sfx

define thud = "audio/sfx/muffled-sound-of-falling-game-character-131797.mp3"
define punch = "audio/sfx/punch-140236.mp3"

#defaults

default investigated = False

#player name input code begins

label ch03:

    $ attackedmaid = False
    $ grabbed_a_weapon = False
 
    scene fadeout

    pause 1.5
 
    scene Alicanto
    with Dissolve(1.5)

    play music "audio/bgm/3_Night_1_Master.mp3" fadeout 1

    "What..."
    "What is that?"
    "It's a bird obviously, but..."
    "Why's it..."
    "... Glowing..."
    "..."
    "I feel like it..."
    "..."
    "..."
    "..."
    mc "...Ok..."
    mc "I'll follow you."

    scene fadeout
    with Dissolve(1.5)

    pause 2.5

    scene mcroom
    with Dissolve(1.5)

    play music "audio/bgm/Friday Afternoon Loop.ogg" fadeout 1

    mc "Uhhhh..."
    "What a weird..."

    play music "audio/bgm/Purple Black Loop.ogg" fadeout 1

    mc "WHUH?!" with hpunch 
    "WHAAAAT THE FUCK."
    "-oh! Got up too fast..."
    mc "This isn't my room."
    "Yeah, no SHIT Sherlock!"
    "How the fuck did I get here?!"
    "..."
    "... Ok..."
    "Let's take a deep breath here..."
    "..."
    "..."
    "Fuck, it's not working."
    "Lesson learned: Don't follow glowing birds in your dreams."
    "Or you get kidnapped."
    "Though..."
    "This room is pretty nice."
    "I could never afford this."
    "They must be pretty rich."
    "So I'm definitely not being held for ransom."
    "And this bed is pretty comfy."
    "Especially compared to mine."
    "And there are no restraints stopping me from leaving."
    "It doesn't seem like my life is in danger yet."
    "Maybe it's just once I leave this room."
    "So maybe it's not too bad..."
    "..."
    "For now, anyway..."

menu:

    "Yeah, let's just relax...":
        jump choice7_yes
    "No, I need to know how I got here.":
        jump choice7_no

label choice7_yes:
        
    $ menu_flag = True

    play music "audio/bgm/Friday Afternoon loop.ogg" fadeout 1

    "Yeah... That's right..."
    "I'm not in any danger right now."
    "So I can relax..."
    "Who knows? Maybe I'm still dreaming..."
    "And I'll wake up in my bedroom like normal."

    scene fadeout
    with Dissolve(1.5)

    pause 1.5

    scene mcroom
    with Dissolve(1.5)

    "I fell asleep..."
    "..."

    play music "audio/bgm/Of Far Different Nature - Largo (CC-BY).ogg" fadeout 1

    "AND I'M STILL HERE."
    "This is real."
    "I've been kidnapped."
    "I'm gonna die."
    "Or maybe not?"
    "No!"
    "Nobody kidnaps you and then let's you live to tell the tale!"

    jump choice7_done

label choice7_no:
        
    $ menu_flag = False
    $ investigated = True

    "NO!"
    "I will not be tempted by a comfy bed!"
    "Out I go!"

    play sound "audio/sfx/muffled-sound-of-falling-game-character-131797.mp3"

    "Oof!" with hpunch
    "..."
    "... Ok..."
    "... Maybe actually rolling out of it was a bit dramatic..."
    "But that was oddly grounding..." 
    "And now I can investigate."

    mc "Let's see... Let's see..."
    "Oh! Maybe a window I can escape from!"
    "Let's get these curtains open!"

    scene mcbalcony
    with Dissolve(.5)

    pause .5

    mc "Oh..."
    "... Nevermind it's just a balcony..."
    "God what is it with this kidnapper and subtly bragging about their wealth?"
    "It's actually kind of annoying."

    scene mcroom
    with Dissolve(.5)

    pause .5

    "Is there seriously nothing here that can help me know where I am?"
    "..."
    "..."
    "..."

    if packed:

        "Oh!" with hpunch
        "That's it!"
        "My phone will tell me!"
        "And then I can call the police!"
        "Oh, hey, and there's my suitcase!"
        "I wonder why they took it..."
        "..."
        "... Oh..."
        "... Nevermind..."
        "... It's not in here..."
        "None of my electronics are."
        "I really shouldn't have just packed clothes."
        "Though, since they wouldn't want their locations to be known."
        "They'd probably check our cases anyway."
        "Ew, somebody probably checked my suitcase..."

    else:

        "ugh, I wish I brought my stuff with me..."

    jump choice7_done
    
label choice7_done:
    # ... the game continues here.

    play sound "audio/sfx/person-knocking-18474.mp3"
    play music "audio/bgm/Of Far Different Nature - Largo (CC-BY).ogg" fadeout 1

    "{i}KNOCK KNOCK{/i}"

    "..."
    "Well shit."
    "This is where I die."
    "... Or not?"

    jump options1

label options1:

    $ time = 5                                     ### set variable time to 3
    $ timer_range = 5                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
    $ timer_jump = 'choice8_silent'                ### set where you want to jump once the timer runs out
    show screen countdown                          ### call and start the timer
        
    menu:
        "Grab a weapon.":
            hide screen countdown                  ### stop the timer
            jump choice8_weapon
            
        "Who's there?":
            hide screen countdown                  ### stop the timer
            jump choice8_Whothere


    label choice8_weapon:

        "That's right."
        "I can attack them before they attack ME!"
        "But all there is..."
        "... Is a lamp..."
        "OK!"
        "IT'LL BE FINE!"
        "Just gotta hope they don't have anything crazy."
        "Like a knife."
        "Or a gun."
        "Or insane martial arts skills."

        $ grabbed_a_weapon = True

        jump choice8_done

    label choice8_Whothere:

        "Ok, no problem."
        "I'll just ask who's there."
        "And then worry later."

        mc "Who's there?"

        "God, I sounded like a wimp."

        hk1 "Housekeeping, mx. [mcname]."

        $ grabbed_a_weapon = False

        jump choice8_done


    label choice8_silent:

        "Don't speak."
        "Don't move."
        "I don't exist."
        "Move on."

        play sound "audio/sfx/person-knocking-18474.mp3"

        "{i}KNOCK KNOCK.{/i}"
        
        u "Mx. [mcname]?"

        $ grabbed_a_weapon = False
            
        jump choice8_done

    
label choice8_done:

    play sound "audio/sfx/dorm-door-opening-6038.mp3"

    play music "audio/bgm/Calm Loop.ogg" fadeout 1
        
    "The door opened. And a woman entered the room."

    show FMaid_smile at center, bounce

    hk1 "Greetings, Mx. [mcname]."

    menu:
        
        "Where am I?":
            jump choice9_where
        "Who are you?":
            jump choice9_who
        "Attack her!" if grabbed_a_weapon:
            jump choice9_weapon

    label choice9_weapon:

        hide FMaid_smile
        show FMaid_surprised at center, bounce

        play music "audio/bgm/Of Far Different Nature - Largo (CC-BY).ogg" fadeout 1
        
        
        scene fadeout
        with Dissolve(1.5)

        hide FMaid_surprised

        play sound "audio/sfx/punch-140236.mp3"
        
        mc "AAAH!" with hpunch
        
        "... Ah?"

        scene mcroom
        with Dissolve(1.5)

        "Did she just..."
        "CATCH THE LAMP?!"
        "SHIT."
        "I'm dead."
        "This is my last day on Earth."
        "If this even is Earth."
        
        "..."

        play music "audio/bgm/Calm Loop.ogg" fadeout 1

        show FMaid_smile at center, bounce

        hk1 "Great attempt, Mx. [mcname]!"
        hk1 "However, let us... NOT do that again, alright?"
        hk1 "After all, I doubt Sir Alicanto would enjoy knowing that you destroyed his lamp."
        
        hide FMaid_smile
        show FMaid_nervous at center, bounce

        hk1 "Or anything of his."

        mc "... Huh...?"

        "What the fuck?"
        "What ungodly power does this maid HAVE?"
        "Even if it IS just a lamp..."
        "... Those reflexes..."
        "And then elegance."
        "..."
        "So scary..."

        $ attackedmaid = True

        jump choice9_where

    label choice9_where:

        play music "audio/bgm/Calm Loop.ogg" fadeout 1

        mc "Where am I?"

        hide FMaid_smile
        hide FMaid_nervous
        show FMaid_neutral at center, bounce

        hk1 "Good to know you're finally awake."
      
        hide FMaid_neutral
        show FMaid_smile at center, bounce

        hk1 "Nice and early too."

        hide FMaid_smile
        show FMaid_neutral at center, bounce

        hk1 "I'm sure you're curious about your situation."

        mc "Curious is... NOT how I would describe it."

        hide FMaid_neutral
        show FMaid_nervous at center, bounce

        hk1 "That is understandable."

        hide FMaid_nervous
        show FMaid_neutral at center, bounce

        hk1 "You are in the home of Sir Alicanto."
        hk1 "You remember that letter we sent you, correct?"

    if openedletter:

        mc "Yeah, I do."
        mc "I thought it was a scam or prank."

        hide FMaid_neutral
        show FMaid_nervous at center, bounce

        hk1 "Yeah, that seemed to be a common thought among the fellow contestants."
            
        mc "Yeah, I really don't know what you guys expected."

        hide FMaid_nervous
        show FMaid_surprised at center, bounce

        hk1 "Oh, no, don't get us wrong."

        hide FMaid_surprised
        show FMaid_nervous at center, bounce

        hk1 "We expected it."
        hk1 "However..."
        hk1 "Sir Alicanto enjoys the element of surprise."

        "Yeah no kidding."

        mc "Still, you guys could have shown SOME trace of your existence online."

        if repliedtopp:

            mc "All I got was a tweet from who I can assume is one of the contestants."

        else:

            mc "There wasn't even a trace or hint about any kind of show."
            mc "Could have at least made a premiere video or something."   
        
        hk1 "Yes, we are aware of that."
        hk1 "And again, we apologise."      

    else:

        mc "Oh, the pink one? I threw it away."

        hide FMaid_nervous
        show FMaid_surprised at center, bounce

        hk1 "..."
        hk1 "You didn't even read it?"

        mc "No, of course not."
        mc "I didn't know where it came from."
        mc "And it gave me the creeps."

        hk1 "That..."

        hide FMaid_surprised
        show FMaid_nervous at center, bounce

        hk1 "Is understandable..."

        hide FMaid_nervous
        show FMaid_surprised at center, bounce

        hk1 "But you didn't even open it?"

        mc "Trust me, I may be curious."
        mc "But not enough to kill the cat."

        hide FMaid_surprised
        show FMaid_nervous at center, bounce

        hk1 "..."
        hk1 "I see..."

        "Ugh that sounded dumb."
        "It sounded so much cooler in my head."
            
    jump choice9_done

    label choice9_who:

        $ attackedmaid = False

        mc "Who are you and what do you want with me?"

        hide FMaid_nervous
        hide FMaid_surprised
        show FMaid_nervous at center, bounce
    
        hk1 "I... see you're confused."

        "Ya think?"

        hide FMaid_nervous
        show FMaid_smile at center, bounce

        hk1 "I can understand your fear and confusion."

        hide FMaid_smile
        show FMaid_neutral at center, bounce

        hk1 "But I can assure you, that you are safe, and we would never purposefully harm you."
        hk1 "And to answer your questions."

        hide FMaid_neutral
        show FMaid_smile at center, bounce

        hk1 "I am a simple maid."

        hide FMaid_smile
        show FMaid_neutral at center, bounce

        hk1 "My name is not important, but I, along with another servant." 
        hk1 "Care for the people on the first floor."
        hk1 "This includes you and Sir Alicanto."
        hk1 "And you are in the home of Sir Alicanto."
        hk1 "In a room that was furnished and designed for you."
      
        mc "So..."
        mc "If you didn't kidnap me to hurt me..."
        mc "Why'd you do it in the first place?"
        mc "Pretty suspicious, if you ask me."

        hide FMaid_neutral
        show FMaid_nervous at center, bounce

        hk1 "You see, Sir Alicanto..."

        hide FMaid_nervous
        show FMaid_smile at center, bounce

        hk1 "As radiant and bright as he is, can be..."

        hide FMaid_smile
        show FMaid_nervous at center, bounce

        hk1 "... Quite..."
        hk1 "... Eccentric..."
        hk1 "And he quite enjoys the element of surprise."
        hk1 "Even if it has a risk of causing distress and chaos."

        "Wow, SO radiant..."
        "Actually, on that topic."
        "The way she said that was like he was a god or something."
        "..."
        "Freaky..."

        hide FMaid_nervous

        jump choice9_done

label choice9_done:

    hide FMaid_annoyed
    hide FMaid_nervous
    hide FMaid_neutral
    hide FMaid_smile
    hide FMaid_surprised
    show FMaid_neutral at center, bounce

    mc "So... Why am I meant to be here?"

    if openedletter:

        mc "I mean, I opened the letter, obviously."
        mc "But still, it's confusing."

    else:

        mc "I just really don't get why somebody would kidnap another with no threats"

    hk1 "Sadly I can't tell you much."

    hide FMaid_neutral
    show FMaid_smile at center, bounce

    hk1 "As Sir Alicanto would very much like to tell you himself."
    hk1 "And I wouldn't like to risk giving you an unfair advantage over the others."

    mc "So what CAN you tell me?"

    hide FMaid_smile
    show FMaid_neutral at center, bounce

    hk1 "That you are about to be presented to an audience."
    hk1 "You are part of a TV show."
    hk1 "So you should show your best self."

    mc "So, everything I do is going to be aired publicly?!"

    hide FMaid_neutral
    show FMaid_surprised at center, bounce

    hk1 "You say that as though we're going to invade your privacy!"

    "Aren't you already kinda doing that by..."
    "I dunno..."
    "Literally kidnapping me?!"

    hide FMaid_surprised
    show FMaid_nervous at center, bounce

    hk1 "Though, yes, certain parts of your daily life here will be aired."

    hide FMaid_nervous
    show FMaid_smile at center, bounce

    hk1 "You will understand more once you meet Sir Alicanto."

    hide FMaid_smile
    show FMaid_neutral at center, bounce

    hk1 "You may also take the time to get acquainted with the others."

    "What the hell?"
    "When'd I consent to THIS?"
    "Don't tell me I did it in my DREAM."

    mc "So, when can I meet them?"

    hide FMaid_neutral
    show FMaid_smile at center, bounce

    hk1 "That is what I came here to tell you, actually."

    hide FMaid_smile
    show FMaid_neutral at center, bounce

    hk1 "Sir Alicanto has asked everyone to arrive within the hour."

    mc "An hour?!" with hpunch 

    hide FMaid_neutral
    show FMaid_nervous at center, bounce

    hk1 "I'm sorry, I know the timing seems intimidating."
    
    mc "You think?!"

    if packed:
        
        mc  "Between unpacking and finding the place and everything else, I'll have no time!"
    
        hide FMaid_nervous
        show FMaid_surprised at center, bounce

        hk1 "Oh, no, do not worry!"

        hide FMaid_surprised
        show FMaid_smile at center, bounce

        hk1 "We will handle your luggage once you've left."

        hide FMaid_smile
        show FMaid_neutral at center, bounce

        hk1 "And we would never let you get lost in a place like this."
    
    else:

        mc "There won't be enough time!"
        mc "And I'll get lost!"

        hide FMaid_nervous
        show FMaid_neutral at center, bounce

        hk1 "Do not worry, the hour is more than enough time."
        hk1 "And we would never let you get lost in a place like this."

    
    mc "Well, that's a relief, I guess..."

    hide FMaid_neutral
    show FMaid_smile at center, bounce
    
    hk1 "Mhm."
    hk1 "Now, once you are ready to leave, simply go down the stairs to the {color=#ffef9f}ground floor{/color}."
    hk1 "Once you are there, turn {color=#ffef9f}left{/color} and you will quickly arrive to the dining hall."

    hide FMaid_smile
    show FMaid_neutral at center, bounce

    menu:

        "I see... Thank you.":
            jump choice10_yes
        "I'll forget that so fast":
            jump choice10_no

    label choice10_yes:

        mc "I'll be sure to remember that."

        hide FMaid_neutral
        show FMaid_smile at center, bounce

        hk1 "You are most welcome."

        hide FMaid_smile

        jump choice10_done

    label choice10_no:

        mc "There's no way I'm not gonna get lost here."

        hide FMaid_neutral
        show FMaid_surprised at center, bounce

        hk1 "But the directions are-"
        
        hide FMaid_surprised
        show FMaid_annoyed at center, bounce

        hk1 "Ah-"
        hk1 "You were joking."

        hide FMaid_annoyed
        show FMaid_nervous at center, bounce

        hk1 "Forgive me."

        "I wasn't."

        hide FMaid_nervous

        jump choice10_done

label choice10_done:

    show FMaid_smile at center, bounce
    
    hk1 "Now, I must be off. Is there anything else you might need?"

    if packed:

        mc "No, I don't think so."

        hide FMaid_smile
        show FMaid_neutral at center, bounce

        hk1 "Then I will be off."

        hide FMaid_neutral
        show FMaid_smile at center, bounce

        hk1 "I wish you a good day, Mx. [mcname]."

        hide FMaid_smile with dissolve

        "And off she goes."
        "Way too much is going on today..."


    else:

        mc "Yeah..."
        mc "I didn't really pack anything."

        hk1 "That is not a problem at all."
        hk1 "I'll make sure to let another servant know that you need spare clothes."
        hk1 "And they'll be sent straight to your room."

        mc "Ok. Thank you."

        hk1 "Mhmm."

        hide FMaid_smile
        show FMaid_neutral at center, bounce

        hk1 "Then I will be off."
        hk1 "I wish you a good day, Mx. [mcname]."

        hide FMaid_neutral

        "And off she goes."
        "I guess I'll just wait here then..."

        "..."
        "..."
        "..."

        play sound "audio/sfx/person-knocking-18474.mp3"

        "{i}KNOCK KNOCK.{/i}"

        mc "Oh, here they are now."
        mc "Come in!"

        play sound "audio/sfx/dorm-door-opening-6038.mp3"

        show tabby maid at center, bounce

        hk2 "Here. Your clothes."
        hk2 "Everything else you will need will be dropped off while you're out."

        menu:

            "Thank you.":
                jump choice12_yes
            "About time.":
                jump choice12_no

        label choice12_yes:

            mc "Oh, thank you."

            hide tabby maid
            show tabby maid2 at center, bounce

            hk2 "Mhm..."

            hide Butler_serious2
            show tabby maid at center, bounce

            hk2 "Let one of us know if you need anything else."

            mc "Yeah, I will."
            mc "Again, thank you."

            hide tabby maid
            show tabby maid2 at center, bounce

            hk2 "Mmhmm."

            hide tabby maid2

            "She left just as quickly as she entered."

            jump ch04

        label choice12_no:

            mc "Ugh."
            mc "About time."

            hide tabby maid
            show tabby maid annoyed at center, bounce

            hk2 "..."

            hide tabby maid annoyed 

            play sound "audio/sfx/door-slam-sound-effect-21878.mp3"

            "{i}SLAM{/i}" with hpunch

            mc "..."

            "She really just dropped them on the floor and left."
            "So rude!"
            "..."
            "But maybe I kinda deserved that..."
            "..."

            jump ch04

jump ch04

