from Game import *

def Theo_game_intro():
      print("""
Dr. G: You are now in SCP-6969420-3. 
it seems to be a theater. 
Try to find the key and open the last door. 
            """)


      print("""
A man: What are you doing, you need to get to the stage. 
There is only five minutes left before it starts. 
            """)

      Follow = input("""
Dr. G: The entity seems to be safe, but I can't guarantee it. 
You can either follow him or you can try to get awey.  
            """)
      
      if Follow.lower() == "follow":
            print("""
You continue to follow him and he pushes you on to a stage. 
You look on to the crowed and see houndreds of people. 
You take a secound look and see that the woman and men are 
copies of eachother and all of them have no face. 
            """)
      
      else:
            print("""
You run away from the entity as fast as you can...
            """)
            dead = """
trying to run awey from the entity
            """
            return dead
      
      dance = input("""
Dr. G: DANCE!!!! DANCE FOR FUCK SAKE!!!!!
IF TOU DON'T YOU WILL DIE: 
            """)
      
      if dance.lower() == "dance":
            print("""
You start doing the macarena...
Suddenly you start hearing the macarena and everyone in the 
crowed stands up. 
You see all the entitys also starts doing the macarena.                   
            """)
      else:
            print("""
You stand there still in confusion and don't know what
to do. You see everyone standing up. 
            """)
            dead = """
standing on stage and being eaten. 
            """
            return dead
            
      print("""
You finnich dancing and start heading backstage. 
You see three doors (One to the left, one in the middle and
one to the right), a mirror, a plant and the exit. 
            """)
      
      
            
Theo_game_intro()