# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define James = Character("James")
define stranger = Character("Stranger", color = "#FF0000")
define Ricardo = Character("Ricardo", color = "#FF0000")
define WhiteSuitMan = Character("Unknown man", color = "#FF0000")
define Croc = Character("Croc", color = "#FFFFFF")
define BigBoss = Character("Big Boss", color = "#C0C0C0")

image beach = "beach.png"
image shack = "shack.png"
image forest = "forest.png"
image interiorShack = "interiorShack.png"
image Injured James = "bond_4.png"
image James = "bond.png"
image stranger = "stranger.png"
image Ricardo = "Ricardo.png"
image Croc = "Croc.png"
# The game starts here.

label start:
    stop music
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene beach

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Injured James

    # These display lines of dialogue.
    "As you awake from your slumber, you find yourself on a beach with the waves crashing at your feet."
    "You get up and realize you are a bit injured with scraps and cuts on your hands and knees."
    "You wonder how in the world did you end up here? You look to your left and see a man lying next to you, unconscience."
    " You then look to your right and see a shack with laughter spewing out. Infront of you there is a forest with bellowing calls from within."
    "Which path would you take?"
    menu:
        "The man":
            "You walked up to the man. He seems to be injured with a deep gash on his head. You decide to give him a gentle shake. He awakens and looks into your eyes with fear."
            hide Injured James
            show stranger
            stranger "\"WHO ARE YOU!!!\" He exclaims as he takes out his blade, pointing it towards your throat."
            "You pause, and think of an answer to give the stranger."
            "Which answer would you give?"
            hide stranger
            menu:
                "\"Your Friend, James.\"":
                    show Injured James
                    James "\"I'm your friend, James. Don't you remember me?\""
                    hide Injured James
                    show stranger
                    stranger "\"James?\""
                    stranger "\"I never recall ever having a friend named James!\", says the stranger with anger and fustration."
                    "The knife, a sheepfoot switchblade, inched ever so close to your throat."
                    hide stranger
                    show Injured James
                    James "\"Wait!\", you say in a panic."
                    James "\"You need to get help!, your head is wide open.\", you explained."
                    "Taking a closer look at the man's wound you see that he must be in a critical condition. His skull is cracked open
                    with a portion of brain matter showing."
                    "The immense amount of blood makes you question how this man is even able to speak or not feel this ungodly type of pain."
                    "The man slowly lowers his weapon, allowing you to rip off the fabric on the sleeves of your dress shirt and fashion a makeshift bandage around his head."
                    "The man winces alittle but immediately calms himself, showing he isn't any regular man. He must be trained either by military or by criminals."
                    "He then regrets his actions towards you and apologies saying "
                    hide Injured James
                    show stranger
                    stranger "\"Sorry for the misunderstanding Antonio...err I mean James\"."
                    hide stranger
                    show Injured James
                    James "\"No problem. But what's your name?\""
                    hide Injured James
                    show stranger
                    stranger "\"My name is...My name...I'm sorry I can't seem to remember who I am.\""
                    hide stranger
                    "You decide to look around and see a shack with men exiting the premises."
                    scene shack
                    "They were all very odd looking...and your gut instincts told you that they're no where close to decent men. Most looked monstrous carrying all forms of weapons and all having builds of various heights but muscular masses."
                    show Injured James
                    "What will you do now?"
                    menu:
                        "Return to the stranger, break into the shack for shelter and tend to him.":
                            "As you both approach the shack, you feel warmth on side of your oblique. You peer down and see the sheepfoot knife stuck into your side. You then collapse to the floor."
                            hide Injured James
                            show stranger
                            stranger "\"I remember you James Bond! I won't let you foil our plan. I hope the next we meet, it'll be in Hell!\""
                            "You lose consciousness and fall into the dark abyss."
                            scene black with fade
                            "You died. The End."
                            # You died
                        "Attempt to kill the stranger. No witnesses.":
                            scene beach
                            "Walking back from the shack, you decide the severely injured stranger might slow you down, thus you pick up a sturdy rock hiding it behind your back."
                            show stranger
                            stranger "\"Did you find anything or anyone to help me out with this headache?\""
                            "Without any remorse or empathy, you swiftly strike at the stranger, but within a fraction of a second, the stranger already wielding his sheepfoot blade, slits your wrist containing the rock."
                            "He then kicks at your shin, causing you to fall into the sand. The stranger straddles you saying"
                            stranger "\"You must think I'm a fool to not remember your name James Bond. It's a shame you didn't kill me when I was unconscience. Goodnight, James.\""
                            "The stranger puts his knife to your throat, and with enough pressure, slowly drags it across. You gasp for air and your vision becomes spotty until darkness envelops your sight."
                            scene black with fade
                            "You died. The End."
                            # You died
                "\"Your Brother.\"":
                    show Injured James
                    James "\"I'm your brother, don't you remember me?\""
                    hide Injured James
                    show stranger
                    stranger "\"Antonio? I'm sorry. I think I hurt my head pretty bad, so I'm a bit discombobulated.\""
                    hide stranger
                    "Worrying about his safety you decide to find a place to help nurse the man back to health. As you pick him up, you spot a shady shack and both shuffle towards it."
                    scene shack
                    "You both hear laughter and banter from within the shack. You knock thrice on the door, causing a giant man in a white suit, and white crocodile leather shoes to open the door."
                    show Croc
                    "You observe the man seeing he has a bulky build, much like that of a heavyweight boxer, a scar above his right eye and a crooked nose which must've healed from a heavy blow years prior."
                    "I guess I'll call him Croc you think to your self."
                    "You notice on the man's hip, he's sporting a Ruger Super GP100. A revolver usually accustomed with holding 8 bullets. Might be useful later you thought."
                    "The man gives you a look of confusion and angst, but upon seeing the stranger with you he then yelled"
                    WhiteSuitMan "\"Ricardo!!! What the hell happened to you, mi amigo!\""
                    "Ignoring you, Croc grabs Ricardo and hulls him within the shack filled with 6 monstrous figures barely resembling men. You feel a chill down your spine at the site of them."
                    "As the man in the white suit turns around you see a small tattoo on the back of Croc's neck resembling a human skull with 4 horns. The mark of the Syndicate! These men must be all members!"
                    "Instantly you remember your mission given to you by the MI6."
                    BigBoss "\"Stop the Syndicate from reaching the temple of Doom at all cost, James.\""
                    hide Croc
                    "What will you do?"
                    show Injured James
                    menu:
                        "While Croc is distracted with Ricardo, reach for the revolver and kill these men.":
                            "You grab the Ruger, spin the cylinder, cock back the hammer 8 times and quickly but surely dispatch every one of these syndicate members."
                            "Mission Accomplished! Ruthlessness was increased! You lost a significant amount of connectivity to your Conscience."
                            scene black with fade
                            "You won but at what cost. The End."
                            # You win negative ending
                        "Enter and help Ricardo too.":
                            "Although you felt a vast amount of fear looking into the room, you compose yourself and calmly walk into the shack."
                            scene interiorShack
                            show Croc
                            Croc "\"Bring ze Espolon Blanco for Ricardo!\""
                            "You see the bottle on the table near the other men. You disregard them and pick up the bottle handing it over to Croc."
                            show Croc
                            Croc "\"Gracias, mi niño. Drink Ricardo, drink.\""
                            "Ricardo resting on a bench, allows Croc to carefully lift his head and pour the tequila into his mouth."
                            "Croc pickes up a first aid kit to mend the head injury Ricardo has."
                            Croc "\"Mi niño, did you care for Ricardo's wound like this?\""
                            hide Croc
                            show Ricardo
                            Ricardo "\"This is my brother I told you much about! Antonio!\""
                            hide Ricardo
                            show Croc
                            "Croc looks at you with curiousity and disbelief seeing as you look nothing like Ricardo, but then shifts his attention towards Ricardo."
                            Croc "\"Well then \"Antonio\", you can stay the night with us for now.\""
                            hide Croc
                            "You converse with the men through the night, not catching a wink of sleep but you've noticed matching tattoos on each of the men."
                            "The tattoo; A human skull with 4 horns...The mark of the syndicate. You begin to recall your mission given to you by the Boss."
                            BigBoss "\"Stop the Syndicate from reaching the temple of Doom at all cost, James.\""
                            "That's another problem for another day, you think as you drift off to sleep.\""
                            with fade
                            "You awake with a burly, calloused hand on your mouth. Your blurred vision slowly focuses to see Croc and the other men all starting at you."
                            show Croc
                            Croc "\"Antonio, we are on a mission to find a rare treasure in this forest. This treasure holds an immeasureable amount of power in the right hands."
                            Croc "\"Seeing as you're Ricardo's brother, are you willing to join us on this quest?\""
                            hide Croc
                            show James
                            "What will you say?"
                            menu:
                                "Yes.":
                                    scene forest
                                    "You and the men, including the injured Ricardo leave in search of the Temple of Doom."
                                    "On the way, you all encounter dangerous on animals along the way, but the men dispatched of them with ease."
                                    "Upon seeing the temple, all the men shout in uproar as they realized their journey has neared it's end. They all (including yourself) began to run towards the temple, but Croc noticed something the others didn't and shouted:"
                                    show Croc
                                    Croc "\"STOP! MI HERMANOS! IT'S AN ILLUSION!\""
                                    hide Croc
                                    "The trap was an optical illuision with a grand pit filled with spikes and bones infront of the Temple of Doom. The 6 men fell to their deaths, yet you caught Ricardo while on the edge of the pit. You look to your left and see Croc struggling to keep hold of a tree root."
                                    show Ricardo
                                    Ricardo "\"Antonio! Please! Pull me up quick!\""
                                    hide Ricardo
                                    show James
                                    "What will you do?"
                                    menu:
                                        "Let go.":
                                            "As you look into Ricardo's eyes, you then remember your mission again."
                                            show James
                                            James "\"The name is Bond...James Bond.\""
                                            "Ricardo's eyes widen, realizing his mistake."
                                            with fade
                                            hide James
                                            show Ricardo
                                            Ricardo "Ah...I forgot Antonio died years ago...Curse you James Bond."
                                            "You release your grip, letting Ricardo's fingers slip through yours. You watch him fall to his death."
                                            hide Ricardo
                                            show Croc
                                            Croc "\"Antonio!!! Antonio!!!! You bastard!!!! YOU BASTARD!!!\""
                                            hide Croc
                                            "You hear the cries of a dying man as you coldly walked away from the pit."
                                            "Mission Successful. Ruthlessness was increased! You lost a significant amount of connectivity to your Conscience."
                                            scene black with fade
                                            "The End."
                                            # You win negative ending
                                        "Pull Ricardo up and help Croc.":
                                            "You struggle as you try to pull up Ricardo. You succeeded! You both then rush to Croc's side and pull him up as well."
                                            show James
                                            James "\"I believe we shouldn't continue. This place my be cursed. You lost all your men and we just barely survived. This isn't the way to get poweer.\""
                                            "Croc considers your words..."
                                            hide James
                                            show Croc
                                            Croc "\"We turn back...We need to find a doctor for Ricardo anyway. But we'll be back with a greater number of men.\""
                                            hide Croc
                                            scene beach
                                            "It seems you've stopped them for now. But you must cling to them, to stop the impending Doom."
                                            "Mission Semi-Successful. Kindness was increased! You gained a significant amount of connectivity to your Conscience."
                                            scene black with fade
                                            "To Be Continued..."
                                            # You win positive ending
                                "No.":
                                    scene beach
                                    "You depart from the men. Looking at the rising sun, with tears knowing you weren't courageous to carry out your first mission. You spend your days looking for a way to contact the MI6."
                                    scene black with fade
                                    "Mission failed. The End."
                                    # You lose.
                #"\"I don't know.\"":
                    #pass
                    # You died
        "The shack":
            scene shack
            "You walk up to the door of the shack and knock on the door."
            show Croc
            "A man in a white suit, and white crocodile leather shoes opens the door."
            "You observe the features of the man noticing he had a bulky build, much like that of a heavyweight boxer, a scar above his right eye and a crooked nose which must've healed from a heavy blow years prior opens the door."
            "The man with a crooked smile, says "
            WhiteSuitMan "\"Hombre Muerto.\""
            "You instantly recognize those words: \"Dead man\""
            "You try to turn away to run, but the man pulls out a revolver and \"Bang\", thats all you hear before everything goes black."
            scene black with fade
            "You died. The End."
            # You died
        "The forest":
            scene forest
            "You run straight foward into the forest driven by some unknown curiosity."
            "As you are running through the forest, you see a clearing and decided to head for that instead."
            "Unfortunately, this wasn't a clearing but the edge of a cliff. You try to stop yourself, but it's too late."
            "You fell to your death."
            scene black with fade
            "You died. The End."
            # You died
    # This ends the game.

    return
