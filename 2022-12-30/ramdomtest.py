
# import random
import random
  
class OddOrEven():
    def __init__(self):
        print("Odd or Even\n")
        inp1=int(input("Press 1 to play with computer"))
        if inp1==1:
            self.game()
    def game(self):
        print("Chose Batting or Balling")
        inp2=int(input("Press 1 for Batting \n Press 2 for Balling"))
        if inp2==1:
            list1 = [1, 2, 3, 4, 5, 6]
            print(random.choice(list1)) 
            
        
        
        
       
