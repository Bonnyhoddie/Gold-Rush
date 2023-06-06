#characters
define mc = Character("[mcname]")

#bg images
image mc room = "Images/backgrounds/old mc room.jpg"
image Letter = "Images/Letter.png"
image fadeout ="Images/Fade-out.png"

default foundbird = False

#player name input code begins

label ch02:
 
    scene fadeout

    scene old_mc_room
    with Dissolve(.5)

    pause .5

    play music "audio/bgm/Friday Afternoon Loop.ogg" fadeout 1

    "It's been a few days since I got that letter."

    if openedletter:
        
        "This should be when that Alicanto guy comes for me."
        "Or maybe that's tomorrow..."
        "Whichever day it's meant to be."
        "I am so stupid for believing this for even a moment."
        "..."
        "On the plus side though, at least I can laugh when I wake up tomorrow."
        "..."
        "..."
        "..."
        "Something feels wrong."
        "In a weird way."
        "No matter how ridiculous it all seems."
        "I keep worrying that the letter..."
        "And this game show..."
        "It's all true."
        "..."
        "I was hoping on going on a trip soon anyway."
        "Wouldn't hurt to actually pack, right?"
        "Even if it doesn't happen."
        
        menu:

            "Yes, let's pack.":
                jump choice4_yes
            "no, it's a waste of time.":
                jump choice4_no

        label choice4_yes:
            
            $ menu_flag = True

            "Yeah, it wouldn't hurt to just pack a few clothes at least."
            
            $ packed = True 

            jump choice4_done

        label choice4_no:
            
            $ menu_flag = False

            "No, this is just a prank."
            "I'm worrying too much."
            "Besides, I should think about packing once I actually BOOK the trip."
            
            $ packed = False 

            jump choice4_done


    else:

        "Something doesn't feel right..."
        "I feel like I should open that letter."

        menu:

            "Open the letter.":
                jump choice5_yes
            "No.":
                jump choice5_no

        label choice5_yes:

            $ menu_flag = True

            mc "Ugh... Fine..."
            mc "I'll open the damn letter..."

            "I slowly open the envelope, with some hesitance."
        
            show Letter

            "Dear [mcname],"

            "I, Alicanto, formally invite you to the very first season of our TV show!" 
            "You were one of the 13 lucky enough to be selected by us!"
            "So pack your things, and we will collect you in a few days to explain everything!"
            "Yours sincerely,
            Alicanto"
            "..."

            hide Letter

            mc "What the fuck?"

            "Well that explained absolutely nothing."
            "I think it's safe to say..."
            "That I have been officially pranked."
            "And by a dumb letter too."
            "And I worried over nothing."
            "Although..."
            "Maybe it's not a prank?"
            "I'll be getting my hopes up."
            "BUT..."
            "There's no harm in investigating, right?"

            $ openedletter = True

            menu:

                "Detective time!":
                    jump choice6_yes
                "No thanks.":
                    jump choice6_no

            label choice6_yes:

                $ menu_flag = True

                mc "Alright, Alicanto, let's play investigator."

                "Let's start with the internet."

                scene fadeout
                with Dissolve(.5)

                pause .5

                scene mc room
                with Dissolve(.5)

                pause .5

                "It felt like hours passed..."
                "And nothing..."
                
                mc "Huhhh, this was a waste of time."
                mc "Should have expected that..."
                "All I got were some drawings of a glowing bird."
                "..."
                "It was a cool bird though."

                $ foundbird = True

                jump choice5_done

            label choice6_no:

                $ menu_flag = True

                "No, this is a waste of time and I know it."
                "Forget the letter."
                "I'm just gonna throw it away."

                scene fadeout
                with Dissolve(.5)

                pause .5

                scene old_mc_room
                with Dissolve(.5)

                pause .5

                "Huh."
                "Weird..."
                "I got rid of that letter."
                "And now I feel like I made the greatest mistake of my life..."
                "Freaky..."

                jump choice5_done

        label choice5_no:

            $ menu_flag = False

            mc "No way..."
            mc "Nuh uh" 
            mc "Not even with a 10ft pole and a hazmat suit."
            
            "I'm just gonna throw it away."

            scene fadeout
            with Dissolve(.5)

            pause .5

            scene old_mc_room
            with Dissolve(.5)

            pause .5

            "Huh."
            "Weird..."
            "I got rid of that letter."
            "And now I feel like I made the greatest mistake of my life..."
            "Freaky..."

            $ openedletter = False
            
            jump choice5_done

        label choice5_done:
    
    label choice4_done:
        # ... the game continues here.
    
    scene fadeout
    with Dissolve(1.5)

    pause 1

    scene old_mc_room
    with Dissolve(1.5)

    pause 1
    
    "Ugh... I feel so tired today..." 
    "No, I need to go to work later..."
    "..."
    "Maybe a small nap wouldn't hurt."

    scene fadeout
    with Dissolve(1.5)

    pause 1



jump ch03
