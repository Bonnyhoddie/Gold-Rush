#characters
define mc = Character("[mcname]")

#unkowns
define U = Character("Unknown", color = "#FFFFFF")

define USa = Character("Girl in purple", color = "#8a6ed6")
define UZ = Character("Man in blue", color = "#6991c5")
define UB = Character("Girl with skates", color = "#e7a644")
define UH = Character("Person with long hair", color = "#a68fcc")
define UA = Character("Girl in uniform", color = "#ff8686")
define UT = Character("Man in lab coat", color = "#fdff80")
define US = Character("Man with gloves", color = "#4fac88")
define UP = Character("Woman with dyed hair", color = "#d899be")
define UM = Character("Girl with pink hair", color = "#7ce772")
define UAz = Character("Boy with pink hair", color = "#ffc5db")
define UR = Character("Man with tattoo", color = "#ff9e81")
define UF = Character("Woman with green hair", color = "#64ebd4")

#actual cast
define Sa = Character("Safirah", color = "#8a6ed6")
define Z = Character("Zach", color = "#6991c5")
define B = Character("Berry", color = "#e7a644")
define H = Character("Holly", color = "#a68fcc")
define A = Character("Aoi", color = "#ff8686")
define T = Character("Tsun", color = "#fdff80")
define S = Character("Sebastian", color = "#4fac88")
define P = Character("Percy", color = "#d899be")
define M = Character("Mina", color = "#7ce772")
define Az = Character("Azzy", color = "#ffc5db")
define R = Character("Red", color = "#ff9e81")
define F = Character("Flora", color = "#64ebd4")

define Al = Character("Alicanto", who_color = "#f5f375", what_color = "#ffef9f")


#defaults

$ annoyedAoi = False
$ liedtoSandT = False
default Percyintro_complete = False

transform center:

    xalign 0.5
    yalign 1.0

transform sleft:

    xalign 0.25
    yalign 1.0

transform Ssleft:

    xalign 0.10
    yalign 1.0

transform sright:

    xalign 0.75
    yalign 1.0

transform Ssright:

    xalign 0.90
    yalign 1.0

transform bounce:

    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    yoffset 0
    


#bg images
image fadeout = "Images/Fade-out.png"
image flashback = "Images/Flashback.png"
image mcroom = "images/backgrounds/new mc room.jpg"
image mcbalcony = "Images/backgrounds/Balcony.jpg"
image Hall = "images/backgrounds/Hall.jpg"
image Droom = "images/backgrounds/Dining room.jpg"
image Saroom = "images/backgrounds/Safirah bedroom.png"
image Zroom = "images/backgrounds/Zach Bedroom.jpeg"
image Aloffice = "images/backgrounds/Alicanto Office.png"

image FMaid_smile = "Images/FMaid Smiling.png"
image FMaid_neutral = "Images/FMaid neutral.png"
image FMaid_annoyed = "Images/Maid annoyed.png"
image FMaid_surprised = "Images/Maid surprise.png"
image FMaid_nervous = "Images/Maid nervous.png"
image Butler_serious1 = "Images/FMaid Smiling.png"
image Butler_serious2 = "Images/FMaid neutral.png"
image Butler_annoyed = "Images/Maid annoyed.png"

image Berry_neutral = "Images/Berry Neutral.png"
image Berry_sad = "Images/Berry Sad.png"
image Berry_angry = "Images/Berry Angry.png"
image Berry_surprised = "Images/Berry Surprise.png"
image Berry_shock = "Images/Berry Shock.png"
image Berry_nervous = "Images/Berry Nervous.png"
image Berry_happy = "Images/Berry Happy.png"

image Flora_neutral = "Images/Flora Neutral.png"
image Flora_surprise = "Images/Flora Surprise.png"
image Flora_shock = "Images/Flora Shock.png"
image Flora_annoyed = "Images/Flora annoyed.png"
image Flora_sad = "Images/Flora Sad.png"
image Flora_happy = "Images/Flora Happy.png"

image Aoi_neutral = "Images/Aoi Neutral.png"
image Aoi_angry = "Images/Aoi Angry.png"
image Aoi_happy = "Images/Aoi Happy.png"
image Aoi_sad = "Images/Aoi Sad.png"
image Aoi_surprise = "Images/Aoi Surprise.png"
image Aoi_flustered = "Images/Aoi Flustered.png"
image Aoi_sigh = "Images/Aoi Sigh.png"

image Holly_neutral = "Images/Holly Neutral.png"
image Holly_nervous = "Images/Holly Nervous.png"
image Holly_sad = "Images/Holly Sad.png"
image Holly_annoyed = "Images/Holly Annoyed.png"
image Holly_happy = "Images/Holly Happy.png"
image Holly_surprise = "Images/Holly Surprised.png"
image Holly_distracted = "Images/Holly Distracted.png"

image Sebastian_neutral = "Images/Sebastian Neutral.png"
image Sebastian_happy = "Images/Sebastian Happy.png"
image Sebastian_annoyed = "Images/Sebastian Annoyed.png"
image Sebastian_sad = "Images/Sebastian Sad.png"
image Sebastian_annoyed = "Images/Sebastian Annoyed.png"
image Sebastian_surprise = "Images/Sebastian Surprise 1.png"
image Sebastian_surprise2 = "Images/Sebastian Surprise 2.png"
image Sebastian_thinking = "Images/Sebastian Thinking.png"
image Sebastian_sigh = "Images/Sebastian sigh.png"

image Tsun_neutral = "Images/Tsun Neutral.png"
image Tsun_happy = "Images/Tsun Happy.png"
image Tsun_annoyed = "Images/Tsun Annoyed.png"
image Tsun_sad = "Images/Tsun Sad.png"
image Tsun_surprise = "Images/Tsun Surprise.png"
image Tsun_smug = "Images/Tsun Smug.png"
image Tsun_serious = "Images/Tsun Serious.png"

image Red_neutral = "Images/Red Neutral.png"
image Red_annoyed = "Images/Red Annoyed.png"
image Red_happy = "Images/Red Happy.png"
image Red_surprise = "Images/Red Surprised.png"
image Red_nervous = "Images/Red Nervous.png"

image Mina_neutral = "Images/Mina Neutral.png"
image Mina_sad = "Images/Mina Sad.png"
image Mina_angry = "Images/Mina Angry.png"
image Mina_happy = "Images/Mina Happy.png"
image Mina_nervous = "Images/Mina Nervous.png"
image Mina_flustered = "Images/Mina Flustered.png"

image Percy_neutral = "Images/Percy Neutral.png"
image Percy_annoyed = "Images/Percy Annoyed.png"
image Percy_happy = "Images/Percy Happy.png"
image Percy_nervous = "Images/Percy Nervous.png"
image Percy_sad = "Images/Percy Sad.png"
image Percy_scold = "Images/Percy Scold.png"
image Percy_surprise = "Images/Percy Surprise.png"

image Azzy_neutral = "Images/Azzy Neutral.png"
image Azzy_sad = "Images/Azzy Sad.png"
image Azzy_angry = "Images/Azzy Angry.png"
image Azzy_flustered = "Images/Azzy Flustered.png"
image Azzy_happy = "Images/Azzy Happy.png"
image Azzy_thinking = "Images/Azzy Thinking.png"

image Alicanto_neutral = "Images/Alicanto Neutral.png"
image Alicanto_happy = "Images/Alicanto Happy.png"
image Alicanto_nervous = "Images/Alicanto Nervous.png"
image Alicanto_annoyed = "Images/Alicanto Annoyed.png"
image Alicanto_Bow = "Images/Alicanto Bow.png"
image Alicanto_mischievous = "Images/Alicanto Mischievous.png"

#player name input code begins

