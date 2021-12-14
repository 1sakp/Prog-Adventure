#from Game import *

def Theo_game():
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
            dead = "trying to run awey from the entity"
            return dead
      
      
      
Theo_game()