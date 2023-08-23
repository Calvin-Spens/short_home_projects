from tkinter import *
from tkinter import ttk
from random import choices 

def main():
    print('How many lottery contestants:')
    lott_num = int(input())
    input_list = input('Enter the team names, lowest odds first: \n')
    team_list = input_list.split()
    team_dct = {(i+1): team_list[i] for i in range(len(team_list))}
    print(team_dct)
    lottery_choices(lott_num, team_dct)

def lottery_choices(lott_num, team_dct):
    lott_amount = [(2**i)*3 for i in range(lott_num)]
    teams = [ i + 1 for i in range(lott_num)]
    for i in range(lott_num):
        prob = [count/sum(lott_amount) for count in lott_amount]
        pick = int(choices(teams, prob)[0])
        print(f"Pick number {i+1} is Team {team_dct[pick]}")
        lott_amount[pick-1] = 0 

main()

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()