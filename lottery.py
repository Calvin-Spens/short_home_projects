import random

print('How many lottery contestants:')
lott_num = int(input())
lott_amount = [ (i+1)*5 for i in range(lott_num)]
print(lott_amount) 

