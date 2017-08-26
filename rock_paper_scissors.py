# Create a two player rock-paper-scissors game

# Rules:
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
trig = 1
while trig != "q" :
        p1 = raw_input("Player 1: Choose among roc-pap-sci: ")
        p2 = raw_input("Player 2: Choose among roc-pap-sci: ")

        p1_low = p1.lower()
        p2_low = p2.lower()

        if (p1_low == p2_low):
            print ("Tie!, Play again?")
            trig = raw_input("Press Q to quit or Return to continue: ")
            if trig.lower() == "q":
                exit()
            else:    
                continue            
        elif (p1_low == "roc") and (p2_low == "sci"):
            print ("Player 1 Wins")
            trig = raw_input("Press Q to quit or Return to continue: ")
            if trig.lower() == "q":
                exit()
            else:    
                continue
        elif (p1_low == "roc") and (p2_low == "pap"):
            print ("Player 2 wins")
            trig = raw_input("Press Q to quit or Return to continue: ")
            if trig.lower() == "q":
                exit()
            else:    
                continue         
        elif (p1_low == "pap") and (p2_low == "roc"):
            print ("Player 1 wins")
            trig = raw_input("Press Q to quit or Return to continue: ")
            if trig.lower() == "q":
                exit()
            else:    
                continue                   
        elif (p1_low == "pap") and (p2_low == "sci"):
            print ("Player 2 wins")         
            trig = raw_input("Press Q to quit or Return to continue: ")
            if trig.lower() == "q":
                exit()
            else:    
                continue
        elif (p1_low == "sci") and (p2_low == "rock"):
            print ("Player 2 Wins")
            trig = raw_input("Press Q to quit or Return to continue: ")
            if trig.lower() == "q":
                exit()
            else:    
                continue                        
        elif (p1_low == "sci") and (p2_low == "pap"):
            print ("Player 1 Wins")
            trig = raw_input("Press Q to quit or Return to continue: ")
            if trig.lower() == "q":
                exit()
            else:    
                continue                        
#         trig = raw_input("Q to quit or C to continue: ")
#         if trig.lower() == "q":
#             exit()

        
    
