from sys import exit
from random import randint

class Room(object):

    def enter(self):
        print "This room is not yet configured."
        exit(1)

class Main(object):

    def __init__(self, room_map):
        self.room_map = room_map

    def play(self):
        current_room = self.room_map.opening_room()
        last_room = self.room_map.next_room('end')

        while current_room != last_room:
            next_room_name = current_room.enter()
            current_room = self.room_map.next_room(next_room_name)

        current_room.enter()

class Death(Room):
     
     message = [
        "You died Bruh", 
        "Rest In Peace"
        ]
     def enter(self):
        index = 0
        while index < len(Death.message):
          print Death.message[index]
          index = index + 1
        exit(1)

class Home(Room):

    def enter(self):
        print "The objective of this game is to go through a full hard day of school, then be rewarded some halal food in the end"
        print "In every class you will recieve a test with one question, get that question wrong and you will die"
        print "You goal is to make the right decisions, and get all the questions right. Eat Halal at the end"
        print "Do not make any stupid choices, you will die!"
        print "Lets begin"
        print ""
        print "You just came out of a very deep sleep"

        print "Have you decided to attend school today? (yes or no)"


        decision = raw_input("> ")

        if decision == "yes":
          print "You've brushed your teeth"
          print "Taken a shower"
          print "Put on clothes"
          print "left for school"
          print ""
          return 'computerScience'
      
        elif decision == "no":
          return 'death'

        else:
          "Please input the only two options above, don't make me add some more engish classes to your schedule"
          return 'home'

class ComputerScience(Room):

    def enter(self):
        print "Welcome to Computer Science!"
        print "Today your very scary teacher Mr.Stern will give you a very informative lesson on methods"
        print "You are very hungry, do you eat the cliff bar in your bag or wait until the end of the day? (eat or nah)"
        
        choice = raw_input("> ")
        print ""
        if choice == "nah":
          print "You made the right choice"
          print "Now you will recieve you daily computer science test/question"
          print "Function Definition: def fire(food):"
          print 'What is "food" in the function Definition?'
          print "A.) Variable"
          print "B.) Parameter"
          print "C.) Argument"
          print "(a, b, or c)"
          print ""
          answer = raw_input("> ")

          if answer == "b":
            print "Correct you get to move onto to the next class!"
            return 'calculus'
          else: 
            return 'death'

        elif choice == "eat":
          return 'death'
        else: 
          "Please input the only two options above, don't make me add some more engish classes to your schedule"
          return 'computerScience'

class Calculus(Room):

    def enter(self):
        print "Welcome to Calculus"
        print "Mr.Hatlee will give a very basic introduction on how to solve a definate integral"
        print "As Mr.Hatlee is talking, Arthur asks you for yesterday's math homework"
        print "Do you give it to him?"
        print "(yes or no)"
        print ""
        give = raw_input("> ")

        if give == "yes":
          return 'death'
        elif give == "no":
          print "good, you would've died"
          print "time for your question/test"
          print "v(t) = 2x what is the average value between t=2 and t=6?"
          print "A.) 8"
          print "B.) 32"
          print "C.) 4"
          print "(a,b or c)"
          print ""
          mult = raw_input("> ")

          if mult == "a":
            print "Correct! You are moving on to the next class"
            print "" 
            return 'english'
          else: 
            return 'death'
        else:
          "Please input the only two options above, don't make me add some more engish classes to your schedule"
          return 'calculus'

class English(Room):

    def enter(self):
        print "Welcome to the last class of the day, english"
        print "We saved the best for last"
        print "As Ms. Wynne is giving her important lesson on Higher Level Questions, Noel asks you a life or death question"
        print "What time is it?"
        print "Do you tell him the time?"
        print "(yes or no)"

        time = raw_input("> ")

        if time == "no":
          print "Nice choice, Noel was taken out of the class by Ms Wynne and was never heard of again"
          print "Time for your last and final question/test of the day"
          print 'Ms.Wynne says that "A Higher level Question should not be a yes or no question" is she correct?'
          print "(yes or no)"
          print "" 
          last = raw_input("> ")
          
          if last == "yes":
            print "Correct, you can finally go get Halal Food"
            return 'food'
          elif last == "no":
            return 'death'
          else:
             print "You entered the answer wrong. YOU DIE!"
             return 'death'

        elif time == "yes":
          return 'death'
        else:
          print "Please input the only two options above, don't make me add some more engish classes to your schedule"
          return 'english'

class Food(Room):
    
    def enter(self):
        print "You finally made it to the most fire part of the day"
        print "You ordered a chicken over rice with hot and white sauce, do you buy a drink?"
        print "(yes or no)"
        print "" 
        drink = raw_input("> ")

        if drink == "yes":
          print "Good, no drink and that hot suace would've killed you"
          return 'end'
        elif drink == "no":
          print "Hot sauce was too hot"
          return 'die'
        else: 
            print "yes or no bruh?"
            print "Don't type in anything else"
            return 'food'
            

class End(Room):
  
    def enter(self):
        print ""
        print "Finally back home"
        print "Hopefully Tuesday will be less stressful"
        exit(0)

class Map(object):

    room = {

        'home': Home(),
        'calculus': Calculus(),
        'computerScience': ComputerScience(),
        'death': Death(),
        'end': End(),
        'english': English(),
        'food': Food(),

    }

    def __init__(self, start_room):
        self.start_room = start_room

    def next_room(self, room_name):
        val = Map.room.get(room_name)
        return val

    def opening_room(self):
        return self.next_room(self.start_room)

startRoom = Map('home')
game = Main(startRoom)
game.play()

