from nba_api.stats.endpoints import playercareerstats

from script import score_1

kareem_stats = playercareerstats.PlayerCareerStats(player_id='76003')
kareem_stats.get_dict()







array = ['a', 10.8, "string", [13, ' s']]
print(array[0])

mixed_list = [[["r,g,b"],["r,g,b"],["r,g,b"]]
              ,[["r,g,b"],["r,g,b"],["r,g,b"]]
              ,[["r,g,b"],["r,g,b"],["r,g,b"]]] #
matrix = [array, array, array]
print(matrix[0][2])
print()

"""
i = int(input("Enter a positive integer"))
while i < 0:
    try:
        i = int(input("Enter a positive integer"))
        break
    except ValueError:
        print("BRUH")

iteration = int(input("Input the number of numbers you want"))
total = 0
array = []
for n in range(iteration):
    total += int(input("Enter any integer"))
print(total)
"""

name  = ""#input("Enter name:")
each_letter = []
for letter in name:
    each_letter.append(letter)
print(each_letter[7:2:-1])

print("Rock is 0, Paper is 1, Scissors is 2")
player1 = int(input("Your Move"))
player2 = int(input("Your Move"))
score_1 = 0
score_2 = 0
while (score_1+score_2) < 3:
    if player1 == player2:
        print("TIE")
    elif (player1 == 0 and player2 == 2) or (player1 == 1 and player2 == 0) or (player1 == 2 and player2 == 1):
        score_1 += 1
        print("PLAYER 1 WINS")
    else:
        score_2 += 1
        print("PLAYER 2 WINS")