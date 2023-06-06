#characters
define mc = Character("[mcname]")

#unkowns + extras
define U = Character("Unknown", color = "#FFFFFF")

define chef = Character("Chef", color = "#FFFFFF")

define USa = Character("Girl in purple", color = "#8a6ed6")
define UZ = Character("Man in blue", color = "#6991c5")
define UB = Character("Girl with skates", color = "#f1d69b")
define UH = Character("Person with long hair", color = "#a68fcc")
define UA = Character("Girl in uniform", color = "#ff8686")
define UT = Character("Man in lab coat", color = "#d8da69")
define US = Character("Man with gloves", color = "#4fac88")
define UP = Character("Woman with dyed hair", color = "#d899be")
define UM = Character("Girl with pink hair", color = "#7ce772")
define UAz = Character("Boy with pink hair", color = "#ffc5db")
define UE = Character("Man with scar", color = "#ff9e81")
define UF = Character("Woman with green hair", color = "#64ebd4")

#actual cast
define Sa = Character("Safirah", color = "#8a6ed6")
define Z = Character("Zach", color = "#6991c5")
define B = Character("Berry", color = "#f1d69b")
define H = Character("Holly", color = "#a68fcc")
define A = Character("Aoi", color = "#ff8686")
define T = Character("Tsun", color = "#d8da69")
define S = Character("Sebastian", color = "#4fac88")
define P = Character("Percy", color = "#d899be")
define M = Character("Mina", color = "#7ce772")
define Az = Character("Azzy", color = "#ffc5db")
define E = Character("Red", color = "#ff9e81")
define F = Character("Flora", color = "#64ebd4")

define Al = Character("Alicanto", who_color = "#ffef9f", what_color = "#ffef9f")


#defaults
default late = False
default dressedbest = False
default casualfit = False
default PJs = False
default metSafirah = False
default LeftwithSafirah = False
default metZach = False
default LeftwithZach = False
default annoyedZach = False
default metBerry = False
default metHolly = False
default annoyedHolly = False
default metAoi = False
default metTsun = False
default metSebastian = False
default metPercy = False
default metMina = False
default metAzzy = False
default metRed = False
default metFlora = False
default kickedoutkitchen = False
default ontopfloor = False
default onsecondfloor = False
default onfirstfloor = True
default ongroundfloor = False
default inbasement = False
default heardaboutRed = False

#bg images
image fadeout = "Images/Fade-out.png"
image flashback = "Images/Flashback.png"
image mcroom = "images/backgrounds/new mc room.jpg"
image mcbalcony = "Images/backgrounds/Balcony.jpg"
image Hall = "images/backgrounds/Hall.jpg"
image GHall = "images/backgrounds/Ground Hall.jpg"
image Kitchen = "images/backgrounds/Kitchen.jpg"
image Droom = "images/backgrounds/Dining room.jpg"

image Safirah_neutral = "Images/Safirah Neutral.png"
image Safirah_surprise = "Images/Safirah Surprise.png"
image Safirah_mad = "Images/Safirah mad.png"
image Safirah_nervous = "Images/Safirah nervous.png"
image Safirah_happy = "Images/Safirah Happy.png"
image Safirah_cry = "Images/Safirah Cry.png"

image Zach_neutral = "Images/Zach Neutral.png"
image Zach_glare = "Images/Zach glare.png"
image Zach_angry = "Images/Zach Angry.png"
image Zach_laugh = "Images/Zach Laugh.png"
image Zach_nervous = "Images/Zach Sad.png"
image Zach_surprise = "Images/Zach Surprise.png" 

#player name input code begins

label ch04:
 
 "I should get changed quickly then."
 "Let's see what I have here..."

 jump clotheschoice

