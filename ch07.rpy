#characters
define mc = Character("[mcname]")
define viridianrose = Character("@viridianrose", color = "#8ce99a")
define percypiper = Character("@percypiper", color = "#d899be")
define BH = Character("Bonnyhoddie", color = "#ffc6e5")

# The game starts here.

label ch07:

    hide Alicanto_happy

    scene fadeout
    with Dissolve(1.5)

    pause 0.5

    scene Aloffice
    with Dissolve(1.5)

    "So this is Alicanto's office."

    show Alicanto_happy at center, bounce

    Al "Welcome to my humble office!"

    hide Alicanto_happy
    show Alicanto_neutral at center, bounce

    Al "What do you think?"

    mc "I was expecting more gold and pizzazz, honestly."
    mc "Either that or for it to be a mess."

    hide Alicanto_neutral
    show Alicanto_happy at center, bounce

    Al "Haha!"
    Al "Well, I like to surprise!"

    "Clearly."

    mc "Uhm..."
    mc "So, why am I here?"
    mc "Am I in trouble?"

    if attackedmaid:

        mc "Is this about the maid?"

    hide Alicanto_happy
    show Alicanto_nervous at center, bounce

    Al "Oh, no, not at all!"

    if attackedmaid:

        Al "I would be mad at you for attacking one of my staff."

        hide Alicanto_nervous
        show Alicanto_neutral at center, bounce

        Al "But in the end, nobody was hurt."
        Al "And you seem to be mad at yourself enough."

        hide Alicanto_neutral
        show Alicanto_happy at center, bounce

        Al "You don't need me making it worse."

        hide Alicanto_happy
        show Alicanto_annoyed at center, bounce

        Al "Though, please don't do it again."

        "Understood."
        "He's kinda scary when he's holding his cane up."

        hide Alicanto_annoyed
        show Alicanto_happy at center, bounce

        Al "Actually, it's for a different reason."
    
    else:

        hide Alicanto_nervous
        show Alicanto_happy at center, bounce
        
        Al "The opposite, actually!"

    hide Alicanto_happy
    show Alicanto_neutral at center, bounce

    Al "It's about your role in the game."

    mc "Role?"
    mc "I thought I was just a contestant."

    hide Alicanto_neutral
    show Alicanto_nervous at center, bounce

    Al "No, you're not."

    hide Alicanto_nervous
    show Alicanto_neutral at center, bounce

    Al "More like an employee."
    
    mc "Employee?"
    mc "So, what?"
    mc "I serve them?"

    hide Alicanto_neutral
    show Alicanto_happy at center, bounce

    Al "Oh, no no no!"
    Al "Haha, of course you're not serving them!"

    hide Alicanto_happy
    show Alicanto_neutral at center, bounce

    Al "So, you know how the game will work, correct?"

    menu:

        "Yes.":
            jump Alicanto_choice1_yes
        "No, remind me.":
            jump Alicanto_choice1_no

    label Alicanto_choice1_yes:

        mc "Yeah, I understand."

        hide Alicanto_neutral
        show Alicanto_happy at center, bounce

        Al "Good!"
        Al "Then I won't need to explain again!"
        Al "And I can go straight to your role!"

        jump Alicanto_choice1_done
        

    label Alicanto_choice1_no:

        mc "Not really."

        hide Alicanto_neutral
        show Alicanto_nervous at center, bounce

        Al "Oh, but I thought I explained things really well."

        mc "Yeah, but I'm not the best at focusing, I'll be honest."
        mc "And sometimes, when people speak, it just sounds like gibberish."

        Al "I see."

        hide Alicanto_nervous
        show Alicanto_happy at center, bounce

        Al "No matter, I'll simply explain everything again."
        Al "So, over the course of a few weeks-"

        mc "How many weeks again?"

        hide Alicanto_happy
        show Alicanto_neutral at center, bounce

        Al "Just 5."
        Al "Each round lasts for a week."

        mc "Oh, ok."
        
        "That's gonna go by so slowly."

        Al "The 10 contestants will compete in mini games occasionally that reveal parts of their personality."

        hide Alicanto_neutral
        show Alicanto_happy at center, bounce

        Al "This revealed personality is important, as it helps the audience develop an opinion of them!"
        Al "And these opinions reflect in popularity polls."
        Al "Which, hopefully, will further reveal hidden aspects of a person."

        mc "Oh, I see."
        mc "So, what exactly is the point of these polls?"
        mc "And what role am I meant to play?"

        hide Alicanto_happy
        show Alicanto_neutral at center, bounce

        Al "Simply put, it's so I don't give it all to the wrong person."
        Al "I don't really have much interest in public opinion itself, it's a flawed system."

        hide Alicanto_neutral
        show Alicanto_mischievous at center, bounce

        Al "However, it matters to a lot of humans."
        Al "So, I care about their reactions."
        Al "Like if a person was to use their positive votings as reasons to be arrogant."
        Al "Or if they turned aggressive or insecure after learning they're disliked by the public."
        
        mc "So you want to reveal their true natures to decide who to give your wealth to?"

        hide Alicanto_mischievous
        show Alicanto_happy at center, bounce

        Al "Precisely!"

        "That is..."
        "Actually terrifying..."

        Al "And this is where we talk about the part that you're going to play!"

        jump Alicanto_choice1_done


    label Alicanto_choice1_done:

        "I hope I have a good role."
        "Or I'm out."
        "I'm not gonna be some drama starter or problematic character."

        hide Alicanto_happy
        show Alicanto_neutral at center, bounce

        Al "So, as you may have noticed, there are 11 players, not 10."
        Al "This was deliberate."
        Al "You're here to interact with the contestants."

        mc "Really?"
        mc "That's it?"

        hide Alicanto_neutral
        show Alicanto_nervous at center, bounce

        Al "Ha, it sounds too simple, doesn't it?"
        Al "Let me elaborate on that."

        hide Alicanto_nervous
        show Alicanto_neutral at center, bounce

        Al "So, obviously, every single one of the contestants are going to be talking to each other."
        Al "And all interactions between contestants are important."

        hide Alicanto_neutral
        show Alicanto_happy at center, bounce

        Al "But who you talk to is the most important!"

        hide Alicanto_happy
        show Alicanto_neutral

        Al "Many of your interactions with other contestants will be aired."
        Al "So you can help boost their spotlight and either help or hinder them by revealing things about them."

        mc "Oh, so I'm like a spy?"

        hide Alicanto_neutral
        show Alicanto_happy at center, bounce

        Al "Pretty much, yes!"

        hide Alicanto_happy
        show Alicanto_neutral at center, bounce

        Al "So you're not exactly competing in the games the same way the others are."
        Al "But for the sake of not exposing your identity, you'll still be treated like one."
        Al "However, to make up for this, I'm more than happy to give you payment as thank you."

        hide Alicanto_neutral
        show Alicanto_happy at center, bounce

        Al "Monetary payment, of course!"

        mc "Really?"
        mc "Wow."
        mc "So I technically win no matter what, right?"

        Al "You could say that!"

        hide Alicanto_happy
        show Alicanto_neutral at center, bounce

        Al "So, would you like to be a part of it?"

        "It'd definitely be good to be a part of it."
        "I mean, monetary payment?"
        "This guy's already paying the winner 5 million."
        "Just imagine how much I'll get."
        
        mc "Ok!"
        mc "I'm in!"
        
        hide Alicanto_neutral
        show Alicanto_happy at center, bounce
        
        Al "Splendid!"
        Al "Then, you should get going!"

        hide Alicanto_happy
        show Alicanto_annoyed at center, bounce

        Al "I need to speak to a certain somebody now anyway."

        if metRed:

            "He means Red."
            "He SO means Red."
        
        else:

            "Huh, I wonder who that could be."

        mc "Yeah, I'll leave quickly then."

        hide Alicanto_annoyed
        show Alicanto_neutral at center, bounce
        
        Al "It was a pleasant talk with you, mx. [mcname]."

        hide Alicanto_neutral with dissolve

    label demo_end:

        scene fadeout
        with Dissolve(1.5)

        play music "audio/bgm/1_Menu_Master.mp3" fadeout 1

        BH "Aannd..."
        BH "Scene!"
        BH "This is the end of the demo!"
        BH "I hope you enjoyed it!"
        BH "I can't wait to be able to work on this after College!"
        BH "As I stated at the start, there are popularity polls for the game."
        BH "Actually, by the time this game is out, you should probably be able to access them."
        BH "Again, the link is {a=https://gold-rush-official.tumblr.com/}here{/a}."
        BH "I'd really love it if you voted and followed the page and development."
        BH "And I'd really appreciate any feedback that could help spice the game up."
        BH "Thank you for playing!"
        BH "Now!"
        BH "Back to the menu you go!"
        BH "Go on!" 
        BH "Get!"

        stop music

    return
