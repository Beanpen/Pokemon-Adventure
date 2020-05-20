import turtle
import time
import random
j = random.randint(1, 3)
k = random.randint(1, 2)
wn = turtle.Screen()
tt = turtle.Turtle()


t = "What would you like to do?"
a = "A"
b = "B"
c = "C"
d = 'Please enter a valid answer!'

print("Candice: Hello! Welcome to the Pokemon World! I’m a Candice Carter. and I’m an Ace Trainer!")
print("Alright, now it is your turn to choose one of those three Pokémons as your first Pokémon pal!")
print(a + ' to choose Bulbasaur')
print(b + ' to choose Squirtle')
print(c + ' to choose Charmander')

wn.setup(1450, 600)

ua = 0
ua_0 = 0
ua_1 = 0
ua_2 = 0
ua_3 = 0
ua_4 = 0
ua_5 = 0
ua_6 = 0

import turtle
import time
import random
j = random.randint(1, 3)
k = random.randint(1, 2)
wn = turtle.Screen()
tt = turtle.Turtle()


t = "What would you like to do?"
a = "A"
b = "B"
c = "C"
d = 'Please enter a valid answer!'

print("Candice: Hello! Welcome to the Pokemon World! I’m a Candice Carter. and I’m an Ace Trainer!")
print("Alright, now it is your turn to choose one of those three Pokémons as your first Pokémon pal!")
print(a + ' to choose Bulbasaur')
print(b + ' to choose Squirtle')
print(c + ' to choose Charmander')

wn.setup(1450, 600)
wn.bgpic('doc.png')
tt.penup()
tt.goto(150, 150)
tt.pendown()
tt.write('Candice: Hello! Welcome to the Pokemon World!\nI’m a Candice Carter and I’m an Ace Trainer!'
         '\nAlright, now it is your turn to choose one of those three Pokémons\nas your first Pokémon pal!', font=("Arial", 18, "normal"))
wn.textinput('Hit Enter','Press ENTER to continue')
wn.clear()
wn.bgpic('bcs.png')

ua = 0
ua_0 = 0
ua_1 = 0
ua_2 = 0
ua_3 = 0
ua_4 = 0
ua_5 = 0
ua_6 = 0