label clotheschoice:

    menu:
    
        "Fancy suit.":
            jump choice11_fancy
        "Shirt, jacket and Jeans.":
            jump choice11_casual
        "Pjs will do.":
            jump choice11_PJs

    label choice11_fancy:

        $ fancy = True
        $ casual = False
        $ PJs = False

        "I'll try to look my best today."
        "It'd be embarrassing if everyone else has and I'm not."

        "So let's get changed!"

        scene fadeout
        with Dissolve(.5)
    
        pause .5

        scene mcroom
        with Dissolve(.5)

        "Yeah!"
        "I look really cool right now!"
        "Though, I'm a bit worried it'll be too much."
        "Especially considering the situation."

        menu:

            "Let's go casual instead.":
                jump choice11_casual
            "Let's just go in PJs.":
                jump choice11_PJs
            "No, this is great.":
                jump choice11_done

    label choice11_casual:

        $ fancy = False
        $ casual = True
        $ PJs = False

        "I want to try, but let's not do anything too crazy."
        "It'd be embarrassing to be too fancy if nobody else is."

        "So let's get changed."

        scene fadeout
        with Dissolve(.5)
    
        pause .5

        scene mcroom
        with Dissolve(.5)

        "I look fine."
        "I don't look like a lazy mess."
        "But I also don't look that fancy."
        "It's just..."
        "An outfit."
        "..."
        "Is this too little?"

        menu:

            "Just this is too much.":
                jump choice11_PJs
            "Let's go fancy.":
                jump choice11_fancy
            "No, this is great.":
                jump choice11_done

    label choice11_PJs:

        $ fancy = False
        $ casual = False
        $ PJs = True

        "No. They kidnapped me, they don't deserve my effort."

        if fancy or casual:

            scene fadeout
            with Dissolve(.5)
    
            pause .5

            scene mcroom
            with Dissolve(.5)

        else:

            "Yeah, so I won't try!"

        "..."
        "Although..."
        "I'm gonna be shown to the public."
        "It'd be humiliating to go like this."

        menu:

            "Let's go casual instead.":
                jump choice11_casual
            "Let's go fancy.":
                jump choice11_fancy
            "No, this is great.":
                jump choice11_done


label choice11_done:

    "Yeah, I look fine like this!"
    "So let's go!"
    "..."
    "The idea of leaving this room's kinda scary."
    "But you know what? I'd rather not be late."
    "Who knows what will happen if I am."

    scene fadeout
    with Dissolve(.5)
    
    pause .5

    scene Hall
    with Dissolve(.5)

    "Ok..."
    "I'm out..."
    "And I wasn't instantly killed or ambushed."
    "That's great."
    "..."
    "I feel like I shouldn't be so worried about dying."
    
    "Anyway, where did the maid say to go?"

    jump stairs1

label stairs1:

    menu:

        "Top floor.":
            if ontopfloor:
                call onfloor from _call_onfloor
                jump stairs1
            else:
                jump top_floorchoice1
        "Second floor.":
            if onsecondfloor:
                call onfloor from _call_onfloor_1
                jump stairs1
            else:
                jump second_floorchoice1
        "First floor":
            if onfirstfloor:
                call onfloor from _call_onfloor_2
                jump stairs1
            else:
                jump first_floorchoice1
        "Ground floor.":
            if ontopfloor:
                call onfloor from _call_onfloor_3
                jump stairs1
            else:
                jump ground_floorchoice1
        "Basement.":
            if inbasement:
                call onfloor from _call_onfloor_4
                jump stairs1
            else:
                jump basement1

