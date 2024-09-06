import random
import logging
from time import time

#Μεγαλύτερη τυχαιότητα
random.seed(time()*1234)

#Μορφοποίηση του logger
logging.basicConfig()
logging.getLogger().setLevel(logging.INFO)

#Κανόνες από αρχείο
def read_instructions():
    ans = input("Would you like to read the rules ? (Y/N) \n")
    if ans.upper() == 'Y':
        rules = open("rps_rules.txt", "r")
        print(rules.read())
        rules.close()

#Αρχικοποίηση σημαντικών μεταβλητών
possible_moves = ['R', 'P', 'S']
player_score = 0
computer_score = 0

#Είσοδος γύρων
def rounds():
    rnds = int(input("\nHow many rounds you wish to play ?  \n"))
    while rnds <= 0:
        logging.warning("Enter a valid number of rounds: ")
        rnds = int(input())
    return rnds    

#Συνάρτηση επικύρωσης
def is_valid(player):
    if player.upper() in possible_moves:
        return True
    else:
        logging.warning("\nInvalid input !!")
        return False

#Είσοδος χρήστη
def user_input():
    print("Enter your choice (R/P/S):")
    player = input()
    while not is_valid(player):
        logging.warning("\nEnter your choice again (R/P/S): ")
        player = input()
    return str(player.upper())

#Είσοδος υπολογιστή
def computer_input():
    x = random.randint(0, 2)
    comp = possible_moves[x]
    return comp

#Εύρεση νικητή γύρου
def round_winner(player, computer):
    global player_score, computer_score
    logging.debug("\nPlayer played: " + str(player.upper()) + " Computer played: " + str(computer))        

    if str(player) == str(computer):
        logging.warning("\nTie!! Play again!")
        player_new = user_input()
        computer_new = computer_input()
        # recursion to play again for the point
        round_winner(player_new, computer_new)
    elif(str(player) == "P" and str(computer) == "R") or (str(player) == "S" and str(computer) == "P") or (str(player) == "R" and str(computer) == "S"):
        player_score += 1
        logging.info("\nPlayer wins this round !")
    else:
        computer_score += 1
        logging.info("\nComputer wins this round !")

    logging.debug("\nPlayer Score: " + str(player_score) +
                 "\nComputer Score: " + str(computer_score) + "\n")

#Ευρεση νικητή γύρου (χωρίς μηνύματα)
def round_winner_testing_gui(player, computer):
    outcomes = ["Tie", "Player wins", "Computer wins"]

    if str(player) == str(computer):
        return outcomes[0]
    elif((str(player) == "P" and str(computer) == "R") or (str(player) == "S" and str(computer) == "P") or (str(player) == "R" and str(computer) == "S")):
        return outcomes[1]
    else:
        return outcomes[2]

#Εύρεση νικητή παιχνιδιού
def display_outcome():
    logging.info("\nPlayer Score: " + str(player_score) +
                 "\nComputer Score: " + str(computer_score) + "\n")

    if player_score == computer_score:
        logging.info("\nGame ended on a tie!")
    elif player_score > computer_score:
        logging.info("\nPlayer wins the game!")
    else:
        logging.info("\nComputer wins the game!")
    
    return player_score, computer_score

#Συνάρτηση παιχνιδιού 
def game(rnds):
    logging.info("\n*** The game starts here ***\n")
    for i in range(rnds):
        print("\n\tRound " + str(i+1))
        player = user_input()
        computer = computer_input()
        round_winner(player, computer)
    logging.info("\n*** The game ends here ***\n")

#Έλεγχος αν "τρέχει" αυτό το αρχείο
if __name__ == '__main__':
    read_instructions()
    rnds = rounds()
    game(rnds)
    display_outcome()