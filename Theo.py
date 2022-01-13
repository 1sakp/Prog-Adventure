#from Game import *

def Theo_game_intro():
      print("""
Dr. G: You are now in SCP-6969420-3. 
it seems to be a theater. 
Try to find the key and open the last door. """)


      print("""
A man: What are you doing, you need to get to the stage. 
There is only five minutes left before it starts. """)

      Follow = input("""
Dr. G: The entity seems to be safe, but I can't guarantee it. 
You can either follow him or you can try to get awey. """)
      
      if "follow" in Follow.lower():
            print("""
You continue to follow him and he pushes you on to a stage. 
You look on to the crowed and see houndreds of people. 
You take a secound look and see that the woman and men are 
copies of eachother and all of them have no face. """)
      
      else:
            print("""
You run away from the entity as fast as you can... """)
            dead = """
trying to run awey from the entity"""
            return dead
      
      dance = input("""
Dr. G: DANCE!!!! DANCE FOR FUCK SAKE!!!!!
IF TOU DON'T YOU WILL DIE: """)
      
      if "dance" in dance.lower():
            print("""
You start doing the macarena...
Suddenly you start hearing the macarena and everyone in the 
crowed stands up. 
You see all the entitys also starts doing the macarena. """)
      else:
            print("""
You stand there still in confusion and don't know what
to do. You see everyone standing up. """)
            dead = """
standing on stage and being eaten. """
            return dead
            
def The_room_of_many_rooms_and_other_stuff_it_also_have_an_exit_but_you_need_a_key_to_open_so_go_in_all_the_rooms_first_to_get_the_key():
      out = 1
      
      while out == 1:
            print("""
When you are done dancing you enter backstage. 
There you see 3 door (one to the left, one in the middle 
and one to the right), a mirror on the wall, a plant
in the corner. 
                  """)
            
            choice = input("""

                           """)      
      
            
Theo_game_intro()