label top_floorchoice1:

    $ ontopfloor = True
    $ onsecondfloor = False
    $ onfirstfloor = False
    $ ongroundfloor = False
    $ inbasement = False

    "Let's go to the top floor!"

    scene fadeout
    with Dissolve(.5)
    
    pause .5

    scene Hall
    with Dissolve(.5)

    "Oh, it pretty much looks the same as the first floor."
    "But there are 5 doors with numbers."
    "This must be where the other contestants are."

    jump top_floor1

    label top_floor1:

        play music "audio/bgm/Calm Loop.ogg" fadeout 1

        menu:

            "Room 6.": 
                call locked from _call_locked
                jump top_floor1 
            "Room 7.":
                call locked from _call_locked_1
                jump top_floor1 
            "Room 8.":
                if metSafirah:
                    call locked from _call_locked_2
                    jump top_floor1
                else:
                    jump Safirah1
            "Room 9.":
                call locked from _call_locked_3
                jump top_floor1 
            "Room 10.":
                call locked from _call_locked_4
                jump top_floor1 
            "back.":
                jump stairs1

    label Safirah1:

        "Let's try this door."

        play sound "audio/sfx/person-knocking-18474.mp3"

        "..."

        play music "audio/bgm/The Puzzle Loop.ogg" fadeout 1

        U "Hello?"
        U "Who's there?"
        U "Another housekeeper?"

        "..."
        "I'll be honest."
        "I was not expecting a response."

        menu:

            "No, not a housekeeper.":
                jump Safirah_choice1_yes
            "Just leave.":
                jump Safirah_choice1_no

        label Safirah_choice1_yes:

                $ metSafirah = True

                mc "No, I'm not a housekeeper."
                mc "I'm a contestant, actually."

                "..."

                play sound "audio/sfx/dorm-door-opening-6038.mp3"

                "{i}*click*{/i}"

                show Safirah_nervous at center, bounce

                USa "Another contestant?"

                mc "Yeah, that's right."
                mc "I'm [mcname]."
                mc "Who are you?"

                Sa "I'm Safirah."

                mc "Nice to meet you."

                menu:
            
                    "Weird situation, isn't it?":
                        jump Safirah_choice2_yes
                    "I've gotta go, sorry.":
                        jump Safirah_choice2_no

        label Safirah_choice2_yes:

            mc "This is all a really weird situation, isn't it?"
            
            "That is such a massive understatement it's unreal."

            hide Safirah_nervous
            show Safirah_surprise at center, bounce

            Sa "..."
            Sa "Well..."

            hide Safirah_surprise
            show Safirah_nervous at center, bounce

            Sa "..."

            hide Safirah_nervous
            show Safirah_cry at center, bounce

            Sa "Aahhh, it's all still so scary!" with hpunch
            Sa "I still don't know where I am!"
            Sa "Or how I got here!"
            Sa "Or who anyone is!"
            Sa "I know I wanted to leave my comfort zone!"
            Sa "But this isn't what I meant!"

            hide Safirah_cry
            show Safirah_nervous at center, bounce

            Sa "I wanna go home..."

            "That was... A lot..."
            "But yeah."
            "Me too."

            Sa "The maids were so nice."
            Sa "And I was kind of warned about it all."
            Sa "Especially with that letter, and that weird dream I had."

            hide Safirah_nervous
            show Safirah_cry at center, bounce

            Sa "But it doesn't make me less scared!"

            menu: 

                "Wait. Dream?":
                    jump Safirah_choice3_Dream
                "Yeah, I can imagine.":
                    jump Safirah_choice3_Agree

            label Safirah_choice3_Dream:

                mc "What dream?"

                hide Safirah_cry
                show Safirah_nervous

                Sa "Oh, well, it's embarrassing to admit..."
                Sa "But I had a dream about leaving my home."

                mc "Like, following a bird?"

                hide Safirah_nervous
                show Safirah_surprise at center, bounce

                Sa "YES! Exactly that!"

                hide Safirah_surprise
                show Safirah_happy at center, bounce

                Sa "It had beautiful golden glowing feathers."

                mc "Yeah, I had that dream too! That's so weird."

                hide Safirah_happy
                show Safirah_neutral at center, bounce

                Sa "Yeah."
                Sa "Maybe it's important somehow."

                menu: 

                    "What kind of bird do you think it is?":
                        jump Safirah_choice4_Bird
                    "No, that's ridiculous.":
                        jump Safirah_choice4_ridiculous

                label Safirah_choice4_Bird:

                    mc "Maybe knowing what kind of bird it is would help."
                    
                    hide Safirah_neutral
                    show Safirah_surprise at center, bounce

                    Sa "Ah, yeah!"

                    hide Safirah_surprise
                    show Safirah_nervous at center, bounce

                    Sa "But I'm not very knowledgeable on birds."

                    mc "Maybe it's mythological?"

                    if foundbird:

                        mc "While researching this whole thing, I found out about a bird."
                        mc "I think it was called an Alicanto?"
                        
                        hide Safirah_nervous
                        show Safirah_surprise at center, bounce

                        Sa "Oh!"
                        Sa "I didn't think to do any research on any of this!"

                        hide Safirah_surprise
                        show Safirah_neutral at center, bounce

                        Sa "And now that I think about it..." 
                        Sa "The guy who owns this place is called Alicanto, isn't he?"

                        mc "Yeah, maybe that was his inspiration."
                        mc "Though the dream is still weird."

                        Sa "Or... Maybe he's an alicanto."

                        mc "Haha, that's funny."

                        hide Safirah_neutral
                        show Safirah_surprise at center, bounce

                        Sa "..."

                        hide Safirah_surprise
                        show Safirah_nervous at center, bounce

                        Sa "Yeah, it sounded silly."

                        "Wait."
                        "Was that SERIOUSLY an actual theory?"

                    else:

                        mc "I wonder..."

                        hide Safirah_nervous
                        show Safirah_happy at center, bounce

                        Sa "Well, we can look into it all later, can't we?"
                        Sa "Surely this place has a library, right?"

                        mc "Hey, maybe."
                        mc "Let's hope it has at least a bookshelf that looks into mythology."

                        "It's entertaining thinking about looking into this."
                        "Because it's so ridiculous."
                        "But she seems pretty serious about it."

                    jump Safirah_leaves

                label Safirah_choice4_ridiculous:

                    mc "Nah, it's probably just a phenomenon of some kind."
                    mc "There's no way a dream would be relevant to being kidnapped."

                    hide Safirah_neutral
                    show Safirah_happy at center, bounce

                    Sa "Actually, dreams are more important than you think."

                    hide Safirah_happy
                    show Safirah_neutral at center, bounce

                    Sa "Like prophetic dreams and Déjà-rêvé."
                    Sa "And the meanings of different objects in dreams."

                    hide Safirah_neutral
                    show Safirah_happy at center, bounce

                    Sa "They're actually very interesting."

                    "Hah, she actually believes in that stuff?"
                    "Come on, it's impossible for dreams to be THAT big of a deal."
                    "..."
                    "Right?"

                    jump Safirah_leaves

            label Safirah_choice3_Agree:

                mc "Yeah, I know how you feel."
                mc "I was so scared and freaked out."

                if investigated:

                    mc "I immediately tried looking for a way to escape."

                else:

                    mc "My brain couldn't even process anything."
                    mc "And I thought I was still dreaming."

                mc "I don't even know how they managed to do all of this."
                mc "I mean, surely we couldn't have just slept through a kidnapping."
                mc "It was honestly like magic."

                hide Safirah_neutral
                hide Safirah_cry
                show Safirah_nervous at center, bounce

                Sa "Yeah."
                
                hide Safirah_nervous
                show Safirah_happy at center, bounce

                Sa "Heh... Maybe it was?"

                mc "Nah, I think they're just good at what they do."

                hide Safirah_happy
                show Safirah_nervous at center, bounce

                Sa "Maybe..."

                jump Safirah_leaves

        label Safirah_choice2_no:

            $ late = False
            
            "I'm gonna be late, I need to go."
            mc "I just wanted to say hi and introduce myself."
            mc "But we should both really get going now."  

            hide Safirah_nervous
            show Safirah_surprise at center, bounce

            Sa "Oh!"
            Sa "You're right!"

            hide Safirah_surprise
            show Safirah_happy at center, bounce

            Sa "Why don't we go together then?"

            jump Safirahleavemenu

            label Safirah_leaves:
                
                hide Safirah_nervous
                hide Safirah_happy
                show Safirah_neutral at center, bounce

                Sa "Anyway, we should go."
                Sa "Or we'll be late."

                mc "Yeah, that's true."
                mc "Who knows what'll happen if we're late."

                hide Safirah_neutral
                show Safirah_nervous at center, bounce

                Sa "... Please don't make me worry."

                hide Safirah_nervous
                show Safirah_happy at center, bounce

                Sa "Anyway, would you like to come with me?"

                jump Safirahleavemenu

            label Safirahleavemenu:

                menu:

                    "No, you go on ahead.":
                        jump Safirah_choice4_stay
                    "Yeah, let's go.":
                        jump Safirah_choice4_go
                
            label Safirah_choice4_stay:

                $ ongroundfloor = False
                $ ontopfloor = True

                show Safirah_neutral at center, bounce
                hide Safirah_happy

                mc "No, you should go on ahead."
                mc "I need to go somewhere first."
                mc "I'll meet you there, though."

                hide Safirah_neutral
                show Safirah_nervous at center, bounce

                Sa "..." 
                Sa "Alright..."
                Sa "Don't be late then."

                mc "I won't, don't worry."

                hide Safirah_nervous with dissolve

                "..."

                "And she's gone."

                jump top_floor1

                

            label Safirah_choice4_go:

                $ LeftwithSafirah = True
                $ ongroundfloor = True
                $ ontopfloor = False

                hide Safirah_happy
                show Safirah_neutral at center, bounce

                mc "Yeah, let's go together."
                mc "Then we won't get lost or distracted."

                hide Safirah_neutral
                show Safirah_happy at center, bounce

                Sa "Yeah, and I won't feel so scared to go in."
                Sa "Let's go then."

                jump Dining_Hall1

        label Safirah_choice1_no:

            "I shouldn't stay."
            "I'll just quietly leave."

            jump top_floor1
