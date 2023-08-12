import random
from random import choices 

def main():
    print('How many lottery contestants:')
    lott_num = int(input())
    input_list = input('Enter the team names in order separated by a space: \n')
    print("\n")
    team_list = input_list.split()
    team_dct = {(i+1): team_list[i] for i in range(len(team_list))}
    print(team_dct)
    lottery_choices(lott_num, team_dct)

def lottery_choices(lott_num, team_dct):
    lott_amount = [(2**i)*3 for i in range(lott_num)]
    print(lott_amount)
    teams = [ i + 1 for i in range(lott_num)]
    for i in range(lott_num):
        print(i)
        prob = [count/sum(lott_amount) for count in lott_amount]
        print(prob)
        pick = choices(teams, prob)[0]
        print(f"Pick number {i+1} is Team {team_dct['pick']}")
        lott_amount[pick-1] = 0 

main()
