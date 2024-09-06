import rps_main as rps
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *

#Αρχικοποίηση μεταβλητών γύρου και βαθμολογίας
rounds = 0
rounds_flag = 0
comp_score = 0
player_score = 0

#Συνάρτηση παιχνιδιού
def play():
    #Έλεγχος αν το πεδίο των γύρων είναι κενό
    if len(rnds.get()) == 0:
        messagebox.showerror("Empty field", "Input number of rounds!")
        return

    global rounds_flag, comp_score, player_score

    #Λήψη κίνησης παίκτη
    playermove = player.get()
    if playermove == "Rock":
        playermove = "R"
    elif playermove == "Paper":
        playermove = "P"
    else:
        playermove = "S"

    #Λήψη κίνησης υπολογιστή
    comp_inp = rps.computer_input()
    
    rnd_win = rps.round_winner_testing_gui(playermove,comp_inp)
    if comp_inp == "R":
        comp_inp = "Rock"
    elif comp_inp == "P":
        comp_inp = "Paper"
    else:
        comp_inp = "Scissors"
    
    #Εμφάνιση κίνησης υπολογιστή
    comp.config(state="normal")
    comp.delete(0,"end")
    comp.insert(0,comp_inp)
    comp.config(state="readonly")

    #Αύξηση των βαθμολογιών
    if rnd_win == "Computer wins":
        comp_score += 1
    if rnd_win == "Player wins":
        player_score += 1     

    #Εμφάνιση νικητή γύρου
    if rnd_win == "Tie":    
        result_list.insert(END,"Round ended on a tie!")
        #Επανάληψη σε περίπτωση ισοπαλίας 
        result_list.insert(END, "Round will be replayed!")
        rounds_flag -= 1
    else:
        result_list.insert(END, str(rnd_win) + " this round!")    
    
    rounds_flag += 1

    #Λήξη παιχνιδιού και εμφάνιση νικητή
    if rounds == rounds_flag:
        if player_score == comp_score:
            result_list.insert(END, "Game ended on a tie!")
            messagebox.showinfo("Game Outcome", "Game ended on a tie!")
        elif player_score > comp_score:
            result_list.insert(END, "Player wins the game!")
            messagebox.showinfo("Game Outcome", "Player wins the game!")
        else:
            result_list.insert(END, "Computer wins the game!")
            messagebox.showinfo("Game Outcome", "Computer wins the game!")
        result_list.insert(END, "Player Score: " + str(player_score) + " Computer Score: " + str(comp_score))

#Ορισμός γύρων
def set_rnds():
    global rounds
    #Έλεγχος αν το πεδίο είναι άδειο
    if len(rnds.get()) == 0:
        messagebox.showerror("Empty field", "Input number of rounds!")
        return
    #Έλεγχος αν ο αριθμός των γύρων είναι έγκυρος    
    if int(rnds.get())<=0:
        messagebox.showerror("Invalid input", "Input a valid number of rounds!")
        return 
    rounds = int(rnds.get())
    messagebox.showinfo("Rounds Set", "Rounds Set To " + str(rounds))

#Παράθυρο εφαρμογής
root=tk.Tk()
root.title("Rock Paper Scissors")
root.geometry('550x400')

#Πρώτο Frame - Είσοδος Γύρου
frame1=tk.Frame(master=root)
label1=tk.Label(master=frame1, width=19, justify=tk.CENTER, text="Number of rounds")
rnds=tk.Entry(master=frame1, width=12, justify=tk.CENTER)
rndbtn=tk.Button(master=frame1, width=20, text="Set rounds", command=set_rnds)
label1.grid(row=0, column=0, padx=7, pady=10)
rnds.grid(row=0, column=1, padx=7, pady=10)
rndbtn.grid(row=0, column=2, padx=7, pady=10)

#Δεύτερο Frame - Είσοδος κίνησης παίκτη
frame2=tk.Frame(master=root)
label2=tk.Label(master=frame2, width=10, justify=tk.CENTER, text="Player\'s move")
player=ttk.Combobox(master=frame2, width=10, values=("Rock", "Paper", "Scissors"), state="readonly")
player.current(0)
playbutton=tk.Button(master=frame2, width=20, text="Play", command=play)
label2.grid(row=1, column=0, padx=30, pady=10)
player.grid(row=1, column=1, padx=10, pady=10)
playbutton.grid(row=1, column=2, padx=10, pady=10)

#Τρίτο Frame - Εμφάνιση κίνησης υπολογιστή
frame3=tk.Frame(master=root)
label3=tk.Label(master=frame3, width=25, justify=tk.CENTER, text="Computer\'s move")
comp=tk.Entry(master=frame3, width=25, justify=tk.CENTER, state="readonly")
label3.grid(row=2, column=0, padx=30, pady=10)
comp.grid(row=2, column=1, padx=50, pady=10)

#Πεδίο Λίστας - Εμφάνιση αποτελεσμάτων
result_list = tk.Listbox(master=root, font=("calibri",13), width=35, height=11, justify=tk.CENTER)

#Εισαγωγή των frames στο παράθυρο
frame1.pack()
frame2.pack()
frame3.pack()
result_list.pack()

#Κατασκευή και καταστροφή παραθύρου εφαρμογής
tk.mainloop()
root.destroy()