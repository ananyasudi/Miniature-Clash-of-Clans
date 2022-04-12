import os
# from random import Random, random
import random
from turtle import clear
from click import style
from src.constants import *
import colorama
from colorama import Fore,Back,Style

from src.huts import townhall

colorama.init()

king  =[list("|\/|"),
        list("|__|")]
class board():
    def __init__(self,rows,colms):
        self.num_rows=rows
        self.num_colms=colms
        self.num_huts=5
        self.board=[]
        for i in range(self.num_rows):
            self.board.append([])
            for j in range(self.num_colms):
                if(i==0 or i==self.num_rows-1):
                    self.board[i].append('_')
                elif j==0 or j==self.num_colms-1:
                    self.board[i].append('|')
                else:
                    self.board[i].append(' ')
        print(len(self.board[0]))
    
    def print_board(self,king,hut,townhall):
        # os.system('clear')
        
        for i in range(self.num_rows):
            for j in range(self.num_colms):
                tobeprinted=self.board[i][j]
                if tobeprinted=='H':#get hit points of hut and if returned num is 1--> Green 2-->yellow 3-->red
                    num=hut.hitpoints_status(i,j) 
                    if num==1:
                        print(Back.GREEN+tobeprinted+Style.RESET_ALL,end='')

                    elif num==2:
                        print(Back.YELLOW+tobeprinted+Style.RESET_ALL,end='')
                        
                    elif num==3:
                        print(Back.RED+tobeprinted+Style.RESET_ALL,end='')
                        
                   
                elif tobeprinted=='T':
                    x=townhall.hit_pts
                    actual=townhall_hitpts
                    if x<=actual and x>=actual//2:
                        print(Back.GREEN+'T'+Style.RESET_ALL,end='')
                    elif x<=actual//2 and x>=actual//2:
                        print(Back.YELLOW+'T'+Style.RESET_ALL,end='')
                    elif x<=actual//2 and x>0:
                        print(Back.RED+'T'+Style.RESET_ALL,end='')

                elif tobeprinted=='X':
                    print(Back.BLUE+'X'+Style.RESET_ALL,end='')
                
                else:
                    print(Fore.CYAN+self.board[i][j]+ Style.RESET_ALL,end='')
            print(end='\n')

        