label second_floorchoice1:

    $ ontopfloor = False
    $ onsecondfloor = True
    $ onfirstfloor = False
    $ ongroundfloor = False
    $ inbasement = False

    "Let's go to the second floor!"

    scene fadeout
    with Dissolve(.5)
    
    pause .5

    scene Hall
    with Dissolve(.5)

    "Oh, it pretty much looks the same as the first floor."
    "But there are 5 doors with numbers."
    "This must be where the other contestants are."

    jump second_floor1

    label second_floor1:

        play music "audio/bgm/Calm Loop.ogg" fadeout 1

        menu:

            "Room 1":
                call locked from _call_locked_5 # goes to locked label to say the door's locked
                jump second_floor1 # goes back to the menu when you return so you don't go to room 2
            "Room 2":
                call locked from _call_locked_6
                jump second_floor1
            "Room 3":
                call locked from _call_locked_7
                jump second_floor1
            "Room 4":
                call locked from _call_locked_8
                jump second_floor1
            "Room 5":
                if metZach or annoyedZach:
                    call locked from _call_locked_9
                    jump second_floor1
                else:
                    jump Zach1
            "Back.":
                jump stairs1

        label Zach1:

            "Let's try this door."

            play sound "audio/sfx/person-knocking-18474.mp3"
            "..."

            play sound "audio/sfx/dorm-door-opening-6038.mp3"

            "{i}*click.*{/i}"

            play music "audio/bgm/Of Far Different Nature - 0 to 100 (CC-BY).ogg" fadeout 1

            show Zach_glare at center, bounce

            UZ "What?"

            "Oh, he does not look happy."

            menu:

                "Hi, who are you?":
                    jump Zachchoice1_Hi
                "... Nobody...":
                    jump Zachchoice1_Bye

            label Zachchoice1_Hi:

                $ metZach = True

                mc "Hi, I'm [mcname]."
                mc "Who are you?"

                UZ "..."

                Z "Zach."

                hide Zach_glare
                show Zach_angry at center, bounce
                
                Z "You done now?"

                mc "Hey! Cool name!"

                "I sound like an idiot right now."
                "But whatever gets on this guys good side."


            label Zachchoice2_Situation:

                mc "So!"
                mc "It's all pretty weird, isn't it?"
                mc "This situation, I mean."

                hide Zach_angry
                show Zach_surprise at center, bounce

                Z "Weird? That's all you have to say?"

                hide Zach_surprise
                show Zach_angry at center, bounce

                Z "It's not weird, it's annoying-"

                hide Zach_angry
                show Zach_surprise at center, bounce

                Z "-Frustrating, even!"
                Z "I mean, we all have a LIFE we need to get back to."

                hide Zach_surprise
                show Zach_angry at center, bounce

                Z "Or- I do."

                hide Zach_angry
                show Zach_glare at center, bounce

                Z "And everyone's calmness about all this is making me think I'm the only one."

                menu:

                    "Yeah, you're right.":
                        jump Zachchoice3_Foolish
                    "You should look on the bright side.":
                        jump Zachchoice3_BrightSide

                label Zachchoice3_Foolish:

                    $ late = True

                    "He's kinda right, actually."
                    "Or, I think he is..."
                    "I haven't exactly had a chance to meet the others."
                    "But we have literally been kidnapped from our homes."
                    "To this unknown location."
                    "To be in a show."
                    "For all we know, this could be exactly like that game with the black and white teddy bear."

                    mc "Maybe they ARE pretty foolish."

                    hide Zach_glare
                    show Zach_laugh at center, bounce
                        
                    Z "Haha, yeah, glad to know you're someone with sense."
                    Z "It's surprisingly hard to find here."

                    hide Zach_laugh
                    show Zach_glare at center, bounce

                    Z "Despite out current situation anyway."
                    Z "Even the doctor guys are calm, one of them treating it like a vacation."
                        
                    "Oh, there are doctors, here too?"

                    mc "It's probably because of the housekeepers being so nice."
                    mc "But still."

                    hide Zach_glare
                    show Zach_laugh at center, bounce

                    Z "Hah, nice?"

                    hide Zach_laugh
                    show Zach_nervous at center, bounce

                    Z "Mine wasn't."

                    hide Zach_nervous
                    show Zach_neutral at center, bounce

                    Z "Well, she kinda was, but only because it was her job."

                    hide Zach_neutral
                    show Zach_angry at center, bounce

                    Z "I could sense her dislike."

                    mc "Geez, what did you do to her?"

                    hide Zach_angry
                    show Zach_nervous at center, bounce

                    Z "..."
                    Z "I may have cursed her out."

                    hide Zach_nervous
                    show Zach_angry at center, bounce

                    Z "But she fucking deserved it."
                    Z "Kidnapping us all like that."

                    "He seems to have opened up a lot more now."

                    mc "I don't know about her deserving it, but I can understand it."
                    mc "Especially with the situation."
                    mc "But you should definitely apologise to her."

                    hide Zach_angry
                    show Zach_nervous at center, bounce

                    Z "..."
                    Z "Yeah, I guess you're right..."

                    hide Zach_nervous
                    show Zach_neutral at center, bounce

                    Z "So how'd you treat the maid that visited you?"

                    if attackedmaid:

                        mc "Well..."

                        Z "Haha, I'm guessing it didn't go well." 
                            
                        mc "I threw a lamp at her."

                        Z "..."

                        hide Zach_neutral
                        show Zach_surprise at center, bounce

                        Z "HUH?!"
                        Z "You WHAT?!"

                        mc "She scared me!"
                        mc "I thought I was gonna die!"
                        mc "Then she just... caught it, put it back and smiled at me!"
                        mc "I was ready for her to kill me with it."

                        Z "..."
                        Z "..."
                        Z "..."

                        hide Zach_surprise
                        show Zach_laugh at center, bounce

                        Z "Hehehehehe!"
                        Z "Oh man! That is so funny!"

                        mc "Hey don't laugh!"

                        "Man, I shouldn't have admitted that to him, so embarrassing..."
                        "I feel even worse than I did before."

                        Z "Hey, don't tell me a story like that if you don't want me to laugh!"

                        mc "Is it funny because I attacked a maid?"

                        hide Zach_laugh
                        show Zach_neutral at center, bounce

                        Z "No, because you don't seem like the kind to do that."
                        Z "And because it didn't work and you were more scared and intimidated than she was."
                        Z "You're lucky it failed."

                        hide Zach_neutral
                        show Zach_glare at center, bounce

                        Z "Otherwise I would have punched you."
                        Z "I almost punched that other guy before."    

                    else:

                        mc "Honestly, it went fine."
                        mc "I was very confused though."

                        hide Zach_neutral
                        show Zach_nervous at center, bounce

                        Z "Ah, so you didn't do anything I did."
                        Z "Now I feel even worse about what I did, haha."
                        Z "Though, at least I didn't do what that other guy did."

                    mc "Other guy?"

                    hide Zach_nervous
                    hide Zach_glare
                    show Zach_surprise at center, bounce

                    $ heardaboutRed = True

                    Z "Oh, right, you woke up later than most of us."

                    hide Zach_surprise
                    show Zach_neutral at center, bounce

                    Z "There was this guy I spoke to when everyone was starting to leave their rooms."

                    "What."
                    "They had more prep time than me?!"

                    Z "I can't remember the name of him, but he had red hair and a tattoo on his neck."
                    Z "He was knocking on everyone's doors to talk to them."

                    hide Zach_neutral
                    show Zach_angry at center, bounce

                    Z "He's a strange guy."

                    hide Zach_angry
                    show Zach_glare at center, bounce

                    Z "But he decided to talk to me."
                    Z "Which would have been fine..."

                    hide Zach_glare
                    show Zach_angry at center, bounce

                    Z "If he didn't laugh about how he almost attacked one of the maids."
                            
                    mc "Jeez, how'd you not punch him?"

                    Z "I seriously would have, but..."

                    hide Zach_angry
                    show Zach_nervous at center, bounce

                    Z "Something about him creeps me the hell out."
                    Z "And what he's done has made him even worse than he already is."
                    Z "And the way he laughed about things is..."
                    Z "Creepy..."

                    menu:

                        "He sounds terrifying.":
                            jump Zachchoice4_Terrifying
                        "Sounds like fun.":
                            jump Zachchoice4_Fun

                    label Zachchoice4_Terrifying:

                        "What the hell is up with the guy he's talking about?"
                        "Have they seriously invited a potential CRIMINAL to this show?"
                        "Even from a not-so-ethical standpoint, surely they see the harm in that, right?"

                        mc "I wouldn't wanna meet him at all."

                        hide Zach_nervous
                        show Zach_glare at center, bounce

                        Z "Yeah, it's a shame you might have to."
                        Z "But, if you do, don't get me anywhere involved with him."
                        Z "That includes being buddy-buddy with him or drama."

                        "Huh, such a small amount of time and there's already drama and grudges."
                        "This is gonna be great..."
                            
                        mc "I won't, don't worry."

                        hide Zach_glare
                        show Zach_neutral at center, bounce

                        Z "Thanks."

                        jump Zachleaves1
                        
                    label Zachchoice4_Fun:

                        $ annoyedZach = True

                        mc "You say he sounds scary, I think he sounds fun."

                        hide Zach_nervous
                        show Zach_surprise at center, bounce

                        Z "Really? He sounds FUN to you?"
                        Z "Are you joking?"
                        Z "..."

                        hide Zach_surprise
                        show Zach_glare at center, bounce

                        Z "Don't answer that..."

                        hide Zach_glare
                        show Zach_angry at center, bounce

                        Z "You're clearly not as smart as I thought you were."

                        mc "Hey, what's THAT supposed to mean?"
                        mc "You-"

                        play sound "audio/sfx/door-slam-sound-effect-21878.mp3"

                        hide Zach_angry

                        "{i}*SLAM!*{/i}"

                        "He slammed the door in my face."
                        "Literally over nothing."

                        jump second_floor1

                    label Zachchoice3_BrightSide:

                        mc "Hey, maybe you should look on the bright side of things."
                        mc "We're not in any danger, that should be a reason to relax, right?"
                        hide Zach_glare
                        show Zach_angry at center, bounce

                        Z "Oh, you're one of THOSE guys."

                        mc "One of those guys? What's THAT supposed to mean?"
                        mc "I'm just saying that you should be more positive."
                        mc "Instead of being so mean and rude to people."

                        hide Zach_angry
                        show Zach_glare at center, bounce

                        Z "But there's a massive difference between being positive and being dumb and naive."

                        hide Zach_angry
                        show Zach_glare at center, bounce

                        Z "It's all fine being positive, but when you're somewhere you DO NOT KNOW..."
                        Z "In a place and situation you NEVER wanted to be in..."
                        Z "Unsure of what's going to happen?"

                        hide Zach_glare
                        show Zach_angry at center, bounce

                        Z "Foolish positivity is the LAST thing I want."
                        Z "And it's the last thing anyone here should resort to."

                        mc "Foolish?!" 
                        mc "What are you talking about, foolish?!"
                        mc "It's not foolish to think you shouldn't be rude to people in the same situation as you!"

                        hide Zach_angry
                        show Zach_glare at center, bounce

                        Z "But we're NOT in the same situation, are we?"
                        Z "Because I seem to be one of the few people here who want to get back to the real world."

                        mc "We all want to go back!"
                        mc "We're just as lost and confused as you!"
                        mc "But there's no need to be so rude!"

                        jump Zachchoice1_Bye

            label Zachchoice1_Bye:

                $ annoyedZach = True

                if metZach:

                    Z "Whatever, I'm done talking."
                
                else:
                    
                    mc "... Nobody..."
                    mc "Goodbye."

                    UZ "Hmph..."

                play sound "audio/sfx/door-slam-sound-effect-21878.mp3"

                hide Zach_glare
                
                "{i}*SLAM!*{/i}"

                "He slammed the door..."
                "Rude."

                jump second_floor1 
            
            label Zachleaves1:

                hide Zach_angry
                hide Zach_glare
                hide Zach_laugh
                hide Zach_nervous
                hide Zach_surprise
                show Zach_neutral at center, bounce

                Z "Anyway, we gotta go."
                Z "We're cutting it close to time."
                
                mc "Oh, yeah, we should."

                Z "We should get going now then."

                menu:

                    "Yeah, let's go.":
                        jump Zachchoice5_Go
                    "No, I'll stay here.":
                        jump Zachchoice5_Stay

                label Zachchoice5_Stay:

                    mc "Nah, I'll stay, I still got things to do."

                    hide Zach_neutral
                    show Zach_laugh at center, bounce
                    
                    Z "Ah well, don't say I didn't ask, haha."
                    Z "I'm heading down then. Peace."

                    hide Zach_laugh with dissolve

                    "And now he's gone."
                    "Should I go down then now?"
                    "Or keep looking around?"

                    jump second_floor1

                label Zachchoice5_Go:


                    if metSafirah:

                        $ late = True
                    
                    else:
                        $ late = False
                    $ ongroundfloor = True
                    $ onsecondfloor = False

                    mc "I'd rather not show up alone."

                    hide Zach_neutral
                    show Zach_nervous at center, bounce

                    Z "Same here."

                    hide Zach_nervous
                    show Zach_neutral at center, bounce

                    Z "Let's go then."

                    hide Zach_neutral

                    jump Dining_Hall1



