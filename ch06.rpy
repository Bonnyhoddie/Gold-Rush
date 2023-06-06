#characters
define mc = Character("[mcname]")
define viridianrose = Character("@viridianrose", color = "#8ce99a")
define percypiper = Character("@percypiper", color = "#d899be")
define BH = Character("Bonnyhoddie", color = "#ffc6e5")

# The game starts here.

label ch06:

    if late:
  
        Al "So, now that you are all here."

    else:

        hide Alicanto_neutral
        show Alicanto_Bow at center, bounce

        Al "Apologies for leaving you all to wait."

    hide Alicanto_Bow
    hide Alicanto_happy
    show Alicanto_neutral at center, bounce
        
    Al "As you are all aware, I am Sir Alicanto."
    Al "However, you can simply call me Alicanto."

    hide Alicanto_neutral
    show Alicanto_happy at center, bounce

    Al "And it is such a joy to see you all!"
    Al "And I can tell some of you have dressed your best!"

    if PJs:

        hide Alicanto_happy
        show Alicanto_nervous at center, bounce

        Al "And some..."
        Al "... Not so much..."

        hide Alicanto_nervous
        show Alicanto_happy at center, bounce

        Al "But no matter!"

        "He's talking about me."
        "Maybe I should have made an effort."

    elif fancy:

        Al "And some more than others!"
        Al "Now that is what I like to see!"

        "Heh, he's talking about me."
        "Although, maybe a suit was a bit too much."
        "Especially compared to what everyone else is wearing."

    hide Alicanto_happy
    show Alicanto_neutral at center, bounce

    Al "And you, my honoured guests..."
    Al "Are competing in the first ever season of Gold Rush!"

    "What a dumb name."

    Al "And you must all be wondering..."
    Al "'Why are we here?'"
    Al "'What is the point of the game?'"
    Al "'How do we decide the winner?'"

    show Sebastian_neutral at Ssleft, bounce
    show Alicanto_neutral at sright  with MoveTransition(0.2)

    if metSebastian:

        S "I'm actually wondering how we got here."

    else:

        US "I'm actually wondering how we got here."

    hide Alicanto_neutral
    show Alicanto_nervous at sright, bounce
    
    Al "Yes, that too..."

    hide Sebastian_neutral
    hide Alicanto_nervous
    show Alicanto_happy at sright
    show Alicanto_happy at center, bounce  with MoveTransition(0.2)

    Al "But worry not!"
    Al "For I have the answers to your questions!"

    show Aoi_neutral at sright, bounce
    show Alicanto_happy at sleft  with MoveTransition(0.2)

    A "You better have!"

    hide Aoi_neutral
    show Aoi_angry at sright, bounce

    A "Or I swear, I'm gonna hit you!"

    hide Alicanto_happy
    show Alicanto_nervous at sleft, bounce
    
    Al "..."
    Al "Let's... Not do that, Miss. Miyagawa..."

    hide Aoi_angry
    hide Alicanto_nervous
    show Alicanto_neutral at sleft, bounce
    show Alicanto_neutral at center  with MoveTransition(0.2)

    Al "So, to answer your questions, and put your minds at ease."
    Al "Again, you are competing in the first ever season of Gold Rush."
    Al "You were all randomly selected from the entire global population."
    Al "The only link between you all is that you speak the same language."
    Al "This was to avoid language barriers."

    "So we were all just incredibly unlucky?"
    "Or... Lucky for some..."

    Al "The game will last for 5 weeks."
    Al "And you will compete in a series of minigames as you stay here."
    Al "All for the purpose of boosting your self-image to the public."
    Al "Who will vote in 5 rounds to decide the winner."

    show Percy_neutral at sleft, bounce
    show Alicanto_neutral at sright  with MoveTransition(0.2)

    if metPercy:

        P "So, what happens to those who lose the votes?"
        P "Are they eliminated from the show?"

    else:

        UP "So, what happens to those who lose the votes?"
        UP "Are they eliminated from the show?"

    hide Alicanto_neutral
    show Alicanto_happy at sright, bounce

    Al "Excellent question, Miss. Percy!"
    
    $ metPercy = True

    hide Alicanto_happy
    show Alicanto_neutral at sright, bounce

    Al "And no, those who lose in the votes are not eliminated from the show."
    Al "Instead, the votes all added up at the end to decide the winner."
    Al "As the key purpose in this game show is to see how behaviours change."

    hide Percy_neutral
    show Alicanto_neutral at sleft  with MoveTransition(0.2)
    show Flora_surprise at sright, bounce
    
    if metFlora:

        F "Then... Isn't it counter-intuitive to tell us that?"

        hide Flora_surprise
        show Flora_sad at sright, bounce

        F "I mean, it's like telling a patient that what you're giving them is a placebo."
        F "It doesn't work if you know."

    else:

        UF "Then... Isn't it counter-intuitive to tell us that?"

        hide Flora_surprise
        show Flora_sad at sright, bounce

        UF "I mean, it's like telling a patient that what you're giving them is a placebo."
        UF "It doesn't work if you know."

    hide Alicanto_neutral
    show Alicanto_happy at sleft, bounce

    Al "Another excellent question, Miss. Flora!"

    $ metFlora = True

    hide Alicanto_happy
    show Alicanto_neutral at sleft, bounce

    Al "However, I wouldn't worry about that at all."

    hide Alicanto_neutral
    show Alicanto_happy at sleft, bounce

    Al "Just focus on having fun!"

    hide Alicanto_happy
    show Alicanto_neutral at sleft, bounce

    Al "We can worry about the voting rounds and results later."

    hide Flora_sad
    hide Alicanto_neutral
    show Alicanto_happy at sleft, bounce
    show Alicanto_happy at center  with MoveTransition(0.2)

    Al "This is so great, any more questions?"

    
    show Alicanto_happy at sright  with MoveTransition(0.2)
    show Safirah_surprise at sleft, bounce

    if metSafirah:

        Sa "So, if we can't leave by elimination..."
        Sa "How DO we leave early if we want to do so?"

    else:

        Sa "So, if we can't leave by elimination..."
        Sa "How DO we leave early if we want to do so?"

    hide Alicanto_neutral
    show Alicanto_happy at sright, bounce

    Al "Ah, another good question."
    Al "And one of the more important ones too!"

    hide Alicanto_happy
    show Alicanto_neutral at sright, bounce

    Al "So, as Miss. Safirah pointed out-"

    $ metSafirah = True

    hide Safirah_surprise
    show Safirah_happy at sleft, bounce

    Sa "Oh, just call me Safirah."

    hide Alicanto_neutral
    show Alicanto_Bow at sright, bounce

    Al "Very well!"

    hide Alicanto_Bow
    hide Safirah_happy
    show Alicanto_neutral at sright, bounce
    show Alicanto_neutral at center  with MoveTransition(0.2)

    Al "As Safirah pointed out, you can't be eliminated from the game."
    Al "So there's no way to purposefully lose."

    show Alicanto_neutral at sright  with MoveTransition(0.2)
    show Red_annoyed at sleft, bounce

    if metRed:

        R "So we're just stuck here?"

    else:

        UR "So we're just stuck here?"

    hide Alicanto_neutral
    show Alicanto_annoyed at sright, bounce

    Al "Let me finish please."

    hide Red_annoyed
    hide Alicanto_annoyed
    show Alicanto_neutral at sright, bounce
    show Alicanto_neutral at center with MoveTransition(0.2)
    

    Al "However, if there's no way you can be eliminated, then you may as well be trapped here."

    hide Alicanto_neutral
    show Alicanto_happy at center, bounce

    Al "And I wouldn't be a very good host, game or otherwise, if I didn't allow my guests to leave!"
    Al "Especially if it's for a game!"

    hide Alicanto_happy
    show Alicanto_neutral at center, bounce

    Al "So, therefore, not only do you have your own rooms for a sense of safety and privacy."
    Al "But if the stress is simply too much for you, you can choose to leave the games."

    hide Alicanto_neutral
    show Alicanto_happy at center, bounce

    Al "And then, all you must do is sleep, and you will find yourself back in your normal life like it was just a dream."

    show Alicanto_happy at sleft with MoveTransition(0.2)
    show Zach_glare at sright, bounce

    if metZach:

        Z "So what's stopping us from leaving right now?"

    else:

        UZ "So what's stopping us from leaving right now?"
        
    Al "I'm so glad you asked."

    hide Alicanto_happy
    show Alicanto_neutral at sleft, bounce
    hide Zach_glare
    show Alicanto_neutral at center  with MoveTransition(0.2)

    Al "So, as I said, you can leave the games if the stress is too much for you."
    Al "Just come to see me in my office on the {color=#ffffff}first floor{/color} if that's the case."

    hide Alicanto_neutral
    show Alicanto_happy at center, bounce

    Al "However, you can only do so after the first round, you know, to give it a chance!"

    hide Alicanto_happy
    show Alicanto_mischievous at center, bounce

    Al "And for many of you... I think the prize would be quite... Convincing."

    show Alicanto_mischievous at sright with MoveTransition(0.2)
    show Red_surprise at sleft, bounce

    if metRed:

        R "Prize?"
        R "What prize?"

    else:

        UR "Prize?"
        UR "What prize?"

    Al "Oh, not much..."
    Al "Just a large amount of money."
    Al "Which seems to total at around..."
    Al "5 million, if I remember correctly?"

    hide Red_surprise
    show Alicanto_mischievous at center with MoveTransition(0.2)

    "What."

    show Alicanto_mischievous at sleft with MoveTransition(0.2)
    show Berry_shock at sright, bounce

    if metBerry:

        B "5 wha-?!" with hpunch
        B "5 million?!"
    
    else:

        UB "5 wha-?!" with hpunch
        UB "5 million?!"

    hide Berry_shock
    show Alicanto_mischievous at sright with MoveTransition(0.2)
    show Sebastian_surprise at sleft, bounce

    if metSebastian:

        S "That could help a lot of people."
        S "Why don't you use it to help them instead of using it to make all of this?"

    else:

        US "That could help a lot of people."
        US "Why don't you use it to help them instead of using it to make all of this?"

    hide Alicanto_mischievous
    show Alicanto_happy at sright, bounce
    
    Al "Oh, easy!"
    
    hide Sebastian_surprise
    show Alicanto_happy at center with MoveTransition(0.2)
    

    Al "I know my appearance and behaviour makes me seem like the opposite."

    hide Alicanto_happy
    show Alicanto_annoyed at center, bounce

    Al "But I really hate those who allow their greed to consume them."
    Al "I am in a situation where I can avoid a corrupt system simply because of my age and diet."
    Al "But many don't have my luck."

    hide Alicanto_annoyed
    show Alicanto_happy at center, bounce

    Al "So I just decided 'hey, why don't I give people from all over the world a chance'?"
    Al "Hence why you are all here."

    hide Alicanto_happy
    show Alicanto_neutral at center, bounce

    Al "And as for simple donating..."
    Al "Well, I DO do that."

    hide Alicanto_neutral
    show Alicanto_happy at center, bounce

    Al "All the time, it's just anonymous."

    hide Alicanto_happy
    show Alicanto_neutral at center, bounce

    Al "But at some point, it stops feeling like enough."
    
    "Huh, so he's not a rich asshole."
    "Though, the cynic in me keeps thinking he is and he's just doing it to make himself look good."
    "His methods definitely make him seem like one, though."

    show Alicanto_neutral at sright with MoveTransition(0.2)
    show Safirah_surprise at sleft, bounce

    Sa "Wait..."
    Sa "What do you mean by your 'age and diet'?"

    "Huh? I didn't even notice that."

    hide Alicanto_neutral
    show Alicanto_nervous at sright, bounce
    
    Al "Ah, right."
    Al "I forgot to tell you all."

    hide Safirah_surprise
    hide Alicanto_nervous
    show Alicanto_happy at sright, bounce
    show Alicanto_happy at center with MoveTransition(0.2)

    Al "I'm not human."

    "I... What?"
    "So he's just delusional."

    hide Alicanto_happy
    show Alicanto_nervous at center, bounce
    
    Al "Ah, I'm sorry, I forgot how that sounds."
    Al "I've been surrounded by my staff for so long."

    hide Alicanto_nervous
    show Alicanto_neutral at center, bounce

    Al "But I am what some know as an alicanto bird."

    show Alicanto_neutral at sright with MoveTransition(0.2)
    show Safirah_nervous at sleft, bounce
    
    Sa "Alicanto?"

    hide Safirah_nervous
    show Sebastian_sigh at sleft, bounce

    if metSebastian:

        S "I believe I can explain this one."

        hide Sebastian_sigh
        show Sebastian_neutral at Ssleft, bounce

        S "An alicanto is from Chilean mythology."
        S "A creature that eats ores like gold and silver."
        S "In the myth, those who successfully find an alicanto's nest would come home with treasures."
        S "However, it has also driven miners whose hearts were not pure off of cliffs."

    else:

        US "I believe I can explain this one."

        hide Sebastian_sigh
        show Sebastian_neutral at Ssleft, bounce

        US "An alicanto is from Chilean mythology."
        US "A creature that eats ores like gold and silver."
        US "In the myth, those who successfully find an alicanto's nest would come home with treasures."
        US "However, it has also driven miners whose hearts were not pure off of cliffs."

    hide Alicanto_neutral
    show Alicanto_happy at sright, bounce

    Al "Oh my, you're quite educated on my existence, Dr. Sebastian."

    $ metSebastian = True

    hide Sebastian_neutral
    show Sebastian_sigh at sleft, bounce

    S "Just Sebastian is fine."
    S "And mythology was just an interest of mine growing up."

    hide Sebastian_sigh
    show Sebastian_annoyed at Ssleft, bounce

    S "However, alicanto birds are simply a myth."
    S "They are not real."
    S "And they were never known to be able to take human form."
    S "So it simply isn't possible for you to be a mythical creature."

    hide Alicanto_happy
    show Alicanto_mischievous at sright, bounce

    Al "Ah, now THAT, is where you're wrong."

    hide Sebastian_annoyed
    show Alicanto_mischievous at center with MoveTransition(0.2)

    Al "Mythical creatures exist everywhere."
    Al "Sirens, vampires, even satyr, all exist."
    Al "Where else do you think these 'mythological' creatures come from?"
    Al "Simple imagination?"

    "Yes."
    "Obviously."

    show Alicanto_mischievous at sleft with MoveTransition(0.2)
    show Berry_shock at sright, bounce

    if metBerry:

        B "What the what?!" with hpunch

        hide Berry_shock
        show Berry_nervous at sright, bounce

        B "I'm sorry, I'm still stuck on the prize."

        hide Berry_nervous
        show Berry_shock at sright, bounce

        B "But are you seriously saying that you're some magical bird?!"
        B "And that creatures we thought were myths ACTUALLY exist?!"
    
    else:

        UB "What the what?!" with hpunch

        hide Berry_shock
        show Berry_nervous at sright, bounce

        UB "I'm sorry, I'm still stuck on the prize."

        hide Berry_nervous
        show Berry_shock at sright, bounce

        UB "But are you seriously saying that you're some magical bird?!"
        UB "And that creatures we thought were myths ACTUALLY exist?!"

    hide Alicanto_mischievous
    show Alicanto_nervous at sleft, bounce

    Al "I see you all don't believe me."

    hide Alicanto_nervous
    hide Berry_shock
    show Alicanto_happy at sleft, bounce
    show Alicanto_happy at center with MoveTransition(0.2)

    Al "But that is no matter!"
    Al "Disbelief is understandable, and I don't need you to believe me."

    hide Alicanto_happy
    show Alicanto_neutral at center, bounce

    Al "All you need to know is that I have existed for a long time."
    Al "My title of 'sir' is legitimate."
    Al "And my age, along with my need to consume gold and ores, is why I have so much to spend."
    Al "It's very easy for me to find and sell too, you see."

    mc "I think what helps to make this unbelievable is the fact that you're apparently an alicanto..."
    mc "That calls himself Alicanto."

    hide Alicanto_neutral
    show Alicanto_nervous at center, bounce

    Al "Ah, that..."
    Al "It is not a name I really connect with, it is just for the show."

    hide Alicanto_nervous
    show Alicanto_neutral at center, bounce

    Al "Actually, I don't have much of a name."
    Al "I technically have many to avoid people being aware of my long life-span, but then time passes and I have to change it."
    
    mc "So you might as well just be nameless."

    hide Alicanto_neutral
    show Alicanto_nervous at center, bounce

    Al "Yes, that's right."
    Al "There's no point developing a connection to a name I'm just going to eventually change."

    hide Alicanto_nervous
    show Alicanto_neutral at center, bounce

    Al "But the matter of my name is no concern."
    Al "Just simply call me Alicanto, that will be my name to you."

    show Alicanto_neutral at sright with MoveTransition(0.2)
    show Safirah_surprise at sleft, bounce
    
    Sa "So... That dream had more meaning than I thought?"

    hide Alicanto_neutral
    show Alicanto_happy at sright, bounce

    Al "Ah, yes!"
    Al "You're so observant, Safirah!"

    hide Safirah_surprise
    show Safirah_nervous at sleft, bounce

    Sa "Oh, umm..."

    hide Safirah_nervous
    show Safirah_happy at sleft, bounce

    Sa "Thank you."

    Al "You're quite welcome!"

    hide Alicanto_happy
    show Alicanto_neutral at sright, bounce

    Al "Anyway, as I was saying."

    hide Safirah_happy
    show Alicanto_neutral at center with MoveTransition(0.2)

    Al "I'm aware that you all had the same dream last night."
    Al "Some of you must be so curious as to why."
    Al "And..."

    hide Alicanto_neutral
    show Alicanto_happy at center, bounce

    Al "That was me!"

    show Alicanto_happy at sright with MoveTransition(0.2)
    show Sebastian_annoyed at Ssleft, bounce

    S "That's impossible."

    hide Alicanto_happy
    show Alicanto_mischievous at sright, bounce

    Al "Oh?"

    hide Alicanto_mischievous
    show Alicanto_happy at sright, bounce

    Al "Ah, right, your speciality is psychology, is it not?"
    Al "Why don't you enlighten me on your human knowledge on how it's impossible?"

    hide Sebastian_annoyed
    show Sebastian_sigh at sleft, bounce

    S "First of all, from a mythological standpoint..."

    hide Sebastian_sigh
    show Sebastian_annoyed at Ssleft, bounce

    S "Alicanto birds weren't known to dream walk either."
    S "And second of all, it was a simple stroke of luck and coincidence."
    S "The brain is complicated, it is entirely possible to dream the same dreams."
    S "Just like how it's possible for your dreams to predict the future."

    hide Alicanto_happy
    show Alicanto_mischievous at sright, bounce

    Al "Oh? A doctor using luck as an argument?"
    Al "And, Sebastian, before, you didn't even know I was real."
    Al "It's bold to assume you know what I'm capable of based off of human research."
    
    hide Alicanto_mischievous
    show Alicanto_happy at sright, bounce

    Al "I mean, how else do you think I managed to bring you all here from all around the world in one night?"
    Al "Especially since some of you are light sleepers."

    hide Sebastian_annoyed
    show Sebastian_surprise2 at Ssleft, bounce

    S "Well, I-"

    show Alicanto_happy at center with MoveTransition(0.2)
    show Flora_annoyed at sright, bounce

    F "Sebastian, please calm down."

    hide Flora_annoyed
    show Flora_sad at sright, bounce

    F "This is strange for us all."
    F "And this doesn't seem to be a situation where we can all just rationalise it with human logic."
    F "Some things just can't be explained."

    hide Sebastian_surprise2
    show Sebastian_sad at sleft, bounce

    S "Hm..."

    hide Sebastian_sad
    show Sebastian_sigh at sleft, bounce

    S "Fine..."

    hide Alicanto_happy
    show Alicanto_neutral at center, bounce

    Al "Thank you, Miss. Flora."

    hide Flora_sad
    hide Sebastian_sigh

    Al "Now, are there any other questions?"

    show Alicanto_neutral at sleft with MoveTransition(0.2)

    show Tsun_neutral at sright, bounce

    if metTsun:

        T "Two from me."

        hide Tsun_neutral
        show Tsun_serious at sright, bounce

        T "If you've spent most of your life in hiding."
        T "Why are you revealing yourself now in such a dangerous way?"
        T "And how do you have the title of 'Sir'?"
        T "Especially when there's no history of you."

    else:

        UT "Two from me."

        hide Tsun_neutral
        show Tsun_serious at sright, bounce

        UT "If you've spent most of your life in hiding."
        UT "Why are you revealing yourself now in such a dangerous way?"
        UT "And how do you have the title of 'Sir'?"
        UT "Especially when there's no history of you."

    Al "Excellent question, Dr. Tsun."
    Al "The first question is because..."

    hide Alicanto_neutral
    show Alicanto_nervous at sleft, bounce

    Al "I was bored."

    "What."
    "He has spent god knows how long hiding himself..."
    "And he's just decided to put himself on TV..."
    "Out of BOREDOM."
    "..."
    "Honestly, valid."

    hide Alicanto_nervous
    show Alicanto_neutral at sleft, bounce

    Al "As for your second question."
    Al "I WOULD answer it..."

    show Alicanto_neutral at center with MoveTransition(0.2)
    hide Tsun_serious

    $ metTsun = True

    Al "However, I need to keep SOME secrets about myself."

    hide Alicanto_neutral
    show Alicanto_happy at center, bounce

    Al "Don't you think?"

    show Alicanto_happy at sleft with MoveTransition(0.2)
    show Berry_shock at sright, bounce

    if metBerry:

        B "Really?!"
        B "Of all secrets to keep, it's about a title?!"
    
    else:

        UB "Really?!"
        UB "Of all secrets to keep, it's about a title?!"

    Al "Well, I need at least some mysteries about myself, don't I?"
    Al "Otherwise I wouldn't be as interesting as I am now."

    "More like a total nutcase."

    hide Alicanto_happy
    show Alicanto_neutral at sleft, bounce
    hide Berry_shock
    show Alicanto_neutral at center with MoveTransition(0.2)

    Al "Anything else?"

    "Nobody's talking."

    Al "No?"

    hide Alicanto_neutral
    show Alicanto_happy at center, bounce

    Al "Then meeting over!"
    Al "Please feel free to take the time to look around and get to know your fellow contestants, if you haven't already."
    Al "And I will meet you all in the evening for our first meal together!"

    hide Alicanto_happy

    "..."
    "... Weirdest..."
    "... Meeting..."
    "... Ever..."
    "I can't even say I've had worse cause I haven't."
    "But I guess it went better and calmer than I thought it'd be."
    "Anyway, everyone's leaving, so I guess I should too."

    show Alicanto_neutral at center, bounce

    Al "Ah, mx. Emerald."

    "Oh no."
    "What did I do?"

    if attackedmaid:

        "Is this about the maid?"

    mc "Uh, yes?"

    Al "May I discuss something with you in my office, please?"

    "Oh no."
    "Oh shit."
    "What's this about?"

    mc "Umm, sure?"

    hide Alicanto_neutral
    show Alicanto_happy at center, bounce

    Al "Excellent! Let us go right away, then!"

    mc "Oh no."
    
    jump ch07