while ua not in ['A', 'a', 'B', 'b', 'C', 'c']:
    ua = wn.textinput(d, 'Which one do you want to choose(A/B/C):\nA Bulbasaur\nB Squirtle\nC Charmander')
    if ua in ['A', 'a']:
        tt.clear()
        wn.bgpic('Bulbasaur.png')
        tt.penup()
        tt.goto(0,0)
        tt.left(90)
        tt.forward(250)
        tt.pendown()
        tt.write('Wow, you chose Bulbasaur! You guys are going be the greatest pals!', font=("Arial", 18, "normal"))

        while ua_0 not in ['Yes', 'yes', 'y', 'Y', 'No', 'no', 'n', 'N']:
            ua_0 = wn.textinput('Ignore Me', 'Would you like to name your Bulbasaur?\nY/N:')
            if ua_0 in ['Y', 'y', 'Yes', 'yes']:
                tt.penup()
                tt.left(180)
                tt.forward(20)
                tt.pendown()
                name = wn.textinput('Name your Pokemon', 'What name would you like to call him?')
                tt.write(name + '?' + 'What a cute name!', font=("Arial", 18, "normal"))
                wn.textinput('Hit Enter', 'Press ENTER to continue')
            elif ua_0 in ['N', 'n', 'No', 'no']:
                tt.penup()
                tt.left(180)
                tt.forward(20)
                tt.pendown()
                tt.write('Alright, your Bulbasaur seems a little bit sad...', font=("Arial", 18, "normal"))
                wn.textinput('Hit Enter', 'Press ENTER to continue')

        wn.clear()
        wn.bgpic('doc.png')
        tt.penup()
        tt.goto(150, 150)
        tt.pendown()
        tt.write('Do you want to train your pokemon?',  font=("Arial", 18, "normal"))
        wn.textinput('Hit Enter', 'Press ENTER to continue')
        wn.clear()
        wn.bgpic('gym.png')

        while ua_1 not in ['A', 'a', 'B', 'b', 'C', 'c']:
            ua_1 = wn.textinput('Training', "A Yes, I\'d love to.\nB to exit.")
            if ua_1 in ['A', 'a']:
                tt.penup()
                tt.goto(-150, 150)
                tt.pendown()
                tt.write('After a long time training, your Bulbasaur evolved to a Ivysaur! Congrats!', font=("Arial", 18, "normal"))
                wn.bgpic('i.png')
                tt.penup()
                tt.goto(-150,130)
                tt.pendown()
                time.sleep(1)
                time.sleep(1)
                wn.clear()
                wn.bgpic('forest.png')

                while ua_2 not in ['A', 'a', 'B', 'b', 'C', 'c']:
                    ua_2 = wn.textinput('Forest Adventure', 'Do you want to enter the forest?\nA Yes, I would like to go!' + '\nB No, never.')
                    if ua_2 in ['A', 'a']:
                        wn.clear()
                        tt.penup()
                        tt.goto(-200, 220)
                        tt.pendown()
                        tt.write('A wild pokemon just jumped out from the grass! It is a wild Pikachu!', font=("Arial", 18, "normal"))
                        wn.bgpic('p.png')
                        tt.penup()
                        tt.goto(-200, 200)
                        tt.pendown()
                        time.sleep(1)
                        tt.write('Do you want to catch it?', font=("Arial", 18, "normal"))
                        tt.penup()
                        tt.goto(-200, 250)
                        tt.pendown()

                        while ua_4 not in ['A', 'a', 'B', 'b', 'C', 'c']:
                            ua_4 = wn.textinput('!!!', 'A Yasss! \nB I do not want this cuuute Pikachu.')
                            if ua_4 in ['A', 'a']:
                                wn.clear()
                                wn.bgpic('pb.png')
                                while ua_5 not in ['A', 'a', 'B', 'b', 'C', 'c']:
                                    ua_5 = wn.textinput('Pokemon Ball', 'Which Poké Ball do you want to use?')
                                    if ua_5 in ['A', 'a']:
                                        while ua_6 not in ['Yes', 'yes', 'y', 'Y', 'No', 'no', 'n', 'N']:
                                            ua_6 = wn.textinput('Failed', 'Do you want to try again?(Y/N)')
                                            if ua_6 in ['Yes', 'yes', 'y', 'Y']:
                                                while j != 1:
                                                    ua_6 = wn.textinput('Failed', 'Do you want to try again?(Y/N)')
                                                    j = random.randint(1, 3)
                                                wn.clear()
                                                wn.bgpic('pt.png')
                                                tt.write('OMG! You have caught the Pikachu!',
                                                         font=("Arial", 18, "normal"))
                                                wn.textinput('Hit Enter', 'Press ENTER to continue')
                                                wn.clear()
                                                wn.bgpic('te.png')
                                            elif ua_6 in ['No', 'no', 'n', 'N']:
                                                tt.write('Oh no! The wild Pikachu just ran away!',
                                                         'Press ENTER to continue', font=("Arial", 18, "normal"))
                                                time.sleep(1)
                                                wn.clear()
                                                wn.bgpic('te.png')
                                    elif ua_5 in ['B', 'b']:
                                        while ua_6 not in ['Yes', 'yes', 'y', 'Y', 'No', 'no', 'n', 'N']:
                                            ua_6 = wn.textinput('Failed', 'Do you want to try again?(Y/N)')
                                            if ua_6 in ['Yes', 'yes', 'y', 'Y']:
                                                while k != 1:
                                                    ua_6 = wn.textinput('Failed', 'Do you want to try again?(Y/N)')
                                                    k = random.randint(1, 3)
                                                wn.clear()
                                                wn.bgpic('pt.png')
                                                tt.write('OMG! You have caught the Pikachu!',
                                                         font=("Arial", 18, "normal"))
                                                wn.textinput('Hit Enter', 'Press ENTER to continue')
                                                wn.clear()
                                                wn.bgpic('te.png')
                                            elif ua_6 in ['No', 'no', 'n', 'N']:
                                                tt.write('Oh no! The wild Pikachu just ran away!',
                                                         'Press ENTER to continue', font=("Arial", 18, "normal"))
                                                time.sleep(1)
                                                wn.clear()
                                                wn.bgpic('te.png')
                                    elif ua_5 in ['C', 'c']:
                                        wn.clear()
                                        wn.bgpic('pt.png')
                                        tt.write('OMG! You have caught the Pikachu!', font=("Arial", 18, "normal"))
                                        wn.textinput('Hit Enter', 'Press ENTER to continue')
                                        wn.clear()
                                        wn.bgpic('te.png')

                    elif ua_2 in ['B', 'b']:
                        wn.clear()
                        tt.penup()
                        tt.goto(0, -50)
                        tt.pendown()
                        tt.write('You left the forest.', font=("Arial", 18, "normal"))
                        wn.textinput('Hit Enter', 'Press ENTER to continue')
                        wn.clear()
                        wn.bgpic('te.png')

            elif ua_1 in ['B', 'b']:
                wn.clear()
                tt.penup()
                tt.goto(-150, 150)
                tt.pendown()
                wn.bgpic('Bulbasaur.png')
                tt.write('Oh no! Your Bulbasaur left you!', font=("Arial", 18, "normal"))
                tt.penup()
                tt.goto(-150, 130)
                tt.pendown()
                time.sleep(1.5)
                wn.clear()
                wn.bgpic('forest.png')

                while ua_3 not in ['A', 'a', 'B', 'b', 'C', 'c']:
                    ua_3 = wn.textinput('Forest Adventure', 'Do you want to enter the forest?\nA Yes, I\'d like to come!\nB No.')
                    wn.clear()
                    wn.bgpic('forest.png')
                    if ua_3 in ['A', 'a']:
                        wn.clear()
                        tt.penup()
                        tt.goto(-150, 150)
                        tt.pendown()
                        tt.write('You cannot go without your Pokemon.', font=("Arial", 18, "normal"))
                        wn.textinput('Hit Enter', 'Press ENTER to continue')
                        wn.clear()
                        wn.bgpic('te.png')
                    if ua_3 in ['B', 'b']:
                        wn.clear()
                        tt.penup()
                        tt.goto(-150, 150)
                        tt.pendown()
                        tt.write('You left the forest.', font=("Arial", 18, "normal"))
                        wn.textinput('Hit Enter', 'Press ENTER to continue')
                        wn.clear()
                        wn.bgpic('te.png')

    elif ua in ['B', 'b']:
        tt.clear()
        wn.bgpic('Squirtle.png')
        tt.penup()
        tt.goto(0,0)
        tt.left(90)
        tt.forward(250)
        tt.pendown()
        tt.write('Wow, you chose Squirtle! You guys are going be the greatest pals!', font=("Arial", 18, "normal"))

        while ua_0 not in ['Yes', 'yes', 'y', 'Y', 'No', 'no', 'n', 'N']:
            ua_0 = wn.textinput('Ignore Me', 'Would you like to name your Squirtle?\nY/N:')
            if ua_0 in ['Y', 'y', 'Yes', 'yes']:
                tt.penup()
                tt.left(180)
                tt.forward(20)
                tt.pendown()
                name = wn.textinput('Name your Pokemon', 'What name would you like to call him?')
                tt.write(name + '?' + 'What a cute name!', font=("Arial", 18, "normal"))
                wn.textinput('Hit Enter', 'Press ENTER to continue')
            elif ua_0 in ['N', 'n', 'No', 'no']:
                tt.penup()
                tt.left(180)
                tt.forward(20)
                tt.pendown()
                tt.write('Alright, your Squirtle seems a little bit sad...', font=("Arial", 18, "normal"))
                wn.textinput('Hit Enter', 'Press ENTER to continue')

        wn.clear()
        wn.bgpic('doc.png')
        tt.penup()
        tt.goto(150, 150)
        tt.pendown()
        tt.write('Do you want to train your pokemon?',  font=("Arial", 18, "normal"))
        wn.textinput('Hit Enter', 'Press ENTER to continue')
        wn.clear()
        wn.bgpic('gym.png')

        while ua_1 not in ['A', 'a', 'B', 'b', 'C', 'c']:
            ua_1 = wn.textinput('Training', "A Yes, I\'d love to.\nB to exit.")
            if ua_1 in ['A', 'a']:
                tt.penup()
                tt.goto(-150, 150)
                tt.pendown()
                tt.write('After a long time training, your Squirtle evolved to a Wartortle! Congrats!', font=("Arial", 18, "normal"))
                wn.bgpic('w.png')
                tt.penup()
                tt.goto(-150,130)
                tt.pendown()
                time.sleep(1)
                time.sleep(1)
                wn.clear()
                wn.bgpic('beach.png')

                while ua_2 not in ['A', 'a', 'B', 'b', 'C', 'c']:
                    ua_2 = wn.textinput('Beach Adventure', 'Do you want to go to the West Beach?\nA Yes, I would like to go!' + '\nB No, never.')
                    if ua_2 in ['A', 'a']:
                        wn.clear()
                        tt.penup()
                        tt.goto(-200, 220)
                        tt.pendown()
                        tt.write('A wild pokemon just jumped out from the ocean! It is a wild Gyarados!', font=("Arial", 18, "normal"))
                        wn.bgpic('g.png')
                        tt.penup()
                        tt.goto(-200, 200)
                        tt.pendown()
                        time.sleep(1)
                        tt.write('Do you want to catch it?', font=("Arial", 18, "normal"))
                        tt.penup()
                        tt.goto(-200, 250)
                        tt.pendown()

                        while ua_4 not in ['A', 'a', 'B', 'b', 'C', 'c']:
                            ua_4 = wn.textinput('!!!', 'A Yasss! \nB I do not want this Gyarados.')
                            if ua_4 in ['A', 'a']:
                                wn.clear()
                                wn.bgpic('pb.png')
                                while ua_5 not in ['A', 'a', 'B', 'b', 'C', 'c']:
                                    ua_5 = wn.textinput('Pokemon Ball', 'Which Poké Ball do you want to use?')
                                    if ua_5 in ['A', 'a']:
                                        while ua_6 not in ['Yes', 'yes', 'y', 'Y', 'No', 'no', 'n', 'N']:
                                            ua_6 = wn.textinput('Failed', 'Do you want to try again?(Y/N)')
                                            if ua_6 in ['Yes', 'yes', 'y', 'Y']:
                                                while j != 1:
                                                    ua_6 = wn.textinput('Failed', 'Do you want to try again?(Y/N)')
                                                    j = random.randint(1, 3)
                                                wn.clear()
                                                wn.bgpic('gt.png')
                                                tt.write('OMG! You have caught the Gyarados!',
                                                         font=("Arial", 18, "normal"))
                                                wn.textinput('Hit Enter', 'Press ENTER to continue')
                                                wn.clear()
                                                wn.bgpic('te.png')
                                            elif ua_6 in ['No', 'no', 'n', 'N']:
                                                tt.write('Oh no! The wild Gyarados just ran away!',
                                                         'Press ENTER to continue', font=("Arial", 18, "normal"))
                                                time.sleep(1)
                                                wn.clear()
                                                wn.bgpic('te.png')
                                    elif ua_5 in ['B', 'b']:
                                        while ua_6 not in ['Yes', 'yes', 'y', 'Y', 'No', 'no', 'n', 'N']:
                                            ua_6 = wn.textinput('Failed', 'Do you want to try again?(Y/N)')
                                            if ua_6 in ['Yes', 'yes', 'y', 'Y']:
                                                while k != 1:
                                                    ua_6 = wn.textinput('Failed', 'Do you want to try again?(Y/N)')
                                                    k = random.randint(1, 3)
                                                wn.clear()
                                                wn.bgpic('gt.png')
                                                tt.write('OMG! You have caught the Gyarados!',
                                                         font=("Arial", 18, "normal"))
                                                wn.textinput('Hit Enter', 'Press ENTER to continue')
                                                wn.clear()
                                                wn.bgpic('te.png')
                                            elif ua_6 in ['No', 'no', 'n', 'N']:
                                                tt.write('Oh no! The wild Gyarados just ran away!',
                                                         'Press ENTER to continue', font=("Arial", 18, "normal"))
                                                time.sleep(1)
                                                wn.clear()
                                                wn.bgpic('te.png')
                                    elif ua_5 in ['C', 'c']:
                                        wn.clear()
                                        wn.bgpic('gt.png')
                                        tt.write('OMG! You have caught the Gyarados!', font=("Arial", 18, "normal"))
                                        wn.textinput('Hit Enter', 'Press ENTER to continue')
                                        wn.clear()
                                        wn.bgpic('te.png')

                    elif ua_2 in ['B', 'b']:
                        wn.clear()
                        tt.penup()
                        tt.goto(0, -50)
                        tt.pendown()
                        tt.write('You left the West Beach.', font=("Arial", 18, "normal"))
                        wn.textinput('Hit Enter', 'Press ENTER to continue')
                        wn.clear()
                        wn.bgpic('te.png')

            elif ua_1 in ['B', 'b']:
                wn.clear()
                tt.penup()
                tt.goto(-150, 150)
                tt.pendown()
                wn.bgpic('Squirtle.png')
                tt.write('Oh no! Your Squirtle left you!', font=("Arial", 18, "normal"))
                tt.penup()
                tt.goto(-150, 130)
                tt.pendown()
                time.sleep(1.5)
                wn.clear()
                wn.bgpic('beach.png')

                while ua_3 not in ['A', 'a', 'B', 'b', 'C', 'c']:
                    ua_3 = wn.textinput('Beach Adventure', 'Do you want to go to the West Beach?\nA Yes, I\'d like to come!\nB No.')
                    wn.clear()
                    wn.bgpic('beach.png')
                    if ua_3 in ['A', 'a']:
                        wn.clear()
                        tt.penup()
                        tt.goto(-150, 150)
                        tt.pendown()
                        tt.write('You cannot go without your Pokemon.', font=("Arial", 18, "normal"))
                        wn.textinput('Hit Enter', 'Press ENTER to continue')
                        wn.clear()
                        wn.bgpic('te.png')
                    if ua_3 in ['B', 'b']:
                        wn.clear()
                        tt.penup()
                        tt.goto(-150, 150)
                        tt.pendown()
                        tt.write('You left the beach.', font=("Arial", 18, "normal"))
                        wn.textinput('Hit Enter', 'Press ENTER to continue')
                        wn.clear()
                        wn.bgpic('te.png')

    elif ua in ['C', 'c']:
        tt.clear()
        wn.bgpic('Charmander.png')
        tt.penup()
        tt.goto(0,0)
        tt.left(90)
        tt.forward(250)
        tt.pendown()
        tt.write('Wow, you chose Charmander! You guys are going be the greatest pals!', font=("Arial", 18, "normal"))

        while ua_0 not in ['Yes', 'yes', 'y', 'Y', 'No', 'no', 'n', 'N']:
            ua_0 = wn.textinput('Ignore Me', 'Would you like to name your Charmander?\nY/N:')
            if ua_0 in ['Y', 'y', 'Yes', 'yes']:
                tt.penup()
                tt.left(180)
                tt.forward(20)
                tt.pendown()
                name = wn.textinput('Name your Pokemon', 'What name would you like to call him?')
                tt.write(name + '?' + 'What a cute name!', font=("Arial", 18, "normal"))
                wn.textinput('Hit Enter', 'Press ENTER to continue')
            elif ua_0 in ['N', 'n', 'No', 'no']:
                tt.penup()
                tt.left(180)
                tt.forward(20)
                tt.pendown()
                tt.write('Alright, your Charmander seems a little bit sad...', font=("Arial", 18, "normal"))
                wn.textinput('Hit Enter', 'Press ENTER to continue')

        wn.clear()
        wn.bgpic('doc.png')
        tt.penup()
        tt.goto(150, 150)
        tt.pendown()
        tt.write('Do you want to train your pokemon?',  font=("Arial", 18, "normal"))
        wn.textinput('Hit Enter', 'Press ENTER to continue')
        wn.clear()
        wn.bgpic('gym.png')

        while ua_1 not in ['A', 'a', 'B', 'b', 'C', 'c']:
            ua_1 = wn.textinput('Training', "A Yes, I\'d love to.\nB to exit.")
            if ua_1 in ['A', 'a']:
                tt.penup()
                tt.goto(-150, 220)
                tt.pendown()
                tt.write('After a long time training, your Charmander evolved to a Charmeleon! Congrats!', font=("Arial", 18, "normal"))
                wn.bgpic('c.png')
                tt.penup()
                tt.goto(-150,130)
                tt.pendown()
                time.sleep(1)
                time.sleep(1)
                wn.clear()
                wn.bgpic('m.png')

                while ua_2 not in ['A', 'a', 'B', 'b', 'C', 'c']:
                    ua_2 = wn.textinput('Mountain Adventure', 'Do you want to go to the Mountains?\nA Yes, I would like to go!' + '\nB No, never.')
                    if ua_2 in ['A', 'a']:
                        wn.clear()
                        tt.penup()
                        tt.goto(-200, 230)
                        tt.pendown()
                        tt.write('A wild pokemon just jumped out from a rock! It is a wild Eevee!', font=("Arial", 18, "normal"))
                        wn.bgpic('e.png')
                        tt.penup()
                        tt.goto(-200, 200)
                        tt.pendown()
                        time.sleep(1)
                        tt.write('Do you want to catch it?', font=("Arial", 18, "normal"))
                        tt.penup()
                        tt.goto(-200, 250)
                        tt.pendown()

                        while ua_4 not in ['A', 'a', 'B', 'b', 'C', 'c']:
                            ua_4 = wn.textinput('!!!', 'A Yasss! \nB I do not want this Eevee.')
                            if ua_4 in ['A', 'a']:
                                wn.clear()
                                wn.bgpic('pb.png')
                                while ua_5 not in ['A', 'a', 'B', 'b', 'C', 'c']:
                                    ua_5 = wn.textinput('Pokemon Ball', 'Which Poké Ball do you want to use?')
                                    if ua_5 in ['A', 'a']:
                                        while ua_6 not in ['Yes', 'yes', 'y', 'Y', 'No', 'no', 'n', 'N']:
                                            ua_6 = wn.textinput('Failed', 'Do you want to try again?(Y/N)')
                                            if ua_6 in ['Yes', 'yes', 'y', 'Y']:
                                                while j != 1:
                                                    ua_6 = wn.textinput('Failed', 'Do you want to try again?(Y/N)')
                                                    j = random.randint(1, 3)
                                                wn.clear()
                                                wn.bgpic('et.png')
                                                tt.write('OMG! You have caught the Eevee!',
                                                         font=("Arial", 18, "normal"))
                                                wn.textinput('Hit Enter', 'Press ENTER to continue')
                                                wn.clear()
                                                wn.bgpic('te.png')
                                            elif ua_6 in ['No', 'no', 'n', 'N']:
                                                tt.write('Oh no! The wild Eevee just ran away!',
                                                         'Press ENTER to continue', font=("Arial", 18, "normal"))
                                                time.sleep(1)
                                                wn.clear()
                                                wn.bgpic('te.png')
                                    elif ua_5 in ['B', 'b']:
                                        while ua_6 not in ['Yes', 'yes', 'y', 'Y', 'No', 'no', 'n', 'N']:
                                            ua_6 = wn.textinput('Failed', 'Do you want to try again?(Y/N)')
                                            if ua_6 in ['Yes', 'yes', 'y', 'Y']:
                                                while k != 1:
                                                    ua_6 = wn.textinput('Failed', 'Do you want to try again?(Y/N)')
                                                    k = random.randint(1, 3)
                                                wn.clear()
                                                wn.bgpic('et.png')
                                                tt.write('OMG! You have caught the Eevee!',
                                                         font=("Arial", 18, "normal"))
                                                wn.textinput('Hit Enter', 'Press ENTER to continue')
                                                wn.clear()
                                                wn.bgpic('te.png')
                                            elif ua_6 in ['No', 'no', 'n', 'N']:
                                                tt.write('Oh no! The wild Eevee just ran away!',
                                                         'Press ENTER to continue', font=("Arial", 18, "normal"))
                                                time.sleep(1)
                                                wn.clear()
                                                wn.bgpic('te.png')
                                    elif ua_5 in ['C', 'c']:
                                        wn.clear()
                                        wn.bgpic('et.png')
                                        tt.write('OMG! You have caught the Eevee!', font=("Arial", 18, "normal"))
                                        wn.textinput('Hit Enter', 'Press ENTER to continue')
                                        wn.clear()
                                        wn.bgpic('te.png')

                    elif ua_2 in ['B', 'b']:
                        wn.clear()
                        tt.penup()
                        tt.goto(0, -50)
                        tt.pendown()
                        tt.write('You left the mountains.', font=("Arial", 18, "normal"))
                        wn.textinput('Hit Enter', 'Press ENTER to continue')
                        wn.clear()
                        wn.bgpic('te.png')

            elif ua_1 in ['B', 'b']:
                wn.clear()
                tt.penup()
                tt.goto(-150, 150)
                tt.pendown()
                wn.bgpic('Charmander.png')
                tt.write('Oh no! Your Charmander left you!', font=("Arial", 18, "normal"))
                tt.penup()
                tt.goto(-150, 130)
                tt.pendown()
                time.sleep(1.5)
                wn.clear()
                wn.bgpic('m.png')

                while ua_3 not in ['A', 'a', 'B', 'b', 'C', 'c']:
                    ua_3 = wn.textinput('Mountain Adventure', 'Do you want to go to the mountains?\nA Yes, I\'d like to come!\nB No.')
                    wn.clear()
                    wn.bgpic('m.png')
                    if ua_3 in ['A', 'a']:
                        wn.clear()
                        tt.penup()
                        tt.goto(-150, 150)
                        tt.pendown()
                        tt.write('You cannot go without your Pokemon.', font=("Arial", 18, "normal"))
                        wn.textinput('Hit Enter', 'Press ENTER to continue')
                        wn.clear()
                        wn.bgpic('te.png')
                    if ua_3 in ['B', 'b']:
                        wn.clear()
                        tt.penup()
                        tt.goto(-150, 150)
                        tt.pendown()
                        tt.write('You left the mountains.', font=("Arial", 18, "normal"))
                        wn.textinput('Hit Enter', 'Press ENTER to continue')
                        wn.clear()
                        wn.bgpic('te.png')

wn.mainloop()