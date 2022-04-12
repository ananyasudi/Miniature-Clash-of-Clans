from timeit import default_timer as timer

from numpy import append
# from goto import goto, label, comefrom
# @goto
from src.huts import *
from src.board import *
from src.input import *
from src.person import *
from src.barbarian import *
from src.constants import *
from sys import exit
LEVEL=1



Board=board(num_rows,num_colms)
Hut=hut(hut_hit_points)
Townhall=townhall(townhall_hitpts)
Wall=wall(wall_hitpts)
bar_list=[]
bal_list=[]
arc_list=[]
# Barbarian=barbarian()
eagle_arrow=False
spawn_pts=[(5,50),(24,10),(44,50)]
spawn_pts_bal=[(5,90),(5,10),(44,10)]
spawn_pts_arc=[(24,90),(44,90),(44,75)]

Board.board[4][50]='1'
Board.board[25][10]='2'
Board.board[45][50]='3'

Board.board[4][90]='4'
Board.board[4][10]='5'
Board.board[45][10]='6'

Board.board[24][90]='7'
Board.board[45][90]='8'
Board.board[45][75]='9'


Townhall.build_townhall(Board.board)
Wall.place_walls(Townhall.coordinates,Board.board)
Hut.build_huts(Board.board)
Canons1=canon(canon_hitpts)
Canons2=canon(canon_hitpts)
Canons3=canon(canon_hitpts)
Canons4=canon(canon_hitpts)

canons_list=[Canons1,Canons2]
Canons1.place_canon(Board.board)
Canons2.place_canon(Board.board)
King=king()
King.place_king(Board.board)
# Board.print_board(King,Hut,Townhall)
LastTimeFired=timer()
start_time=-1
start_time2=-1
start_time3=-1
clicked_time=timer()
choice="King"
get=Get()
def print_board():
    os.system('clear')
    # print("queen",King.Queen_coord)
    # print("huts",Hut.coordinates)
    # print(timer()-clicked_time)
    print(Fore.CYAN+Style.BRIGHT+"LEVEL-{}".format(LEVEL)+Style.RESET_ALL,end="\n")
    if King.character=="King":
        print(Fore.CYAN+Style.BRIGHT+"King's health:"+Style.RESET_ALL)
        for K in range(King.health):
            print(Back.GREEN+' '+Style.RESET_ALL,end='')
        print(end='\n')
    if King.character=="Queen":
        print(Fore.CYAN+Style.BRIGHT+"Queen's health:")
        for K in range(King.health):
            print(Back.GREEN+' '+Style.RESET_ALL,end=''+Style.RESET_ALL)
        print(end='\n')
    num_rows=len(Board.board)
    num_colms=len(Board.board[0])
    for i in range(num_rows):
        for j in range(num_colms):
            tobeprinted=Board.board[i][j]
            if tobeprinted=='H':#get hit points of hut and if returned num is 1--> Green 2-->yellow 3-->red
                num=Hut.hitpoints_status(i,j) 
                if num==1:
                    print(Back.GREEN+tobeprinted+Style.RESET_ALL,end='')

                elif num==2:
                    print(Back.YELLOW+tobeprinted+Style.RESET_ALL,end='')
                    
                elif num==3:
                    print(Back.RED+tobeprinted+Style.RESET_ALL,end='')
                    
                
            elif tobeprinted=='T':
                x=Townhall.hit_pts
                actual=townhall_hitpts
                if x<=actual and x>=actual//2:
                    print(Back.GREEN+'T'+Style.RESET_ALL,end='')
                elif x<=actual//2 and x>=actual//5:
                    print(Back.YELLOW+'T'+Style.RESET_ALL,end='')
                elif x<=actual//2 and x>0:
                    print(Back.RED+'T'+Style.RESET_ALL,end='')

            elif tobeprinted=='X':
                print(Back.BLUE+'X'+Style.RESET_ALL,end='')
            elif tobeprinted=='1' or tobeprinted=='2' or tobeprinted=='3':
                print(Fore.CYAN+Style.BRIGHT+tobeprinted+Style.RESET_ALL,end='')

            else:
                print(Fore.CYAN+Board.board[i][j]+ Style.RESET_ALL,end='')
        print(end='\n')
# print_board()


