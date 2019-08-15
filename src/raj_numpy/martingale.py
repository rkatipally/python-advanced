"""Assess a betting strategy. 			  		 			 	 	 		 		 	  		   	  			  	
 			  		 			 	 	 		 		 	  		   	  			  	
Copyright 2018, Georgia Institute of Technology (Georgia Tech) 			  		 			 	 	 		 		 	  		   	  			  	
Atlanta, Georgia 30332 			  		 			 	 	 		 		 	  		   	  			  	
All Rights Reserved 			  		 			 	 	 		 		 	  		   	  			  	
 			  		 			 	 	 		 		 	  		   	  			  	
Template code for CS 4646/7646 			  		 			 	 	 		 		 	  		   	  			  	
 			  		 			 	 	 		 		 	  		   	  			  	
Georgia Tech asserts copyright ownership of this template and all derivative 			  		 			 	 	 		 		 	  		   	  			  	
works, including solutions to the projects assigned in this course. Students 			  		 			 	 	 		 		 	  		   	  			  	
and other users of this template code are advised not to share it with others 			  		 			 	 	 		 		 	  		   	  			  	
or to make it available on publicly viewable websites including repositories 			  		 			 	 	 		 		 	  		   	  			  	
such as github and gitlab.  This copyright statement should not be removed 			  		 			 	 	 		 		 	  		   	  			  	
or edited. 			  		 			 	 	 		 		 	  		   	  			  	
 			  		 			 	 	 		 		 	  		   	  			  	
We do grant permission to share solutions privately with non-students such 			  		 			 	 	 		 		 	  		   	  			  	
as potential employers. However, sharing with other current or future 			  		 			 	 	 		 		 	  		   	  			  	
students of CS 7646 is prohibited and subject to being investigated as a 			  		 			 	 	 		 		 	  		   	  			  	
GT honor code violation. 			  		 			 	 	 		 		 	  		   	  			  	
 			  		 			 	 	 		 		 	  		   	  			  	
-----do not edit anything above this line--- 			  		 			 	 	 		 		 	  		   	  			  	
 			  		 			 	 	 		 		 	  		   	  			  	
Student Name: Tucker Balch (replace with your name) 			  		 			 	 	 		 		 	  		   	  			  	
GT User ID: tb34 (replace with your User ID) 			  		 			 	 	 		 		 	  		   	  			  	
GT ID: 900897987 (replace with your GT ID) 			  		 			 	 	 		 		 	  		   	  			  	
"""

import numpy as np
import matplotlib.pyplot as plt


def author():
    return 'knelluri3'  # replace tb34 with your Georgia Tech username.


def gtid():
    return 903475494  # replace with your GT ID number


def get_spin_result(win_prob):
    result = False
    rnd = np.random.random()
    # print(rnd)
    if rnd <= win_prob:
        result = True
    return result


def test_code_limited():
    win_prob = 0.47  # set appropriately to the probability of a win
    np.random.seed(gtid())  # do this only once
    counter1 = 0
    while counter1 < 10:
        winLst = []
        winLst.append(0)
        cntr = 0
        max_bet_amount = 256
        episode_winnings = 0
        game_over = False
        while episode_winnings < 80 and cntr < 1000 and not game_over:
            won = False
            bet_amount = 1
            while not won:
                if max_bet_amount >= bet_amount:
                    pass
                else:
                    if max_bet_amount > 0:
                        bet_amount = max_bet_amount
                    else:
                        print("Game Over")
                        game_over = True
                        break
                won = get_spin_result(win_prob)  # test the roulette spin
                if won:
                    max_bet_amount = max_bet_amount + bet_amount
                    episode_winnings = episode_winnings + bet_amount
                else:
                    max_bet_amount = max_bet_amount - bet_amount
                    episode_winnings = episode_winnings - bet_amount
                    bet_amount = bet_amount * 2
                cntr += 1
                winLst.append(episode_winnings)
                print(f'max_bet_amount: {max_bet_amount} - episode_winnings: {episode_winnings}')

        for n in range(winLst.__len__(), 1000):
            winLst.append(episode_winnings)
        winnings = np.array(winLst)
        print(cntr)
        #print(winnings)
        counter1 += 1
        #plot_data(winLst)


def test_code_un_limited():
    win_prob = 0.47  # set appropriately to the probability of a win
    max_amount = 256
    np.random.seed(gtid())  # do this only once
    counter1 = 0
    while counter1 < 1:
        winLst = []
        winLst.append(0)
        cntr = 0
        episode_winnings = 0
        while episode_winnings < 80 and cntr < 1000:
            won = False
            bet_amount = 1
            while not won:
                max_amount -= bet_amount
                won = get_spin_result(win_prob)  # test the roulette spin
                if won:
                    episode_winnings = episode_winnings + bet_amount
                else:
                    episode_winnings = episode_winnings - bet_amount
                    bet_amount = bet_amount * 2
                cntr += 1
                winLst.append(episode_winnings)
                print(bet_amount)

        for n in range(winLst.__len__(), 1000):
            winLst.append(episode_winnings)
        winnings = np.array(winLst)
        #print(cntr)
        #print(winnings)
        counter1 += 1
        #plot_data(winLst)


def plot_data(df, title="Roulette Winnings"):
    plt.plot(df)
    plt.title(title)
    plt.xlabel("Spins")
    plt.ylabel("Winnings")
    plt.show()


if __name__ == "__main__":
    test_code_limited()