label ch05:
    
    label Dining_Hall1:

        scene fadeout
        with Dissolve(.5)
    
        pause .5

        scene Droom
        with Dissolve(.5)

        "So this is the dining hall."
        "And where we're supposed to meet up."

        if late:

            "Everyone's here."
            "And they're all staring at me..."
            "This is humiliating..."
            "There's only one guy who isn't sat down."
            "He looks so fancy."
            "That must be the 'Sir' Alicanto I've heard so much about."

            show Alicanto_neutral at center, bounce

            play music "audio/bgm/Of Far Different Nature - Intervals [v2] (CC-BY 4.0).ogg" fadeout 1.0

            Al "Tsk tsk tsk."
            Al "You're late, Mx. [mcname]."

            "He's so charming it's creepy..."

            mc "Yeah, I'm sorry."

            hide Alicanto_neutral
            show Alicanto_happy at center, bounce

            Al "Do not worry about it."
            Al "Luckily for you, you didn't miss out on anything."

            hide Alicanto_happy
            show Alicanto_mischievous at center, bounce

            Al "We were waiting for you, actually."

            "That's even worse!"

            show Alicanto_mischievous at sright with MoveTransition(0.2)  
            show Aoi_angry at sleft, bounce


            UA "Yeah, you took way too long!"

            hide Alicanto_mischievous
            show Alicanto_happy at sright, bounce

            Al "Now now, Miss. Aoi." 

            $ metAoi = True
            
            Al "Let's not make Mx. [mcname] feel more embarrassed than they already are."

            hide Aoi_angry
            show Aoi_neutral at sleft, bounce

            A "Hmph!"
            A "They shouldn't have been late if they didn't want to be embarrassed!"

            hide Aoi_neutral
            show Aoi_angry at sleft, bounce

            A "And we're not friends, so don't use my first name!"

            hide Alicanto_happy
            show Alicanto_Bow at sright, bounce

            Al "Much apologies, Miss. Miyagawa."

            "Rude, it's not MY fault."
            "..."
            "Ok, yeah, it is kinda my fault."

            hide Alicanto_Bow
            hide Aoi_angry
            show Alicanto_happy at sright, bounce
            show Alicanto_happy at center with MoveTransition(0.2)

            Al "Now, take your seat and let us begin."

            hide Aoi_angry
            show Alicanto_happy at center  

            "I wish you would have said that faster."
            "Let's sit down then..."
            "I'm sat next to a purple haired person and the Miyagawa girl."
            "Ugh, I wish that wouldn't be the case..."

            jump Alicantoexplanation

        else:

            "Everyone seems to be here."
            
            if openedletter:

                if LeftwithSafirah or LeftwithZach:

                    "Except 1."

                else:
                    
                    "Except 2."

                "There WERE supposed to be 11 of us, right?"
                "And except Alicanto."
                "Otherwise they'd be focusing on him."
            
            else:
                
                "Except Alicanto."
                "Otherwise they'd be focusing on him."
            
            "I should probably start introducing myself."

            label Introductions:

                play music "audio/bgm/Calm Loop.ogg" fadeout 1

                menu:

                    "Talk to the girls in the roller skates and yellow shirt.":
                        if metBerry and metFlora:
                            call alreadymet from _call_alreadymet
                            jump Introductions
                        else:
                            jump BerryandFlora1
                    "Talk to the person with the purple hair.":
                        if metHolly:
                            call alreadymet from _call_alreadymet_1
                            jump Introductions
                        else:
                            jump Holly1
                    "Talk to the red haired girl.":
                        if metAoi:
                            call alreadymet from _call_alreadymet_2
                            jump Introductions
                        else:
                            jump Aoi1
                    "Talk to the men in the gloves and lab coat.":
                        if metSebastian and metTsun:
                            call alreadymet from _call_alreadymet_3
                            jump Introductions
                        else:
                            jump SebastianandTsun1
                    "Talk to the man with the tattoo.":
                        if metRed:
                            call alreadymet from _call_alreadymet_4
                            jump Introductions
                        else:
                            jump Red1
                    "Talk to the girl in the white sweater.":
                        if metPercy:
                            call alreadymet from _call_alreadymet_5
                            jump Introductions
                        else:
                            jump Percy1
                    "I'm done.":
                        if metAoi and metBerry and metHolly and metPercy and metSebastian and metRed:
                            jump Alicantoarrives
                        else:
                            jump notdone1

            label BerryandFlora1:

                $ metBerry = True
                $ metFlora = True

                "Let's talk to those two."
                "They seem like they're having fun."

                play music "audio/bgm/Of Far Different Nature - Dream Factory (CC-BY).ogg"

                show Berry_happy at sleft, bounce
                show Flora_happy at sright

                UB "Hahaha!"
                UB "You seem to be having a lot of fun watching me spin on these!"

                hide Flora_happy
                show Flora_happy at sright, bounce

                UF "Of course!"
                UF "You look so happy and cute!"
                UF "I wish I knew how to skate."

                hide Berry_happy
                show Berry_neutral at sleft, bounce

                UB "Why don't I teach you?"

                hide Berry_neutral
                show Berry_happy at sleft, bounce

                UB "It'd be fun!" 
                UB "This house is so big, we'd probably have so much space for practice."

                hide Flora_happy
                show Flora_shock at sright, bounce

                UF "Oh, goodness, no!"
                UF "I'd fall flat on my face."

                hide Berry_happy
                show Berry_neutral at sleft, bounce

                UB "Hey, don't worry about that!"
                UB "Even if you did, practice makes perfect!"
                UB "Plus, it's easy!"

                hide Berry_neutral
                show Berry_happy at sleft, bounce

                UB "I've done it since I was a kid!"

                hide Flora_shock 
                show Flora_sad at sright, bounce

                UF "Oh, I don't know..."

                hide Flora_sad 
                show Flora_neutral at sright, bounce

                UF "I guess it wouldn't hurt to try something new."

                hide Berry_happy
                show Berry_happy at sleft, bounce

                UB "Hey, that's the spirit!"

                hide Berry_happy
                show Berry_neutral at sleft, bounce

                UB "Why don't we meet later once we've settled in?"

                hide Flora_neutral
                show Flora_happy at sright, bounce

                UF "I wouldn't mind that."

                "Aww, they get along so well already."
                "It's kinda nice just watching them."

                hide Berry_neutral
                show Berry_surprised at sleft, bounce

                hide Flora_happy
                show Flora_surprise at sright, bounce

                UB "Hm?" 

                hide Berry_surprised
                show Berry_happy at sleft, bounce

                UB "Oh, hey!"

                "Crap, they noticed me."
                "Wait, why was I worried?"

                mc "Uh, hey, I just wanted to say hi."
                mc "I'm [mcname]."

                hide Berry_happy
                show Berry_neutral at sleft, bounce
                
                B "I'm Berry! And this is Flora!"

                hide Flora_surprise
                show Flora_happy at sright, bounce

                F "It's so nice to meet you."
                
                mc "Yeah, same here."

                hide Flora_happy
                show Flora_neutral at sright

                hide Berry_neutral
                show Berry_happy at sleft, bounce
                
                B "This whole thing is a funny situation, isn't it?"

                mc "Funny is... The wrong word."

                hide Berry_happy
                show Berry_neutral at sleft, bounce

                B "Oh, yeah! It's really strange."

                hide Berry_neutral
                show Berry_nervous at sleft, bounce

                B "Sorry, I'm not always the best with my words."

                hide Flora_neutral
                show Flora_happy at sright, bounce

                F "I think it was a good word to use."

                hide Flora_happy
                show Flora_neutral at sright, bounce

                F "What's happening here is so strange it's funny."

                hide Berry_nervous
                show Berry_happy at sleft, bounce

                B "Yeah, it is, haha."
                B "We've been kidnapped but we're not in danger."
                B "And most of the people here look so calm and relaxed despite how we got here."
                B "It's such an odd situation!"

                hide Berry_happy
                show Berry_neutral at sleft, bounce

                B "But I feel like we should make the best of it."
                B "And what better way to do that than to cheer each other up?"

                hide Flora_neutral
                show Flora_happy at sright, bounce

                F "And she's certainly cheered ME up!"

                hide Berry_neutral
                show Berry_happy at sleft, bounce

                B "Well, what can I say?"
                B "I'm a natural born entertainer!"

                F "Mhmm!"

                hide Flora_happy
                show Flora_neutral at sright, bounce

                F "And I can tell you're happy doing it!"
                
                B "Yeah, that's right!"
                B "I especially love the smiles I can put on all the kid's faces back at my job!"
                
                menu:
                    mc "Aw, you two get along pretty well!"

                    "It's almost like you're dating.":
                        jump BerryandFlorachoice1_dating
                    "It's almost like you already know each other.":
                        jump BerryandFlorachoice1_history

                label BerryandFlorachoice1_dating:

                    mc "It's almost like you're both dating already!"

                    hide Berry_happy
                    show Berry_surprised at sleft, bounce

                    hide Flora_neutral
                    show Flora_surprise at sright, bounce

                    B "..."

                    hide Berry_surprised
                    show Berry_shock at sleft, bounce

                    B "HUUUUHH?!" with hpunch

                    hide Flora_surprise
                    show Flora_neutral at sright, bounce

                    F "Haha, it looks like that?"
                    
                    hide Flora_neutral
                    show Flora_happy at sright, bounce

                    F "I guess that's a good sign we're gonna be great friends, isn't it Berry?"

                    hide Berry_shock
                    show Berry_nervous at sleft, bounce

                    B "I guess, but-"

                    hide Berry_nervous
                    show Berry_angry at sleft, bounce

                    B "What the heck is up with you?!"
                    B "That's such a wild thing to say to people you just met!"

                    mc "Ah, I'm sorry, I didn't meant to offend you."

                    B "Just don't say something like that again!"

                    hide Flora_happy
                    show Flora_annoyed at sright, bounce

                    F "I agree, it's not very nice to say."
                    F "And it's definitely an effective way of making friendships awkward."

                    hide Flora_annoyed
                    show Flora_happy at sright, bounce

                    F "But still, I take it as a sign we're going to be great friends!"
                    F "Especially since it was a judgement based on our friendship and not just a judgement on two girls being friendly!"

                    hide Berry_angry
                    show Berry_nervous at sleft, bounce

                    B "Haha, that's true."

                    hide Berry_nervous
                    show Berry_neutral at sleft, bounce

                    B "It's weird how you can completely change how something sounds."

                    hide Flora_happy
                    show Flora_surprise at sright, bounce

                    F "Weird?"

                    hide Berry_neutral
                    show Berry_nervous at sleft, bounce

                    B "Weird in a good way!"

                    F "Oh!"

                    hide Flora_surprise
                    show Flora_happy at sright, bounce

                    F "Haha, I guess."

                    "Oh, I didn't make things awkward."
                    "That's good."
                    "But I probably shouldn't say something like that again."

                    mc "Well, I'm glad I got to meet you both."
                    mc "Again, sorry for what I said."

                    hide Berry_nervous
                    show Berry_neutral at sleft, bounce
                    
                    B "Ah, it's fine, especially now you've apologised."

                    hide Berry_neutral
                    show Berry_happy at sleft, bounce

                    B "Hey, you should try skating with us, too!"

                    hide Flora_happy
                    show Flora_shock at sright, bounce

                    F "Oh, no, that'd be so embarrassing!"

                    hide Berry_happy
                    show Berry_neutral at sleft, bounce
                    
                    B "Oh, no it won't!"
                    B "It'll be fun!"
                    
                    mc "Oh, no, I haven't skated since I was a kid."

                    hide Berry_neutral
                    show Berry_happy at sleft, bounce
                    
                    B "See? You don't know how to, and they've gone rusty!"
                    B "It won't be embarrassing, you'll be laughing WITH each other, not AT each other!"

                    hide Flora_shock
                    show Flora_neutral at sright, bounce

                    F "Haha, I guess that's true."

                    mc "If you both promise not to laugh at me, I guess I can consider it."

                    hide Berry_happy
                    show Berry_neutral at sleft, bounce

                    B "We promise!"
                    
                    mc "Then I'll see you later."

                    hide Berry_neutral
                    show Berry_happy at sleft, bounce

                    B "Yep!"
                    B "See ya later!"

                    "Those two were pretty nice."
                    "I hope the others are just as nice."

                    hide Berry_happy
                    hide Flora_neutral

                    jump Introductions

                label BerryandFlorachoice1_history:


                    mc "It's like you both already knew each other before all of this."

                    hide Berry_happy
                    show Berry_surprised at sleft, bounce

                    B "Huh?" 

                    hide Berry_surprised
                    show Berry_neutral at sleft, bounce

                    B "Oh, no, we just met."

                    hide Flora_neutral
                    show Flora_happy at sright, bounce
                    
                    F "Yeah, and when we did, we just clicked!"

                    hide Berry_neutral
                    show Berry_happy at sleft, bounce
                    
                    B "Haha, that's true!"

                    hide Berry_happy
                    show Berry_nervous at sleft, bounce

                    B "We haven't even met the others yet."

                    hide Flora_happy
                    show Flora_surprise at sright, bounce

                    F "Oh, no, we haven't!"

                    hide Flora_surprise
                    show Flora_neutral at sright, bounce

                    F "But I'm sure it's alright."
                    F "Some of them seem busy anyway."
                    F "We can say hi to them after."

                    hide Berry_nervous
                    show Berry_happy at sleft, bounce

                    B "Yeah, we can!"

                    mc "Well, I'm glad I got to meet you both."

                    hide Berry_happy
                    show Berry_neutral at sleft, bounce
                    
                    B "Yeah, we'll see you-"

                    hide Berry_neutral
                    show Berry_happy at sleft, bounce

                    B "Hey, you should try skating with us, too!"

                    hide Flora_neutral
                    show Flora_shock at sright, bounce

                    F "Oh, no, that'd be so embarrassing!"
                    
                    hide Berry_happy
                    show Berry_happy at sleft, bounce

                    B "No it won't!"
                    B "It'll be fun!"
                    
                    mc "Oh, no, I haven't skated since I was a kid."

                    hide Berry_happy
                    show Berry_neutral at sleft, bounce
                    
                    B "See? You don't know how to, and they've gone rusty!"

                    hide Berry_neutral
                    show Berry_happy at sleft, bounce

                    B "It won't be embarrassing, you'll be laughing WITH each other, not AT each other!"

                    hide Flora_shock
                    show Flora_neutral at sright, bounce

                    F "Heh, I guess that's true."

                    mc "If you both promise not to laugh at me, I guess I can consider it."

                    hide Berry_happy
                    show Berry_neutral at sleft, bounce

                    B "We promise!"
                    
                    mc "Then I'll see you later."

                    hide Berry_neutral
                    show Berry_happy at sleft, bounce

                    B "Yep!"
                    B "See ya later!"

                    hide Berry_happy with dissolve
                    hide Flora_neutral with dissolve

                    "Those two were pretty nice."
                    "I hope the others are just as nice."

                    jump Introductions
                
            label Percy1:

                $ metPercy = True

                "Let's talk to her."
                "She looks like she's wants to talk to someone."

                mc "Hey, I'm [mcname]. Nice to meet you."

                play music "audio/bgm/Mazit Music Loop.ogg"

                show Percy_happy at center, bounce

                P "Percy."
                P "And you too."

                if repliedtopp:

                    mc "Percy..."
                    mc "As in..."
                    mc "Percypiper?"

                    hide Percy_happy
                    show Percy_surprise at center, bounce

                    P "Oh!"
                    P "You were the person who replied to me?"

                    mc "Haha yeah, seems so."

                    hide Percy_surprise
                    show Percy_happy at center, bounce

                    P "Well, then it's nice to meet you again."

                    mc "Yeah, nice to meet you again." 

                hide Percy_happy 
                show Percy_neutral at center, bounce

                P "It's very busy in here, isn't it?"

                mc "Yeah, it is."

                P "Yet despite how busy it is, it feels like there's nobody to talk to."

                mc "Haha, yeah, I know what you mean."
                mc "I've been going around talking to people but I always feel bad interrupting them."

                P "I wish I had your confidence."

                mc "You mean, you haven't spoken to a single person?"

                hide Percy_neutral
                show Percy_nervous at center, bounce

                P "..."
                P "Not really."

                hide Percy_nervous
                show Percy_sad at center, bounce

                P "It's easy for me to get along with people."
                P "But it's hard for me to start conversations."

                mc "Oh, I see."

                "She's already too much like me."

                mc "That's the same with me."
                mc "I may be able to start conversations."
                mc "But that's because I'm trying not to freak out."
                mc "But talking to some of the people here is surprisingly calming."

                hide Percy_sad 
                show Percy_neutral at center, bounce

                P "Is that so..."
                P "Maybe I should try an introduce myself to everyone, then."
                P "Any advice on the people here?"

                label Percyintros:

                    menu:
                        "Who should I tell Percy about?"

                        "About Berry and Flora." if metBerry:
                            jump Percyintros_BerryandFlora
                        "About Holly." if metHolly:
                            jump Percyintros_Holly
                        "About Aoi." if metAoi:
                            jump Percyintros_Aoi
                        "About Sebastian and Tsun." if metSebastian:
                            jump Percyintros_SebastianandTsun
                        "About Zach." if metZach:
                            jump Percyintros_Zach
                        "About Red." if metRed:
                            jump Percyintros_Red
                        "About Safirah." if metSafirah:
                            jump Percyintros_Safirah
                        "I'm done.":
                            jump Percyintros_done

                label Percyintros_BerryandFlora:

                    $ Percyintro_complete = True

                    mc "Well, the girls in the roller skates and yellow top are Berry and Flora."
                    mc "They're both actually super friendly and social."
                    mc "I don't have much advice for those two, actually."
                    mc "I just hope they're not too high energy for you."

                    hide Percy_sad
                    hide Percy_annoyed
                    hide Percy_nervous
                    hide Percy_sad
                    hide Percy_scold
                    hide Percy_neutral
                    hide Percy_surprise
                    hide Percy_happy
                    show Percy_happy at center, bounce

                    P "Ah, I see."
                    P "They already remind me of my friends from home."

                    mc "Hah, yeah, they kind of remind me of mine too."
                    
                    jump Percyintros

                label Percyintros_Holly:

                    $ Percyintro_complete = True

                    mc "Holly is the guy there with the purple hair."
                    mc "He's the complete opposite of Berry and Flora."
                    mc "And he's more like Sebastian and Tsun."
                    mc "The best way to get along with him is to talk about his game."
                    mc "Because otherwise he'll give really dry and dead responses."
                    mc "Like, conversation killing dry."

                    if annoyedHolly:

                        mc "But don't talk about old games or argue with him."
                        mc "He'll shut it down REAL fast."

                    hide Percy_sad
                    hide Percy_annoyed
                    hide Percy_nervous
                    hide Percy_sad
                    hide Percy_scold
                    hide Percy_neutral
                    hide Percy_surprise
                    hide Percy_happy
                    show Percy_sad at center, bounce

                    P "Oh, ok."
                    P "I'm not much of a gamer though."

                    mc "So I wasn't much help to you, then..."
                    mc "Because I don't know how else to get him to talk to you."

                    jump Percyintros

                label Percyintros_Aoi:

                    $ Percyintro_complete = True

                    mc "That red haired girl is Aoi."
                    mc "But she doesn't like being called that."
                    mc "So call her by her last name, 'Miyagawa'."
                    mc "But she isn't very easy to get along with."
                    mc "She's your average teenager with a bad attitude."
                    mc "I mean, she yelled at me after I said hi."
                    mc "She also hates adults and 'bright side' believers."

                    hide Percy_sad
                    hide Percy_annoyed
                    hide Percy_nervous
                    hide Percy_sad
                    hide Percy_scold
                    hide Percy_neutral
                    hide Percy_surprise
                    hide Percy_happy
                    show Percy_sad at center, bounce

                    P "That's a lot of negatives for such a young girl."
                    
                    mc "Oh, yeah, that's true."
                    mc "A lot of her negative behaviour could very well be her being scared."
                    mc "So, if you want some plus sides or advice for a good conversation..."
                    mc "She's very knowledgable about her own culture."
                    mc "She gave me some pretty cool information about how Japanese names work."
                    mc "She's also your typical kid, so she likes cute things."
                    mc "Though it can be pretty difficult getting to talk about that."
                    mc "Especially considering the attitude she has right now."

                    hide Percy_sad
                    show Percy_neutral at center, bounce

                    P "I'll keep that in mind."

                    mc "Oh, yeah." 
                    mc "You'll have no problem getting along with her."
                    mc "You seem to be a very polite person."

                    hide Percy_neutral
                    show Percy_happy at center, bounce

                    P "Hah, well I try to be."

                    jump Percyintros 

                label Percyintros_Azzy:

                    mc "Azzy's the pink haired boy there."
                    mc "He's pretty nice, I guess."
                    mc "But he's also pretty childish."
                    mc "And he tends to react badly to any negativity."
                    mc "He also has very strong values, so don't try to debate with him."

                    hide Percy_sad
                    hide Percy_annoyed
                    hide Percy_nervous
                    hide Percy_sad
                    hide Percy_scold
                    hide Percy_neutral
                    hide Percy_surprise
                    hide Percy_happy
                    show Percy_sad at center, bounce

                    P "You make him sound worse than he really is."

                    mc "Haha, sorry."
                    mc "I actually admire his values."
                    mc "It's honestly just surprising that they come from such a young looking face."
                    mc "It's cool to see though."
                    mc "Most of the people I live around just don't care about issues in the world."

                    hide Percy_sad
                    show Percy_neutral at center, bounce

                    P "I agree."
                    P "While it can be really harmful for your mental health to continously absorb bad news..."
                    P "There are also dangers with ignorance."

                    mc "Oh, yeah I agree."

                    "Man it's great to meet so many people already who don't just tell me to 'suck it up'."

                    jump Percyintros

                label Percyintros_SebastianandTsun:

                    $ Percyintro_complete = True

                    hide Percy_sad
                    hide Percy_annoyed
                    hide Percy_nervous
                    hide Percy_sad
                    hide Percy_scold
                    hide Percy_neutral
                    hide Percy_surprise
                    hide Percy_happy
                    show Percy_surprise at center, bounce

                    P "What about those two?"

                    mc "Those two are Sebastian and Tsun."

                    menu:

                        "They're both bad news.":
                            jump Percy1SandT_Bad
                        "They're both really interesting.":
                            jump Percy1SandT_Good

                    label Percy1SandT_Bad:

                        mc "I get weird vibes from those two."

                        hide Percy_surprise
                        show Percy_sad at center, bounce

                        P "Are they not good people?"

                        mc "Well, they're doctors, so I hope they are."
                        mc "But I feel like they're very..."
                        mc "... Full of themselves..."
                        mc "Especially Tsun."
                        mc "He definitely likes bragging."
                        mc "Sebastian actually seems pretty modest so far."
                        mc "But something doesn't feel right with him."

                        P "I see..."

                        hide Percy_sad
                        show Percy_happy at center, bounce

                        P "Well, there's nothing wrong with confidence."
                        P "And they're doctors, I'm sure they're good people."

                        hide Percy_happy
                        show Percy_neutral at center, bounce

                        P "Not only that, but you just met them." 
                        P "It's far too early to judge people so negatively."
                        P "Especially on behaviours like arrogance."

                        jump Percyintros

                        
                    label Percy1SandT_Good:
                        
                        mc "They're both doctors."
                        mc "And they're both super skilled at what they do."
                        mc "Sebastian specifically is a criminal psychologist."
                        mc "And Tsun is a general surgeon."

                        hide Percy_surprise
                        show Percy_happy at center, bounce

                        P "Oh, that sounds so interesting!"

                        mc "It is!"
                        mc "My only complaints of them is that..."
                        mc "Sebastian's not used to small talk."
                        mc "So if you want an ideal conversation, talk to him about his job and interests."
                        mc "And Tsun is very overconfident in himself."
                        mc "Which, despite his achievements, may be annoying."
                        mc "Though, he's better at talking than Sebastian, so that might be enough to redeem him."

                        hide Percy_happy
                        show Percy_neutral at center, bounce

                        P "Oh, I understand."
                        P "That doesn't sound too bad."
                        P "So I'll just have to ask questions, right?"

                        mc "Yeah, that'll do."
                        mc "Though, don't worry too much about keeping a conversation going."
                        mc "They already find each other entertaining enough."
                        mc "So you can just introduce yourself, ask some things and leave."
                        mc "..."
                        mc "Ok, not exactly like that."
                        mc "But you know what I mean."

                        hide Percy_neutral
                        show Percy_happy at center, bounce

                        P "Yes, I know what you mean, don't worry."

                        mc "Oh, ok good."

                        jump Percyintros

                label Percyintros_Zach:

                    $ Percyintro_complete = True

                    if LeftwithZach:

                        mc "He's the guy with the blue hair I came in with."

                    else:
                        
                        mc "Zach doesn't seem to be here yet, but he has blue hair in a ponytail."
                        mc "Can't miss him."

                        "Huh, I wonder what's taking him so long."
                        "He left before me, after all."

                    if annoyedZach:

                        mc "He's super rude."
                        mc "I couldn't even have a normal discussion with him without him slamming the door."

                        hide Percy_sad
                        hide Percy_annoyed
                        hide Percy_nervous
                        hide Percy_sad
                        hide Percy_scold
                        hide Percy_neutral
                        hide Percy_surprise
                        hide Percy_happy
                        show Percy_surprise at center, bounce

                        P "Oh my..."

                        mc "I know, right?!"
                        mc "But part of me can't help but think he's not a bad person."
                        mc "So you should probably try and give him a chance."
                        mc "And don't annoy him like I did."

                        hide Percy_surprise
                        show Percy_sad at center, bounce

                        P "I'll keep that in mind."

                    else:
                        mc "And, while he can be quick to react, he's actually pretty decent."
                        mc "But he doesn't seem to like many people here right now."
                        mc "He seems like the type to develop strong opinions of people based on first impressions."

                        hide Percy_sad
                        hide Percy_annoyed
                        hide Percy_nervous
                        hide Percy_sad
                        hide Percy_scold
                        hide Percy_neutral
                        hide Percy_surprise
                        hide Percy_happy
                        show Percy_sad at center, bounce

                        P "He sounds like he'd be difficult to talk to."

                        mc "If you make a mistake, yeah, for a little while, but I think he's just stressed."

                        show Percy_sad at center, bounce

                        P "That might be true."
                        P "That seems to be a shared feeling between a few of the people here."

                        mc "Hey, maybe you two will get along great!"
                        mc "Especially since you might be able to relate to him."
                        
                        hide Percy_sad
                        show Percy_happy at center, bounce

                        P "I hope so."

                    jump Percyintros

                label Percyintros_Mina:

                    mc "Mina is the girl with the pink hair and the patches on her skin."
                    mc "Another one of the friendly ones."
                    mc "I don't have any advice for her either."
                    mc "She's nice, social and she has pretty thick skin, so doesn't get insulted easily."
                    mc "Actually, she's just an all-round perfect friend to have."

                    P "She sounds very nice!"

                    mc "Yeah, she does."

                label Percyintros_Red:

                    $ Percyintro_complete = True

                    mc "Now onto Red..."

                    hide Percy_sad
                    hide Percy_annoyed
                    hide Percy_nervous
                    hide Percy_scold
                    hide Percy_neutral
                    hide Percy_surprise
                    hide Percy_happy
                    show Percy_surprise at center, bounce

                    P "The one with the tattoo?"
                    P "I already get very bad feelings about him."
                    P "He seems nice enough to the others, but something feels off."

                    menu:

                        "He's not that bad.":
                            jump Percy1Red_Good
                        "Yeah, you have the right idea.":
                            jump Percy1Red_Bad

                    label Percy1Red_Good:

                        mc "He's not too bad actually."
                        mc "Kinda weird about things that he doesn't understand, like phobias."
                        mc "But as annoying as it is, I guess it's not that much of an issue."
                        mc "He's pretty open, too."
                        mc "Especially about his tattoos."

                        hide Percy_surprise
                        show Percy_surprise at center, bounce

                        P "Oh, really?"

                        hide Percy_surprise
                        show Percy_happy at center, bounce

                        P "That bad feeling must just all be in my head then..."

                        mc "Yeah."

                        if metZach:

                            mc "I don't know why Zach's so worried about him, honestly."
                            mc "He made me worry but then I actually met him."
                            mc "Though even I didn't get good vibes from him until I leaned more about him"
                            mc "But I'd recommend you don't try bringing those two together."
                            mc "Zach doesn't seem to like him."

                            hide Percy_surprise
                            show Percy_sad at center, bounce

                            P "I see..."
                            P "It's strange that there are already clashes here."
                            P "Especially when we've only just woke up."

                            mc "Well, that's just what you can expect when you meet new people."
                            mc "Sometimes you like them instantly, sometimes it needs more time."
                            mc "And sometimes you just hate their guts immediately."

                            hide Percy_sad
                            show Percy_annoyed at center, bounce

                            P "Well, I know that."
                            
                            hide Percy_annoyed
                            show Percy_neutral at center, bounce
                            
                            P "What I mean is..."
                            P "Maybe there's a reason for the clash aside from that."

                            mc "So..."
                            mc "You're saying one of them might actually be an issue?"

                            hide Percy_neutral
                            show Percy_nervous at center, bounce

                            P "Not exactly that."

                            hide Percy_nervous
                            show Percy_neutral at center, bounce

                            P "What I meant was..."

                            hide Percy_neutral
                            show Percy_nervous at center, bounce

                            P "Ok, yeah, that..."

                            mc "Eh, I'm sure it'll be fine and they'll sort themselves out."

                        jump Percyintros
                        
                    
                    label Percy1Red_Bad:

                        $ GavePercybadimpressionofRed = True

                        mc "And, not to be biased, but you're right to."
                        mc "He's friendly, but in a weird way."

                        hide Percy_surprise
                        show Percy_annoyed at center, bounce

                        P "You're losing me now."

                        if metZach:

                            
                            mc "Yeah, that sounded like a weird reason to avoid him."
                            mc "What I mean is, he's friendly to the point of being open about everything."
                            mc "Including his violent tendencies."
                            mc "He tends to laugh when talking about those things too."
                            mc "Like when he told Zach that he attacked a maid."
                            mc "But then he just has no regrets about it when confronted."
                            mc "He also doesn't seem very sympathetic about certain things, like my phobias."

                            hide Percy_annoyed
                            show Percy_surprise at center, bounce

                            P "What?!"
                            P "Why would he laugh about that?!"

                            if attackedmaid:

                                mc "I know, even I felt bad when I threw that lamp at mine."

                                hide Percy_surprise
                                show Percy_scold at center, bounce

                                P "You attacked somebody?!"

                                mc "Oh, no, don't worry!"
                                mc "She caught it and laughed it off!"
                                mc "And I feel bad."
                                mc "And like she was going to kill me if I didn't."

                                hide Percy_scold
                                show Percy_sad at centre, bounce

                                P "..."
                                P "I see..."
                                P "As long as she's alright."
                                P "But he sounds frightening."
                                P "Especially when he laughed about it."
                                P "I'm just hoping you're lying about it."
                            
                                mc "That's understandable."

                                hide Percy_sad
                        
                            else:

                                mc "I don't know."
                                mc "All I know is that he gives me a bad feeling."
                                mc "And that it would do us both good to stay away from him."

                                hide Percy_surprise
                                show Percy_sad at center, bounce

                                P "..."
                                P "I don't think I'd feel comfortable staying away from him."
                                P "Excluding people based on what I hear isn't exactly my thing."
                                P "But I know to be careful around him now."

                                mc "That's a relief."
                                mc "... Anyway..."
                                mc "Let's move onto talking about the others."

                                hide Percy_sad
                                show Percy_neutral at center, bounce

                                P "Yeah... Let's do that..."

                        else:

                            $GavePercybadimpressionofRed = False

                            mc "Yeah, that sounded like a weird reason to avoid him."
                            mc "What I mean is, he's very friendly, but something about him just feels off."
                            mc "And sometimes it just kinda leaks out."
                            mc "Like when he kinda brushes things off, like him judging some phobias I told him about."
                            mc "Something about him just makes me uncomfortable, too."

                            hide Percy_annoyed
                            show Percy_surprise at center, bounce

                            P "Is that so?"

                            hide Percy_surprise
                            show Percy_sad at center, bounce

                            P "I'm sorry to hear about how he treated your phobias."

                            hide Percy_sad
                            show Percy_happy at center, bounce

                            P "Though, this doesn't mean you can't get along with him."
                            P "Maybe you both just got off on the wrong foot."

                            mc "Heh, yeah, maybe."
                            mc "Maybe you're right, and I shouldn't just judge him so fast."
                            mc "I mean, today's been stressful enough."
                            mc "This is probably just him being stressed."

                            P "Exactly."
                            P "You should try talking to him later."

                            mc "Yeah."
                            mc "But anyway, let's talk about the others."

                        jump Percyintros
                        
                label Percyintros_Safirah:

                    $ Percyintro_complete = True

                    mc "Then there is Safirah."

                    if LeftwithSafirah:

                        mc "She's the girl with the purple hijab I came in with."

                    else:
                        
                        mc "She doesn't seem to be here yet but she has a purple hijab."

                    mc "She's very nervous about this place, but she's quick to open up."
                    mc "She seems to like believing in dreams and magic and other strange things."

                    hide Percy_annoyed
                    hide Percy_nervous
                    hide Percy_sad
                    hide Percy_scold
                    hide Percy_neutral
                    hide Percy_surprise
                    hide Percy_happy
                    show Percy_surprise at center, bounce

                    P "Dreams?"
                    P "You mean the dream everyone apparently had about the bird?"

                    mc "Yes! Exactly!"
                    mc "I think she believes that the dream is important."
                    mc "As if there's some kind of magic here."

                    hide Percy_surprise
                    show Percy_neutral at center, bounce

                    P "Well, that wouldn't be very hard to believe if it was true."

                    mc "What makes you think that?"

                    if metAoi:

                        P "Well, Miyagawa is from Japan."
                        P "And I'm from the UK."
                        P "And we were both brought here overnight."
                        P "Without being awoken."
                        P "We were also dreaming the same thing."

                        mc "Yeah, that..."
                        mc "That's true."
                        mc "Hey, wait, you're from the UK?"
                        mc "Same here!"

                        hide Percy_neutral
                        show Percy_happy at center, bounce

                        P "Oh!"
                        P "It's nice to meet another Brit."

                        mc "It is, isn't it?"
                        
                    else:
                        
                        P "Well, some of us are from completely differing countries."
                        P "Like one of the girls being from Japan."
                        P "And I'm from the UK."
                        P "And we were all brought here overnight."
                        P "Without being awoken."
                        P "We were also dreaming the same thing."

                        mc "Yeah, that..."
                        mc "That's true."
                        mc "Hey, wait, you're from the UK?"
                        mc "Same here!"

                        hide Percy_neutral
                        show Percy_happy at center, bounce

                        P "Oh!"
                        P "It's nice to meet another Brit."

                        mc "It is, isn't it?"

                label Percyintros_done:

                    if Percyintro_complete:

                        mc "And that seems to be all I know."

                        hide Percy_annoyed
                        hide Percy_nervous
                        hide Percy_sad
                        hide Percy_scold
                        hide Percy_neutral
                        hide Percy_surprise
                        hide Percy_happy
                        show Percy_happy at center, bounce

                        P "Thank you, [mcname]."

                        hide Percy_happy
                        show Percy_neutral at center, bounce

                        P "I'll make sure to keep all of that in mind when I talk to them."
                    
                        mc "Glad I could be of some help."
                        mc "I'll see you later then."

                        hide Percy_neutral with dissolve

                    else:

                        mc "Sorry, I don't really know anything."

                        hide Percy_annoyed
                        hide Percy_nervous
                        hide Percy_sad
                        hide Percy_scold
                        hide Percy_neutral
                        hide Percy_surprise
                        hide Percy_happy
                        show Percy_sad at center, bounce

                        P "Oh, that's alright."

                        hide Percy_sad
                        show Percy_happy at center, bounce

                        P "I'll just have to talk to them."

                        mc "I'm sorry I couldn't help."
                        mc "Though it was nice meeting you."

                        P "Yes, it was nice meeting you too."

                        hide Percy_happy
                        show Percy_sad at center, bounce

                        P "Even though this was such a short meeting."

                        hide Percy_sad
                        show Percy_happy at center, bounce

                        P "But it doesn't matter, I can always talk to you later!"
                        
                        mc "Yeah, that's true."
                        mc "I'll see you later then."

                        P "Mhmm!"
                        P "I'll see you later, [mcname]."

                        hide Percy_happy with dissolve

                    hide Percy_annoyed
                    hide Percy_nervous
                    hide Percy_sad
                    hide Percy_scold
                    hide Percy_neutral
                    hide Percy_surprise
                    hide Percy_happy 

                    jump Introductions

            label Aoi1:

                $ metAoi = True

                "Let's talk to her."
                "But she seems kinda grumpy."
                "No, not just grumpy."
                "Annoyed."
                "Angry, even."
                "But ah well, how angry can she be?"

                mc "Hey the-"

                play music "audio/bgm/LandingPage Loop.ogg" fadeout 1

                show Aoi_angry at center, bounce

                UA "Leave me alone!" with hpunch

                "Turns out..."
                "Very..."

                mc "Hey, I'm not gonna hurt you or anything."
                mc "If that's what you're worried about."
                mc "I just wanted to say hi and introduce myself."

                UA "I don't care!"
                UA "And don't treat me like some scared kid!"
                UA "That's rude!"

                "So is just yelling at me."
                
                mc "Ah, sorry."
                mc "Anyway, I'm [mcname]."

                hide Aoi_angry
                show Aoi_neutral at center, bounce
                
                UA "..."
                A "Aoi Miyagawa."

                mc "Ah, nice to meet you, Aoi-"

                A "We're not friends, don't call me that."
                A "Call me Miyagawa."

                mc "Huh? Uh, ok then."
                mc "Then, it's nice to-"

                hide Aoi_neutral
                show Aoi_sigh at center, bounce

                A "Yeah, yeah, you don't have to repeat what you said."

                "..."
                "What is WITH this girl?"
                "She wants me to be polite but can't even return it!"
                "Or maybe it's only about something she's used to."
                "Her name definitely doesn't sound English."
                
                mc "So... Your name."
                mc "It doesn't sound English at all."
                mc "Where's it from?"

                hide Aoi_sigh
                show Aoi_surprise at center, bounce
                
                A "... Japan?"

                hide Aoi_surprise
                show Aoi_neutral at center, bounce

                A "I'm Japanese."

                mc "OH!"
                mc "Sorry, it wasn't quite clicking in my head."
                
                A "Yeah. It's Aoi as in 'hollyhock', the flower, and Miyagawa as in 'shrine' and 'river'."

                mc "Oh, your names have meaning?"
                mc "That's so cool!"

                hide Aoi_neutral
                show Aoi_surprise at center, bounce

                A "Yours don't?"

                mc "No, we go based on what sounds the best."
                mc "Or, well, most of the time."
                mc "Sometimes they have intended meanings."
                mc "But yeah, it's mostly what sounds best."
                mc "Which makes me wonder why you have them."

                hide Aoi_surprise
                show Aoi_neutral at center, bounce

                A "That's so dumb."

                "Rude."
                "But..."
                "Yeah, it is kinda dumb."
                "Especially since Aoi's name is so poetic and has pretty meanings..."
                "And then we have names like 'Oliver'."
                "Who would name their kid OLIVER?"
                "..."
                "Would I?"

                hide Aoi_neutral
                show Aoi_sigh at center, bounce

                A "And to answer your question..."

                hide Aoi_sigh
                show Aoi_neutral at center, bounce

                A "We've always had a history of believing that names are sacred."
                A "Certain names are even used in anime to hint at evil characters."

                hide Aoi_neutral
                show Aoi_sigh at center, bounce

                A "Like that villain whose last name has the characters for 'death', 'grip' and 'tree'."

                hide Aoi_sigh
                show Aoi_neutral at center, bounce

                A "Our names can also be spelled and pronounced in different ways."
                A "This changes the meaning. Haruto, for example, can either mean 'sunlight' and 'to soar'."
                A "Or 'big' and 'soar'." 
                A "My name, Aoi, can also mean 'blue' if written in a different way."
                
                mc "Oh, that's so interesting!"
                
                "Hah, that'd be some funny irony if that was how her name was written."
                "Or... Would it? Since the opposite of blue is actually orange?"

                mc "You know a lot about this."

                hide Aoi_neutral
                show Aoi_angry at center, bounce
                
                A "Well, obviously!"
                A "What did you expect?"
                A "For me to be clueless about my own name?"

                mc "No, not at all!"
                mc "It's just impressive."
                mc "I can't even remember what's happening around me most of the time."
                mc "Never mind remember that."

                hide Aoi_angry
                show Aoi_sigh at center, bounce

                A "Yeah... I can tell..."

                "Again with the rudeness."
                "The more I talk to this girl, the more I wish her name wasn't so pretty."
                "It doesn't suit her at all."

                mc "So, I'm guessing you're all the way from Japan, huh?"

                hide Aoi_sigh
                show Aoi_neutral at center, bounce
                
                A "Well, obviously."

                mc "It must be difficult being so far from home..."
                mc "Wherever we are..."

                hide Aoi_neutral
                show Aoi_angry at center, bounce

                A "Wow, what made you think that?"

                hide Aoi_angry
                show Aoi_sad at center, bounce

                A "I'm missing out on school."
                A "I'm missing out on the new trends."
                A "And I'm missing out on my childhood."
                A "All for some dumb show I didn't ask to be a part of!"
                A "And now I'm stuck with morons who think nothing more than 'oh, this is strange'!"

                mc "Hey now, that's too far."

                hide Aoi_sad
                show Aoi_angry at center, bounce

                A "AARGH, who CARES!" with hpunch
                A "I wanna go home!"
                
                mc "We all do."
                mc "And don't worry, I'm sure we won't be here for long!"
                mc "Everyone and everything will be waiting for you when you get home."

                A "Ugh, would you shut up?!"
                A "People like you are so annoying!"
                
                mc "Hey, I was only trying to make you feel better!"

                A "Well it's not working!"
                A "Adults like you are the WORST!" 

                A "Because you're nothing but liars!"
                A "And I hate liars!"

                "God, so immature."
                "How old are you?"
                "5?"
                "But she does seem pretty stressed out."
                "So maybe I shouldn't be TOO harsh on her?"

                menu:

                    "God you're rude as hell.":
                        jump Aoichoice1_Rude
                    "I'm sorry.":
                        jump Aoichoice1_Sorry

                label Aoichoice1_Rude:

                    $ annoyedAoi = True

                    mc "God you're a rude brat."

                    hide Aoi_angry
                    show Aoi_surprise at center, bounce

                    A "..."
                    A "You..."

                    hide Aoi_surprise
                    show Aoi_angry at center, bounce

                    A "What gives you the right to call me a brat?!"
                    A "Actually, no, I don't care!"
                    A "Leave me alone!"

                    A "NOW!" with hpunch

                    mc "Geez, fine, I'll go."

                    hide Aoi_angry with dissolve

                    jump Introductions

                label Aoichoice1_Sorry:

                    "Ugh, screw it."
                    "I'll just apologise."
                    "I have a feeling I shouldn't go pissing everyone off so soon."
                    "Especially since I'm in a TV show."
                    "..."
                    "That was concerningly easy to forget..."

                    mc "You're right."
                    mc "Wishful thinking isn't helpful at all."
                    mc "Especially considering how serious are situation is."
                    mc "I'm sorry."

                    hide Aoi_angry
                    show Aoi_neutral at center, bounce

                    A "..."

                    hide Aoi_neutral
                    show Aoi_happy at center, bounce

                    A "Hah, finally an adult who can apologise."
                    
                    "Oh my god she can smile!"
                    "I'm guessing this means I'm starting to get on her good side now."
                    "Which is a good thing."

                    mc "Hah, well it's pretty much standard to apologise if you mess up."

                    A "Yeah, that's what you'd expect."
                    A "But you'd be surprised at how many refuse to apologise simply because I'm a kid."
                    
                    mc "Really?!"
                    mc "I knew about the patronizing but not that."
                    mc "Does it really happen that often?"

                    A "Oh, yeah."

                    hide Aoi_happy
                    show Aoi_sigh at center, bounce

                    A "It's so annoying."
                    A "Adults are so annoying."

                    mc "Hey, we're not all that bad."

                    hide Aoi_sigh
                    show Aoi_happy at center, bounce
                    
                    A "Yeah, maybe not..."

                    hide Aoi_happy
                    show Aoi_neutral at center, bounce

                    A "But there are still too many of you that are."

                    mc "Well, you aren't wrong there."
                    mc "Though kids are just as annoying as we are, if not more."
                    mc "Anyway, I should start introducing myself to the others."
                    mc "Try not to yell at anyone else, alright?"

                    A "If they annoy me, I do what I want with them."

                    "Of course..."

                    mc "See you later Miyagawa."

                    hide Aoi_neutral with dissolve

                    jump Introductions

            label Holly1:
                
                $ metHolly = True

                "Let's talk to that person over there."
                "They look like they're..."
                "Oh come on!"
                "They're playing video games?!"
                "Now I wish I brought my console!"

                mc "Hey, what are you playing?"

                show Holly_neutral at center, bounce

                play music "audio/bgm/8Bit Tragic Mistake Loop.ogg" fadeout 1

                UH "voidmons."

                mc "voidmons?"
                mc "Haha, that sounds interesting."

                hide Holly_neutral
                show Holly_distracted at center, bounce

                UH "Mhmm..."

                "So... Not quite one for talking..."
                
                mc "So, what's your name?"

                UH "..."

                H "Holly."

                mc "Huh, Holly..."
                
                H "Weird, I know."
                
                hide Holly_sad
                hide Holly_happy
                hide Holly_neutral
                hide Holly_nervous
                hide Holly_surprise
                hide Holly_distracted
                show Holly_neutral at center, bounce
                
                H "Since I'm a guy."

                mc "I wasn't thinking it was weird."
                
                "It's a little weird."
                "Though in a weird way, it suits him."
                
                mc "What led you to having Holly as a name, though?"
                mc "If you don't mind me asking."
                
                H "..."

                hide Holly_neutral
                show Holly_distracted at center, bounce
                
                H "My mom wanted a girl."
                H "Got me instead."
                
                mc "Oh..."

                "Oof..."
                "That is..."
                "Definitely a thing..."
                "Let's change the subject."

                menu:

                    "You're being really rude.":
                        jump Hollychoice1_rude
                    "Tell me about the game you're playing.":
                        jump Hollychoice2_game
                
                label Hollychoice1_rude:

                    $ annoyedHolly = True

                    mc "You're being really rude right, now, you know that?"

                    hide Holly_neutral
                    show Holly_distracted at center, bounce

                    H "Ok."

                    mc "You don't care about how rude you're being?"

                    H "..."

                    mc "Hello? I'm talking to you."

                    H "..."

                    "He's blanked me..."
                    "..."
                    "..."
                    "..."
                    "It's so awkward now..."
                    "Whatever, I'll just leave." 

                    hide Holly_distracted with dissolve

                    jump Introductions
                    

                label Hollychoice2_game:

                    mc "So, about your game..."
                    mc "I think I've sort of heard about it."
                    mc "But what's it about?"

                    hide Holly_distracted
                    show Holly_nervous at center, bounce

                    H "..."
                    H "It's just about catching creatures that resemble emotions."

                    mc "Hmmm..."
                    mc "Nope, turns out I didn't, haha."
                    mc "I know Pokepets, but not voidmons."

                    hide Holly_nervous
                    show Holly_neutral at center, bounce

                    H "Well, Pokepets was the main inspiration."

                    mc "Really?"

                    "I definitely should have expected that..."
                    "And yet I didn't."
                    "Man, my brain has been through too much today."

                    H "Yeah."
                    H "The person who created the game is a huge fan of Pokepets, with a lot of plushies."

                    mc "Oh! So do I!"
                    mc "I have a ton of plushies!"

                    "Though some of them had to retire to the end of my bed because I broke them from using them all as pillows."
                    "But nobody needs to know that."

                    hide Holly_neutral
                    show Holly_happy at center, bounce

                    H "Same here."
                    H "I have a lot of merch from my favourite games."

                    "Oh, we're getting somewhere now!"
                    "Let's see how long we can keep it going."

                    mc "Ooh, what kind of games do you like?"

                    hide Holly_happy
                    show Holly_nervous at center, bounce

                    H "Well, I like story games."
                    H "Though they also need good visuals."
                    H "So, I like games like Michigan: Become Human, Soulfarer and Dark Dead Deception."

                    mc "Oh, I like those games too!"
                    mc "Since you like good visuals, I'm guessing that you like newer games then."

                    hide Holly_nervous
                    show Holly_neutral at center, bounce

                    H "Yeah, that's right."
                    H "Some older 2D games are pretty fun, but old 3D games suck."
                    H "I can't get myself into the story if the character's mouths aren't moving."

                    hide Holly_neutral
                    show Holly_annoyed at center, bounce

                    H "And don't get me started about the controls and functions of REALLY old games."

                    hide Holly_annoyed
                    show Holly_distracted at center, bounce

                    H "Very few old games are successful."
                    H "Or, as some would day, timeless."
                    H "But not many."

                    mc "Wow, he's definitely passionate about this."

                    menu:

                        "Same here.":
                            jump Hollychoice3_Compliment
                        "You're gonna hate me then.":
                            jump Hollychoice3_Insult

                    label Hollychoice3_Compliment:

                        mc "I know exactly how you feel."
                        mc "Old games just don't hit as well as newer games."
                        mc "Yeah, it's cool to play them for nostalgia."
                        mc "But that doesn't mean we have to be stuck in the past."

                        H "Mhmm."
                        H "That's what I tell people."
                        H "Especially when the games are objectively bad."

                        mc "I know, right?!"
                        mc "These people will put old and bad games on a pedestal like it's the best game ever made, when the stories are often so poorly written."
                        mc "And don't even get me started on the graphics."
                        mc "Most are decent, I guess, but some are just so bad that the good story gets dragged down by them."
                        mc "I don't want to see every individual pore in a character's skin, but I want some decent lip-syncing at least."

                        hide Holly_distracted
                        show Holly_neutral at center, bounce

                        H "Yeah, that does get irritating."
                        H "Some of those old games, and even anime, are incredibly overrated."
                        H "Especially when they just keep going and they don't stop."
                        H "It's good for those with lifelong obsessions and games that don't have set stories."
                        H "But sometimes it just ruins the stories."

                        mc "Oh yeah, definitely."
                        mc "There are certain games where it makes sense."
                        mc "Like Pokepets."
                        mc "It makes more sense that there at a lot of games, as there's no plot between the regions that makes it seem strange."
                        mc "And the regions are now based on countries, not just areas in Japan."
                        mc "And if the whole thing is to catch them all, then obviously that involves going around the world."
                        mc "So it makes sense. It's just an issue of the repetitive story."

                        hide Holly_neutral
                        show Holly_distracted at center, bounce

                        H "Hmm."

                        hide Holly_distracted
                        show Holly_neutral at center, bounce

                        H "But you could argue that the repetitive story is what has kept so many fans."
                        H "A game with a story that is too different from the others tends not to do as well as a game whose story doesn't change much."

                        hide Holly_neutral
                        show Holly_happy at center, bounce

                        H "Though, it is nice to have more unique storylines every so often."

                        mc "Yeah, I guess you're right."

                        "He's definitely passionate about this."
                        "And he's definitely in a good mood now."
                        "Though I really need to introduce myself to the others."

                        mc "Well, I should go introduce myself to the others."
                        mc "It was nice meeting you, Holly."
                        mc "Have fun with your game."

                        H "I will."
                        H "See you later."

                        hide Holly_happy with dissolve

                        jump Introductions

                    
                    label Hollychoice3_Insult:

                        mc "You're gonna hate me then..."
                        mc "Because I love older games."
                        mc "I can't stand newer games."
                        mc "Especially with Pokepets."
                        mc "It's too easy now, which drains the fun."

                        hide Holly_distracted
                        show Holly_surprise at center, bounce

                        H "..."

                        hide Holly_surprise
                        show Holly_distracted at center, bounce

                        H "I don't hate you...?"
                        
                        hide Holly_distracted
                        show Holly_annoyed at center, bounce

                        H "But you realise that Pokepets is built for KIDS, right?"
                        H "Obviously the new games are going to be more easy and accessible."

                        mc "Well yeah, I guess."
                        mc "But still, it's too easy, which makes most of the games suck."
                        mc "There was one newer game that I had a hard time."
                        mc "But that's just because you battle the guy 3 times with no breaks."
                        mc "Plus, I don't like any of the new designs."
                        mc "The older ones are so much better."

                        hide Holly_annoyed
                        show Holly_distracted at center, bounce

                        H "Are they really or is it nostalgia?"
                        
                        "God what is with this guy?"

                        mc "So what if it's nostalgia?"
                        mc "Nostalgia can be an amazing way of keeping an audience."
                        mc "Which is useful for long-time franchises, like Pokepets."
                        mc "But you have to pay attention to that audience."

                        H "Says who?"

                        mc "Uhh..."
                        mc "Anyone good at promoting things?"

                        H "But there's a diffence between smart marketing and being stagnant."
                        H "Catering to an older audience is fine and all."
                        H "But at some point they just stop making progress and become stagnant."
                        H "If they just stop making Pokepets designs, you're gonna start getting annoyed."
                        H "You'll stop seeing the point in playing a game that's the same as the others."
                        H "And if we applied your logic to the very first game."
                        H "We'd be stuck with 150."
                        H "All of your favourite Pokepets after the first game?"
                        H "Poof."

                        "He's definitely used to arguing about this."
                        "That's so ridiculous..."
                        "And he could afford to just glance up at me once in a while."

                        mc "Well, I still think that the newer games suck..."

                        H "Mmhmm."
                        H "That opinion is valid."

                        hide Holly_distracted
                        show Holly_neutral at center, bounce

                        H "But it's not the right one."

                        mc "I never said it was!"

                        hide Holly_neutral
                        show Holly_distracted at center, bounce
                        
                        H "Mhmmm..."

                        "This kid..."
                        "Whatever!"
                        "I'm done talking to him."
                        "How annoying."

                        hide Holly_distracted with dissolve

                        jump Introductions

            label SebastianandTsun1:

                $ metSebastian = True
                $ metTsun = True

                "Let's talk to them."
                "They look like they were just having a serious conversation."
                "Or..."
                "That is if you ignore the guy in the lab coat."

                play music "audio/bgm/Mr Snarky Destructoid Loop.ogg" fadeout 1

                show Sebastian_neutral at Ssleft
                show Tsun_happy at sright, bounce

                UT "Oh, you have no idea how great it is to see another doctor here."

                US "I'm sure..."

                hide Tsun_happy
                show Tsun_neutral at sright, bounce
                
                UT "Even if we are from drastically different fields, I get to have a conversation with another intellectual."
                
                US "Mm..."

                hide Sebastian_neutral
                show Sebastian_happy at sleft, bounce

                US "It is certainly an excellent opportunity."
                US "To be able to discuss my work with somebody who will understand."

                hide Sebastian_happy
                show Sebastian_neutral at Ssleft, bounce

                US "Hm?"

                "Oh, he noticed me."

                hide Tsun_neutral
                show Tsun_surprise at sright, bounce

                UT "Huh? What are you-"

                hide Tsun_surprise
                show Tsun_happy at sright, bounce

                UT "Oh, hello!"

                "They both noticed me."

                hide Tsun_happy
                show Tsun_neutral at sright, bounce

                UT "You must be the person sleeping on the first floor."
                
                mc "Uh, yeah, that's me."
                mc "I'm [mcname]."
                mc "And you two?"

                T "Oh, I'm Tsun."

                hide Tsun_neutral
                show Tsun_smug at sright, bounce

                T "Dr. Alexander Tsun."
                T "But Tsun or Dr. Tsun will do."

                hide Tsun_smug
                show Tsun_neutral at sright, bounce

                T "And this is Dr. Sebastian Alves."

                hide Sebastian_neutral
                show Sebastian_sigh at sleft, bounce

                S "Just call me Sebastian."

                hide Sebastian_sigh
                show Sebastian_neutral at Ssleft, bounce

                S "We were just discussing our medical fields."

                hide Tsun_neutral
                show Tsun_happy at sright, bounce
                
                T "Oh, yes!"
                T "I'm a general surgeon."

                hide Tsun_happy
                show Tsun_smug at sright, bounce

                T "That means I specialise in a wide range of surgeries."

                "Yeah, I know what general surgeon means."

                hide Tsun_smug 
                show Tsun_neutral at sright, bounce

                T "And Sebastian here is a criminal psychologist."
                T "That means he works to help offenders."

                hide Sebastian_neutral
                show Sebastian_happy at sleft, bounce

                S "I work in different settings to assess and treat criminals."
                S "Along with occasionally researching why they might commit crimes."
                S "All in hopes of rehabilitation."
                
                mc "Wow, that's..."
                mc "That's amazing."

                hide Tsun_neutral
                show Tsun_smug at sright, bounce

                T "Hah, I know."

                "Ok, calm down now."
                
                S "Hm..."

                hide Sebastian_happy
                show Sebastian_neutral at Ssleft, bounce
                
                S "So, are you also a doctor?"

                menu:
                    "Yes.":
                        jump SebastianandTsun_choice1_lie
                    "No.":
                        jump SebastianandTsun_choice1_truth
                    
                label SebastianandTsun_choice1_lie:

                    $ liedtoSandT = True

                    "Man, I wanna sound cool too."
                    "I know, I'll lie!"
                    "That'll make me seem cool!"

                    mc "Oh, yeah."
                    mc "I am."

                    hide Tsun_smug
                    show Tsun_surprise at sright, bounce

                    T "Oh? What's your field then?"

                    "Oh, the big question."
                    "Shit, what do I go with?"
                    "I'll just go simple."

                    mc "I'm a GP."
                    mc "General practitioner."

                    hide Tsun_surprise
                    show Tsun_happy at sright, bounce

                    T "Ah, is that so?"
                    
                    "ughhh, no, this isn't right..."
                    "I can't just lie to them."

                    mc "..."
                    mc "... No..."
                    mc "I lied, I just wanted to sound cool."
                    mc "I'm actually just a bartender."

                    S "..."

                    hide Sebastian_neutral
                    show Sebastian_sigh at sleft, bounce

                    S "Yeah, I expected that."

                    "And what's THAT supposed to mean?"

                    hide Tsun_happy
                    show Tsun_sad at sright, bounce

                    T "You didn't have to lie to us, you know."

                    hide Tsun_sad
                    show Tsun_happy at sright, bounce
                    
                    T "And hey, you keep us busy with all the drunks."

                    mc "... I don't think that's a good thing."
                    mc "And we don't keep you busy at all."
                    mc "It's the drunks that do that by finding ways of getting more alcohol."
                    
                    T "Ah, relax, I was just joking."

                    hide Tsun_happy
                    show Tsun_neutral at sright, bounce

                    T "But you certainly don't need to lie about your job."
                    
                    mc "Yeah, sorry."

                    hide Sebastian_sigh
                    show Sebastian_neutral at Ssleft, bounce

                    S "Don't apologise."
                    S "You're acting like you decieved us."
                    S "But you couldn't even last a minute before you told us the truth."

                    "..."
                    "Yeah, that's a tad embarrassing."

                    jump SebastianandTsun_choice1_done
                    

                label SebastianandTsun_choice1_truth:

                    mc "No, I'm not."
                    mc "I'm just a bartender."

                    hide Tsun_smug
                    show Tsun_happy at sright, bounce

                    T "Oh, nice!"

                    hide Tsun_happy
                    show Tsun_neutral at sright, bounce

                    T "Very simple."
                    T "But it's the simple jobs that mean the most."
                    
                    "He's just trying to make me feel better..."

                    jump SebastianandTsun_choice1_done

                label SebastianandTsun_choice1_done:

                    hide Tsun_neutral
                    show Tsun_happy at sright, bounce
                    
                    T "So!"

                    hide Tsun_happy
                    show Tsun_neutral at sright, bounce

                    T "I guess that makes us two the only doctors."
                    
                    S "It would seem so."

                    hide Tsun_neutral
                    show Tsun_sad at sright, bounce
                    
                    T "I'll admit, it's a slight disappointment that we're the only ones."

                    hide Tsun_sad
                    show Tsun_happy at sright, bounce

                    T "But at least I have SOMEONE to have enlightening conversations with."

                    S "That is true."

                    hide Sebastian_neutral
                    show Sebastian_sigh at sleft, bounce

                    S "Though..."
                    S "It's been a while since I've engaged in idle chit-chat."

                    hide Sebastian_sigh
                    show Sebastian_sad at sleft, bounce

                    S "..."
                    S "It's strange, to say the least."

                    mc "Really?"
                    mc "Not even with your co-workers?"
                    mc "Or your family?"

                    S "No."

                    hide Sebastian_sad
                    show Sebastian_neutral at Ssleft, bounce

                    S "I'm usually too busy with work to engage in small talk with my co-workers."
                    S "And so, many of our conversations are goal-oriented."
                    S "And I don't have a partner."

                    mc "Oh."
                    
                    "That's actually kind of sad."

                    hide Tsun_happy
                    show Tsun_sad at sright, bounce

                    T "Medical fields in general are very busy."
                    T "So the moments where you can actually relax are rare."
                    T "Especially enough for casual conversation."

                    hide Tsun_sad
                    show Tsun_neutral at sright, bounce

                    T "Though, in less stressful surgeries, we can have a few conversations during."

                    hide Tsun_neutral
                    show Tsun_happy at sright, bounce

                    T "And we can learn about everyone's music tastes."

                    hide Tsun_happy
                    show Tsun_annoyed at sright, bounce

                    T "Though, there are some songs I wish to unhear."
                    
                    mc "Oh, I see."
                    mc "Sebastian's work must be a lot then."

                    hide Tsun_annoyed
                    show Tsun_neutral at sright, bounce

                    T "Well, he's also a workaholic."

                    hide Sebastian_neutral
                    show Sebastian_sigh at sleft, bounce

                    S "I don't think I'd call myself that."
                    S "But yes, I'm very dedicated to my work."
                    
                    mc "Oh."
                    
                    "It sounds a bit like a workaholic."
                    "But hey, there's nothing wrong with dedication."
                    "So he could also just be enjoying his job."

                    mc "Well, there's nothing wrong with dedication."

                    hide Tsun_neutral
                    show Tsun_happy at sright, bounce

                    T "Oh, I agree!"
                    T "Though, there's a difference between being dedicated..."

                    hide Tsun_happy
                    show Tsun_neutral at sright, bounce

                    T "And letting it consume you."
                    T "Not only that but..."

                    hide Tsun_neutral
                    show Tsun_happy at sright, bounce

                    T "Somebody had to tell you that it's this guy's own fault."
                    
                    hide Sebastian_sigh
                    show Sebastian_sad at sleft, bounce

                    S "Tsun."

                    T "What?"

                    hide Tsun_happy
                    show Tsun_neutral at sright, bounce

                    T "Come on, you can't tell me you just don't have any time to talk casually with co-workers."
                    T "Everybody has time for that."
                    T "You're just obsessed with your work."
                    
                    "Yeah, he should loosen up more once we all go home."
                    "I can't even imagine the idea of being obsessed with my job."
                    "Though... Maybe if my job was something I was interested in..."
                    "Maybe I'd be just like him..."
                    "..."
                    "I'm running out of time."
                    "I should make sure to introduce myself to everyone before the meeting starts."
                    "And let these two go back to just talking to each other."

                    mc "Hey, I should get going."
                    mc "Sorry if I interrupted you guys before."

                    hide Tsun_neutral
                    show Tsun_surprise at sright, bounce

                    T "Hm?"

                    hide Tsun_surprise
                    show Tsun_happy at sright, bounce

                    T "Oh! So soon?"
                    T "Feel free to talk to us later, then."

                    hide Sebastian_sad
                    show Sebastian_neutral at Ssleft, bounce

                    S "Mhmm."

                    mc "Yeah, I'll make sure to."
                    mc "I'll see you two later then."

                    hide Tsun_happy with dissolve
                    hide Sebastian_neutral with dissolve

                    jump Introductions

            label Red1:

                $ metRed = True

                "Let's talk to him."

                if heardaboutRed:

                    "A tattoo..."
                    "He's the only one with one."
                    "He must be the guy Zach told me about."
                    "He doesn't seem so bad."

                play music "audio/bgm/vntrack13.mp3" fadeout 1

                show Red_neutral at center, bounce

                UR "Hm?"
                UR "Whaddya want?"

                "Something about this guy says bad news already."

                mc "I just wanted to say hi."
                mc "I'm [mcname]."
                mc "And you are?"

                UR "Oh, you're here to say hello."

                hide Red_neutral
                show Red_happy at center, bounce

                R "I'm Red, nice to meet ya, [mcname]." 

                "Oh, he's surprisingly friendly."
                "This is great."
                "So it was probably all in my head."

                hide Red_happy
                show Red_neutral at center, bounce

                R "You look relieved."
                R "You were expecting me to bite ya head off, weren't ya?"

                "Yes."

                mc "What? No!"
                mc "..."
                mc "Ok, kinda."

                if heardaboutRed:

                    mc "I mean, I heard from Zach about you."
                    mc "And how you laughed about hurting that maid."
                    
                    hide Red_neutral
                    show Red_nervous at center, bounce

                    R "Oh, he told you about that?"

                    hide Red_nervous
                    show Red_happy at center, bounce

                    R "Haha, I should have expected that."

                    hide Red_happy
                    show Red_neutral at center, bounce

                    R "But what was I supposed to do?"
                    R "Besides, she wasn't actually hurt."

                    hide Red_neutral
                    show Red_nervous at center, bounce

                    R "..."
                    R "Ok, she was a little hurt, but still."

                    hide Red_nervous
                    show Red_neutral at center, bounce

                    R "It's like they were all trained for self-defence or something."
                    
                    if attackedmaid:

                        mc "Yeah, I noticed that too."

                        hide Red_neutral
                        show Red_surprise at center, bounce

                        R "What, you attack one too?"

                        hide Red_surprise
                        show Red_happy at center, bounce

                        R "Hah, you were really scared of me when you did the same thing!"
                        R "Weird how that works, ain't it?"

                        mc "Hey, we aren't the same."
                        mc "I regret it a lot."
                        mc "And you laughed about it to him."

                        hide Red_happy
                        show Red_neutral at center, bounce

                        R "It was a stress laugh."

                        "Sure it was, bucko."

                        mc "And you actually hurt yours."
                        mc "While mine just laughed it off."

                        R "Eh, all she got was a sore wrist and arm."
                        R "No biggie."

                        "No biggie?"
                        "That's all he has to say?"
                        "No regret?"

                    else:
                        
                        mc "And it was a good thing they were too."
                        mc "Cause from the sounds of it, you could have done serious harm."

                        hide Red_neutral
                        show Red_happy at center, bounce

                        R "Ah, relax."
                        R "Like I said, she's fine."
                        R "Just a sore arm."
                        R "It's not like I killed her or something."

                        mc "Any kind of damage done to anyone in your first hour here is not a good sign."

                        hide Red_happy
                        show Red_neutral at center, bounce

                        R "Again, relax."
                        R "It was just fight or flight instincts."
                        R "I mean, ya gotta understand the situation, right?"

                        mc "Well, yeah, but still."
                        mc "You gotta-"
                        
                        R "You're a 'freeze' person, aren't you?"

                        mc "What?"
                        mc "I mean, I guess?"

                        "Yes."
                        "Very much so."
                        "It's embarrassing."
                        "But I'm a bad liar."
                        "So..."

                        hide Red_neutral
                        show Red_happy at center, bounce

                        R "Yeah, ya seem like the type."
                        R "To freeze up like a deer in the headlights."

                        if grabbed_a_weapon:
                            
                            mc "I mean, I didn't completely freeze."
                            mc "I grabbed something in case I got attacked."
                            mc "I just didn't go through with it."

                            R "Right, of course ya did."

                            mc "I did!"

                            R "Sure ya did!"

                        else:

                            "Yeah, let's be honest, he's not completely wrong."
                            "I would have been screwed if that was an actual attacker."

                            mc "I guess you're not entirely wrong."

                            R "Hah, of course I'm not!"
                            R "People like you are so easy to predict."
                            R "It's funny."

                            mc "Uh, thanks, I guess?"
                
                else:

                    mc "I mean, you're not exactly the most friendly looking person."

                    hide Red_neutral
                    show Red_surprise at center, bounce

                    R "Eh? Am I not?"
                    R "Huh, maybe that's why some of the people here have been avoiding me."

                    hide Red_surprise
                    show Red_nervous at center, bounce

                    R "Is it the tattoos?"
                    
                    mc "I don't think it is?"
                    mc "It's hard to describe."

                    hide Red_nervous
                    show Red_surprise at center, bounce

                    R "So, it's just general vibe then?"

                    hide Red_surprise
                    show Red_happy at center, bounce

                    R "Weird."

                hide Red_happy
                hide Red_neutral
                show Red_neutral at center, bounce

                R "Well, anyway, since you're here, ya probably want to know more about me, right?"
                
                mc "I mean, it'd be great if you told me about yourself."

                hide Red_neutral
                show Red_happy at center, bounce
                
                R "Heh, then tell ya, I will."

                hide Red_happy
                show Red_neutral at center, bounce

                R "So, first things first, I'm from Ohio."

                mc "Ohio in the US?"

                R "Yeah, that's right."

                hide Red_neutral
                show Red_nervous at center, bounce

                R "Not always proud of that part, though."

                hide Red_nervous
                show Red_neutral at center, bounce

                R "Anyway, I'm 27, I'm a mechanic."
                R "I'm allergic to shellfish."
                R "And I can't see that well."
                R "My eyesight isn't the best and it's worse short-distance."

                mc "Oh, I see."
                mc "That's interesting!"

                R "Eh, not really."
                R "Despite my looks, I'm not actually that interesting."

                hide Red_neutral
                show Red_happy at center, bounce

                R "So, anything else ya wanna know about me? Or is that it?"

                mc "Yeah, where'd you get your tattoos from?"

                hide Red_happy
                show Red_surprise at center, bounce

                R "Hm? Oh, these things?"

                hide Red_surprise
                show Red_happy at center, bounce

                R "I'm a criminal!"
                R "Got 'em done by my crew."
                R "This place actually somehow got me out of jail for a hit and run."

                "..."
                "What?"

                mc "You're a what?"

                R "Haha, I'm just messing with you."

                hide Red_happy
                show Red_neutral at center, bounce

                R "I actually just thought they were really cool and I got bored of not having one."

                hide Red_neutral
                show Red_happy at center, bounce

                R "I always wanted to be a tattoo artist, actually."

                hide Red_happy
                show Red_nervous at center, bounce

                R "But I'm not that good at art and I worry that I'd be too heavy-handed for clients."
                
                mc "Oh."
                mc "I mean, I was kind of expecting for you to be joking."
                mc "It was just kinda baffling to hear."

                hide Red_nervous
                show Red_happy at center, bounce

                R "Haha, yeah, it's funny seeing people look so shocked when I say things like that."

                mc "So, do they have a meaning?"

                hide Red_happy
                show Red_neutral at center, bounce

                R "The one on my neck?"

                hide Red_neutral
                show Red_happy at center, bounce

                R "Not at all."

                hide Red_happy
                show Red_neutral at center, bounce

                R "I was just newly 18 and wanted something cool."
                R "And the one on my arm?"

                hide Red_neutral
                show Red_nervous at center, bounce

                R "Well, I didn't really intend for it to have one."
                R "I honestly just saw some guy with it and wanted it too."
                R "And yes, I was still a young adult at the time."
                R "19 specifically."
                R "And I was still obsessed with looking cool at the time."

                hide Red_nervous
                show Red_neutral at center, bounce

                R "But a few years after I got it, I learned that one of its meanings is 'duality'."
                R "So, like, infinity and death, good and evil and whatnot."

                hide Red_neutral
                show Red_happy at center, bounce

                R "Which I find pretty cool."

                mc "Oh, that IS pretty cool."

                R "Yep, do you have any tats?"

                "Tats?"

                mc "No, I don't."
                mc "Big fear of needles."
                mc "And pain."

                hide Red_happy
                show Red_surprise at center, bounce

                R "Really?"
                R "How are you... How old are you?"

                mc "25."

                R "Jeez, you look young for 25."

                "Uhh... Thanks?"
                "I guess?"

                R "Anyway, how are you 25 and still have a fear of needles and pain?"

                "Rude."

                mc "I just never had good experiences with needles and doctors."
                mc "And everyone has a fear of pain."

                hide Red_surprise
                show Red_neutral at center, bounce
                
                R "I don't."

                "Uhh, congrats?"

                mc "Well, I do."
                mc "And it's not fun to live with."
                
                R "Then I won't judge you about it anymore."
                R "It's just weird to me, is all."
                R "Like, I expect it with kids, but not adults."

                "Of course it's weird to you."

                R "So, anyway, any more questions?"

                mc "No, none come to mind."

                if metBerry or metAoi or metHolly or metSebastian or metPercy:

                    mc "Though, so far you're the only one who's been this open to sharing things about yourself."

                    hide Red_neutral
                    show Red_happy at center, bounce

                    R "Hah, really?"
                    R "That's surprising."

                    mc "not really."

                    hide Red_happy
                    show Red_neutral at center, bounce

                R "Then we're done?"

                hide Red_neutral
                show Red_happy at center, bounce

                R "Great, then I'll see ya later?"

                mc "I guess."

                "It feels a bit like he just wants me gone."

                if metAoi or metHolly or metZach:

                    "Though, I guess he wouldn't be the only person to be like that."

                "But whatever, I guess I'll just leave?"

                mc "Uh, bye then."

                hide Red_happy
                show Red_neutral at center, bounce

                R "Yep, see ya."

                "Weird."

                hide Red_neutral with dissolve

                jump Introductions

            label Azzy1:

                "Let's talk to him."
                "He looks like he's lost in thought."

                jump Introductions

            label Mina1:

                "Let's talk to her."
                "She looks tired."

                jump Introductions
            
            label Alicantoarrives:

                "I think that was everyone."
                "I wonder when that Alicanto guy's gonna arrive."

                play music "audio/bgm/Of Far Different Nature - Intervals [v2] (CC-BY 4.0).ogg" fadeout 1.0

                show Alicanto_Bow at center, bounce

                Al "Hello, my fellow contestants!"

                "Speak of the devil..."

                hide Alicanto_Bow
                show Alicanto_happy at center, bounce

                Al "I hope you don't mind, I gave you all time to get to know each other before we begin."

                "I do mind."
                "His movements remind me of a bird."
                "In a strange way."
                "It's hard to describe."

                hide Alicanto_happy
                show Alicanto_neutral at center, bounce

                Al "Now, once everyone is ready, take your seats."
                Al "And then I'll explain everything."

                "Let's sit down then..."
                "I'm sat next to Holly and Aoi."

                jump Alicantoexplanation
            
        label Alicantoexplanation:

            "So, let's hear this explanation."

            jump ch06

    label alreadymet:

        "I already spoke to them."

        return 

    label notdone1:

        "No, I'm not."

        jump Introductions
        
    