label first_floorchoice1:

    play music "audio/bgm/Calm Loop.ogg" fadeout 1

    $ ontopfloor = False
    $ onsecondfloor = False
    $ onfirstfloor = True
    $ ongroundfloor = False
    $ inbasement = False

    "Let's go to the first floor!"

    scene fadeout
    with Dissolve(.5)
    
    pause .5

    scene Hall
    with Dissolve(.5)

    "This is the first floor."
    "There are 2 doors."
    "One is mine."
    "So the other must be Alicanto's..."
    "Unless it's not and I'm being dumb."

    label first_floor1:

        menu:
            "My room":
                jump mcroom_inaccessible
            "Alicanto's room":
                call locked from _call_locked_10
                jump first_floor1
            "back.":
                jump stairs1
        
        label mcroom_inaccessible:

            "I already left my room."
            "It'd be weird if I went in again."

            jump first_floor1 

    

label ground_floorchoice1:

    

    $ ontopfloor = False
    $ onsecondfloor = False
    $ onfirstfloor = False
    $ ongroundfloor = True
    $ inbasement = False
    
    play music 'audio/bgm/Calm Loop.ogg' fadeout 1

    "Let's go to the ground floor!"

    scene fadeout
    with Dissolve(.5)
    
    pause .5

    scene GHall
    with Dissolve(.5)

    "This is the ground floor."
    "It has 3 corridors."
    "This place just gets bigger and bigger..."

    jump Ground_floor1

    label Ground_floor1:

        menu:

            "Go left":
                jump Dining_Hall1
            "Go right":
                if kickedoutkitchen:
                    jump kickedoutkitchen
                else:
                    jump Kitchen1
            "Go forward":
                jump GFForward1
            "back.":
                jump stairs1

        label Kitchen1:


            scene fadeout
            with Dissolve(.5)
    
            pause .5

            scene Kitchen
            with Dissolve(.5)

            "This must be the kitchen."
            "It's so busy..."
            "I feel like I should leave."

            chef "OI!!!" with hpunch
            chef "What the FUCK are ya doing in my kitchen?!?!"
            chef "GET OUT!!!" with hpunch

            "Oop, yeah I should go."
            "And fast!"

            menu:

                "Let's leave.":
                 jump Kitchen_left1
                "No, how dare he!":
                    jump kickedoutkitchen1

            label Kitchen_left1:

                "Oh, yeah, I should leave."

                mc "I'm sorry, I got lost!"
                mc "I'll get out of your hair!"

                chef "Did the fucking maid not give you the right directions or are you just stupid?!"
                chef "LEFT!"
                chef "TURN LEFT GOD DAMN IT!"
                chef "LLEEEEFFTT!"

                "Alright, alright, I get it!"
                "Turn left!"

                scene fadeout
                with Dissolve(.5)
    
                pause .5

                scene GHall
                with Dissolve(.5)

                jump Ground_floor1

            label kickedoutkitchen1:

                $ late = True
                $ kickedoutkitchen = True

                "NO!"
                "How dare he!"
                "He has NO right to be rude to me!"

                mc "HEY!"
                mc "Don't you yell at me!"
                mc "You have NO right to be so rude to me!"

                chef "Oi, you..."

                "SHIT he's PISSED!"


                scene GHall with hpunch

                chef "YOU ARROGANT LITTLE SHIT!"
                chef "IF I FUCKING TELL YOU TO LEAVE MY FUCKING KITCHEN, YOU FUCKING LEAVE!"
                chef "YOU BEING A GUEST DOESN'T MAKE YOU FUCKING SPECIAL!"

                play sound "audio/sfx/door-slam-sound-effect-21878.mp3"

                "{i}*SLAM!*{/i}"

                "..."
                "... What just happened?"
                "..."
                "I can hear so much more swearing in there."

                jump Ground_floor1

        label GFForward1:

            "Let's go forwards."
            "That's the right way, right?"
            "Ah well, even if it isn't, we're exploring."

            show tabby maid at center, bounce

            hk2 "Oh, I'm sorry, but this isn't the right way to the dining hall."
            hk2 "Allow me to take you there."

            mc "Uh..."
            mc "Ok."

            "Damn, exploring time's over, I guess."

            hide tabby maid

            jump Dining_Hall1

label basement1:

    $ ontopfloor = False
    $ onsecondfloor = False
    $ onfirstfloor = False
    $ ongroundfloor = False
    $ inbasement = True

    "Let's go to the basement!"

    "Oh..."
    "Nevermind..."
    "There's a locked door blocking the way."
    "I'll just stop at the ground floor then."

    jump ground_floorchoice1

label lockedT1:

    "The door's locked."
    "Don't tell me I'm gonna have to wait for them to come back."
    "I hate waiting."

    jump top_floor1

label lockedS1:

    "The door's locked."
    "Don't tell me I'm gonna have to wait for them to come back."
    "I hate waiting."

    jump second_floor1

label locked:
    
    "The door's locked."
    "Don't tell me I'm gonna have to wait for them to come back."
    "I hate waiting."

    return # returns to previous call choice label

label lockedF1:

    "The door's locked."
    "Don't tell me I'm gonna have to wait for them to come back."
    "I hate waiting."

    jump first_floor1
    
label kickedoutkitchen:

    "I probably shouldn't."
    "I'm not welcome there."
    "Especially not after what happened."

    jump Ground_floor1

label onfloor1:

    "I'm already on this floor."

    jump stairs1

label onfloor:

    "I'm already on this floor."

    return

jump ch05
