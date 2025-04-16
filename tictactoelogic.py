class TicTacToe:
    def __init__(self,arr):
       self.arr=arr
    def h_check(self):
        for i in self.arr:
            if sum(i)==0:
                return 'Player 1 wins!'
            elif sum(i)==3:
                return 'Player 2 wins!'
            
    def v_check (self) :
       lst=[]
       for i in range(3):
            for j in range(3) :
                lst. append(self.arr[j][i])
            if sum(lst)==0:
                return 'Player 1 wins!'
            elif sum(lst)==3:
                return 'Player 2 wins!'
            lst.clear()
    def d_check(self):
        lst=[]
        for i in range(3):
            lst.append(self.arr[i][i])
        if sum(lst)==0 :
            return 'Player 1 wins!'
        elif sum(lst)==3:
            return 'Player 2 wins!'
        lst. clear()
        for i in range(3):
            lst. append(self.arr[i][3-(i+1) ])
        if sum(lst)==0:
            return 'Player 1 wins!'
        elif sum(lst)==3:
            return 'Player 2 wins!'
    def full_check(self) :    
        out=self.h_check()
        if out is None:
            out=self.v_check()
            if out is None:
                out=self.d_check()
                if out is None:
                    return 'Draw!'
        return out