def Canons_attack():
    present_time=timer()
    global LastTimeFired
    if(King.is_kingIn_canon(Canons1) and present_time-LastTimeFired>1):
        # print('yes king is in canon range')
        King.health-=Canons1.damage
        LastTimeFired=timer()
        return
    elif(King.is_kingIn_canon(Canons2) and present_time-LastTimeFired>1):
        # print('yes king is in canon range')
        King.health-=Canons2.damage
        LastTimeFired=timer()
        return
    if LEVEL>=2:
        if King.is_kingIn_canon(Canons3) and present_time-LastTimeFired>1:
            King.health-=Canons1.damage
            LastTimeFired=timer()
            return
        if LEVEL==3:
            if King.is_kingIn_canon(Canons4) and present_time-LastTimeFired>1:
                King.health-=Canons1.damage
                LastTimeFired=timer()
                return
    return


    
flag1=0

# Board.print_board()
def main_func():
    global start_time
    global start_time2
    global start_time3
    global clicked_time
    global Board
    global Hut
    global Townhall
    global Wall
    global bar_list
    global bal_list
    global arc_list
    global eagle_arrow
    global spawn_pts
    global spawn_pts_bal
    global spawn_pts_arc
    global LEVEL
    global King
    global canons_list
    global Canons3
    global Canons4
    global flag1
    global choice
    global LastTimeFired



    last_move=''
    while(True):
        
        if flag1==0:
            os.system('clear')
            print(Fore.CYAN+Style.BRIGHT+"For choosing king, press K\nFor choosing Queen, press Q\n"+Style.RESET_ALL,end='\n')
            choice=input()
            flag1=1
            if choice=='K':King.char("King")
            else: King.char("Queen")
            print_board()


        if(len(Hut.hit_pts)==0 and Townhall.hit_pts<=0 and len(canons_list)==0 ):
            os.system('clear')
            if LEVEL==3:
                print(Fore.CYAN+Style.BRIGHT+"ALL LEVELS ARE DONE"+Style.RESET_ALL,end='\n')
                exit(0)
            else:
                print(Fore.CYAN+Style.BRIGHT+"YOU'VE DESTROYED ALL BUILDINGS..!!you've reached next level"+Style.RESET_ALL,end='\n')
                LEVEL+=1
                
                Board=board(num_rows,num_colms)
                Hut=hut(hut_hit_points)
                Townhall=townhall(townhall_hitpts)
                Wall=wall(wall_hitpts)
                bar_list=[]
                bal_list=[]
                arc_list=[]
                # Barbarian=barbarian()
                eagle_arrow=False
                spawn_pts=[(5,50),(24,10),(44,50)]
                spawn_pts_bal=[(5,90),(5,10),(44,10)]
                spawn_pts_arc=[(24,90),(44,90),(44,75)]

                Board.board[4][50]='1'
                Board.board[25][10]='2'
                Board.board[45][50]='3'

                Board.board[4][90]='4'
                Board.board[4][10]='5'
                Board.board[45][10]='6'

                Board.board[24][90]='7'
                Board.board[45][90]='8'
                Board.board[45][75]='9'


                Townhall.build_townhall(Board.board)
                Wall.place_walls(Townhall.coordinates,Board.board)
                Hut.build_huts(Board.board)
                Canons1=canon(canon_hitpts)
                Canons2=canon(canon_hitpts)
                canons_list=[Canons1,Canons2]
                Canons1.place_canon(Board.board)
                Canons2.place_canon(Board.board)
                if(LEVEL>=2):
                    canons_list.append(Canons3)
                    Canons3.place_canon(Board.board)
                    if LEVEL==3:
                        canons_list.append(Canons4)
                        Canons4.place_canon(Board.board)
                
                King=king()
                King.place_king(Board.board)
                # Board.print_board(King,Hut,Townhall)
                LastTimeFired=timer()
                start_time=-1
                start_time2=-1
                start_time3=-1
                clicked_time=timer()
                if choice=='K':King.char("King")
                else: King.char("Queen")
                print_board()

                main_func()

        elif(King.health==0):
            os.system('clear')

            print(Fore.CYAN + Style.BRIGHT +
                "\t\t\t####    ####   ##   ##  ######           ####   ##  ##  ######  ######         " + Style.RESET_ALL)
            print(Fore.CYAN + Style.BRIGHT +
                "\t\t\t#      ##  ##  ### ###  ##              ##  ##  ##  ##  ##      ##  ##         " + Style.RESET_ALL)
            print(Fore.CYAN + Style.BRIGHT +
                "\t\t\t# ###  ######  ## # ##  ####            ##  ##  ##  ##  ####    #####          " + Style.RESET_ALL)
            print(Fore.CYAN + Style.BRIGHT +
                "\t\t\t#  ##  ##  ##  ##   ##  ##              ##  ##   ####   ##      ##  ##         " + Style.RESET_ALL)
            print(Fore.CYAN + Style.BRIGHT +
                "\t\t\t####   ##  ##  ##   ##  ######           ####     ##    ######  ##  ##         " + Style.RESET_ALL)
            exit(0)
        ch=input_to(get,0.07)
    
        
        if(ch=='W'):
            #move king up
            King.move_up(Board.board)
            Canons_attack()
            print_board()
            last_move='W'


        if(ch=='S'):
            #move king DOWN
            King.move_down(Board.board)
            Canons_attack()
            print_board()
            last_move='S'


        if(ch=='D'):
            #move king right
            King.move_right(Board.board)
            Canons_attack()
            print_board()
            last_move='D'


        if(ch=='A'):
            #move king right
            King.move_left(Board.board)
            Canons_attack()
            print_board()
            last_move='A'


        if ch=='1':
            if len(bar_list)<10:
                Barbarian=barbarian()
                bar_list.append(Barbarian)
                Barbarian.place_barbarian('1',Board.board)
                print_board()

        if ch=='2':
            if len(bar_list)<10:
                Barbarian=barbarian()
                bar_list.append(Barbarian)
                Barbarian.place_barbarian('2',Board.board)
                print_board()

        if ch=='3':
            if len(bar_list)<10:
                Barbarian=barbarian()
                bar_list.append(Barbarian)
                Barbarian.place_barbarian('3',Board.board)
                print_board()

        if ch=='4':
            if len(bal_list)<10:
                Balloon=balloon()
                bal_list.append(Balloon)
                Balloon.place_balloon('1',Board.board)
                print_board()

        if ch=='5':
            if len(bal_list)<10:
                Balloon=balloon()
                bal_list.append(Balloon)
                Balloon.place_balloon('2',Board.board)
                print_board()

        if ch=='6':
            if len(bal_list)<10:
                Balloon=balloon()
                bal_list.append(Balloon)
                Balloon.place_balloon('3',Board.board)
                print_board()

        if ch=='7':
            if len(arc_list)<10:
                Archer=archer()
                arc_list.append(Archer)
                Archer.place_archer('1',Board.board)
                print_board()

        if ch=='8':
            if len(arc_list)<10:
                Archer=archer()
                arc_list.append(Archer)
                Archer.place_archer('2',Board.board)
                print_board()

        if ch=='9':
            if len(arc_list)<10:
                Archer=archer()
                arc_list.append(Archer)
                Archer.place_archer('3',Board.board)
                print_board()

        # if ch=='Z':
        #     #attack
        #     eagle_arrow=True
        #     clicked_time=timer()
            
        
        if(ch==' '):
            #attack
            King.king_attack(Board.board,Hut,Townhall,canons_list,last_move,Wall)
            Canons_attack()
            print_board()
        elif ch=='Q':
            exit(0) 
        if timer()-start_time>0.5:
            for barb in bar_list:
                barb.move(barb.curr_coord,Hut,Board.board,Townhall,Wall)
                print_board()
            start_time=timer()
        if timer()-start_time2>0.25:
            for bal in bal_list:
                bal.move(bal.curr_coord,Hut,Board.board,Townhall,Wall,canons_list)
                print_board()
            start_time2=timer()
        if timer()-start_time3>0.25:
            for arc in arc_list:
                arc.move_a(Hut,Board.board,Townhall,Wall,canons_list)
                print_board()
            start_time3=timer()
        # if timer()-clicked_time>1 and eagle_arrow==True:
        #         # print(timer()-clicked_time)
        #         King.spcl_queen_attack(Board.board,Hut,Townhall,canons_list,last_move,Wall,King.Queen_coord)
        #         eagle_arrow=False
        #         # Canons_attack()
        #         print_board()
main_func()

        
   
