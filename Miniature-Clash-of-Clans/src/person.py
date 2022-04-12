import random
from src.constants import *
# def canons_ind(coord,canons_list):
#     for i in range(len(canons_list)):
#         if coord[0]==i.coordinates[0] and coord[1]==i.coordinates[1]:
#             return i
#     return -1

class person():
    def __init__(self):
        self.hit_pts=1
        self.damage=2
        self.health=30
    def gethealth(self):
        print(self.health)

class king(person):
    def __init__(self):
        super().__init__()
        self.damage=4
        self.damage_q=self.damage/2
        self.hit_pts_k=20
        self.hit_pts_q=10
        self.king_coord=[]
        self.Queen_coord=[]
        self.character="king"
    def char(self,ch):
        self.character=ch       
    def place_king(self,board):
        temp_r=random.randint(1,25)
        temp_c=random.randint(1,5)
        for i in range(temp_r,temp_r+2):
            for j in range(temp_c,temp_c+4):
                board[i][j]=k[i-temp_r][j-temp_c]
                self.king_coord.append([i,j])
        self.Queen_coord=[self.king_coord[0][0],self.king_coord[0][1]]
        print(len(board[0]))
        print(len(board))


    def move_up(self,board):
        if(self.king_coord[0][0]>1 and board[self.king_coord[0][0]-1][self.king_coord[0][1]]==' ' and board[self.king_coord[1][0]-1][self.king_coord[1][1]]==' ' 
        and board[self.king_coord[2][0]-1][self.king_coord[2][1]]==' ' and board[self.king_coord[3][0]-1][self.king_coord[3][1]]==' '): #check for all valid conditions
            for i in range(8):
                board[self.king_coord[i][0]-1][self.king_coord[i][1]]=board[self.king_coord[i][0]][self.king_coord[i][1]]

            board[self.king_coord[4][0]][self.king_coord[4][1]]=' '
            board[self.king_coord[5][0]][self.king_coord[5][1]]=' '
            board[self.king_coord[6][0]][self.king_coord[6][1]]=' '
            board[self.king_coord[7][0]][self.king_coord[7][1]]=' '

            for i in range(8):
                self.king_coord[i]=[self.king_coord[i][0]-1,self.king_coord[i][1]]
        self.Queen_coord=[self.king_coord[0][0],self.king_coord[0][1]]
            
    

    def move_down(self,board):
        if(self.king_coord[4][0]<len(board)-2 and board[self.king_coord[4][0]+1][self.king_coord[4][1]]==' ' and board[self.king_coord[5][0]+1][self.king_coord[5][1]]==' ' 
        and board[self.king_coord[6][0]+1][self.king_coord[6][1]]==' ' and board[self.king_coord[7][0]+1][self.king_coord[7][1]]==' '): #check for other conditions
            i=7
            while(i>=0):
                board[self.king_coord[i][0]+1][self.king_coord[i][1]]=board[self.king_coord[i][0]][self.king_coord[i][1]]
                i-=1

            board[self.king_coord[0][0]][self.king_coord[0][1]]=' '
            board[self.king_coord[1][0]][self.king_coord[1][1]]=' '
            board[self.king_coord[2][0]][self.king_coord[2][1]]=' '
            board[self.king_coord[3][0]][self.king_coord[3][1]]=' '

            for i in range(8):
                self.king_coord[i]=[self.king_coord[i][0]+1,self.king_coord[i][1]]
        self.Queen_coord=[self.king_coord[0][0],self.king_coord[0][1]]
        
    
    def move_right(self,board):
        if(self.king_coord[3][1]+1<len(board[0]) and board[self.king_coord[3][0]][self.king_coord[3][1]+1]==' ' and board[self.king_coord[7][0]][self.king_coord[7][1]+1]==' '):
            board[self.king_coord[3][0]][self.king_coord[3][1]+1]=board[self.king_coord[3][0]][self.king_coord[3][1]]
            board[self.king_coord[7][0]][self.king_coord[7][1]+1]=board[self.king_coord[7][0]][self.king_coord[7][1]]
            board[self.king_coord[2][0]][self.king_coord[2][1]+1]=board[self.king_coord[2][0]][self.king_coord[2][1]]
            board[self.king_coord[6][0]][self.king_coord[6][1]+1]=board[self.king_coord[6][0]][self.king_coord[6][1]]
            board[self.king_coord[1][0]][self.king_coord[1][1]+1]=board[self.king_coord[1][0]][self.king_coord[1][1]]
            board[self.king_coord[5][0]][self.king_coord[5][1]+1]=board[self.king_coord[5][0]][self.king_coord[5][1]]
            board[self.king_coord[0][0]][self.king_coord[0][1]+1]=board[self.king_coord[0][0]][self.king_coord[0][1]]
            board[self.king_coord[4][0]][self.king_coord[4][1]+1]=board[self.king_coord[4][0]][self.king_coord[4][1]]

            board[self.king_coord[0][0]][self.king_coord[0][1]]=' '
            board[self.king_coord[4][0]][self.king_coord[4][1]]=' '
            for i in range(8):
                self.king_coord[i]=[self.king_coord[i][0],self.king_coord[i][1]+1]
        self.Queen_coord=[self.king_coord[0][0],self.king_coord[0][1]]
        

    def move_left(self,board):
        if(self.king_coord[3][1]-1>1 and board[self.king_coord[0][0]][self.king_coord[0][1]-1]==' ' and board[self.king_coord[4][0]][self.king_coord[4][1]-1]==' '):
            board[self.king_coord[0][0]][self.king_coord[0][1]-1]=board[self.king_coord[0][0]][self.king_coord[0][1]]
            board[self.king_coord[4][0]][self.king_coord[4][1]-1]=board[self.king_coord[4][0]][self.king_coord[4][1]]
            board[self.king_coord[1][0]][self.king_coord[1][1]-1]=board[self.king_coord[1][0]][self.king_coord[1][1]]
            board[self.king_coord[5][0]][self.king_coord[5][1]-1]=board[self.king_coord[5][0]][self.king_coord[5][1]]
            board[self.king_coord[2][0]][self.king_coord[2][1]-1]=board[self.king_coord[2][0]][self.king_coord[2][1]]
            board[self.king_coord[6][0]][self.king_coord[6][1]-1]=board[self.king_coord[6][0]][self.king_coord[6][1]]
            board[self.king_coord[3][0]][self.king_coord[3][1]-1]=board[self.king_coord[3][0]][self.king_coord[3][1]]
            board[self.king_coord[7][0]][self.king_coord[7][1]-1]=board[self.king_coord[7][0]][self.king_coord[7][1]]
            
           

            board[self.king_coord[3][0]][self.king_coord[3][1]]=' '
            board[self.king_coord[7][0]][self.king_coord[7][1]]=' '
            for i in range(8):
                self.king_coord[i]=[self.king_coord[i][0],self.king_coord[i][1]-1]
        self.Queen_coord=[self.king_coord[0][0],self.king_coord[0][1]]
        
    def king_attack(self,board,huts,townhall,canons_list,last_move,wall):
        if self.character=="King":
            if(self.is_townhall_near(board)):
                self.attack_townhall(board,townhall)

            #check if WALL is right or left side
            if(board[self.king_coord[3][0]][self.king_coord[3][1]+1]=='#'):
                wall_ind=wall.get_index([self.king_coord[3][0],self.king_coord[3][1]+1])
                wall.hit_pts[wall_ind]-=self.damage
                wall.upd_walls(board)
                return

            elif(board[self.king_coord[7][0]][self.king_coord[3][1]+1]=='#'):
                wall_ind=wall.get_index([self.king_coord[7][0],self.king_coord[7][1]+1])
                wall.hit_pts[wall_ind]-=self.damage
                wall.upd_walls(board)
                return
            elif(board[self.king_coord[0][0]][self.king_coord[0][1]-1]=='#'):
                wall_ind=wall.get_index([self.king_coord[0][0],self.king_coord[0][1]-1])
                wall.hit_pts[wall_ind]-=self.damage
                wall.upd_walls(board)
                return
            elif(board[self.king_coord[4][0]][self.king_coord[4][1]-1]=='#'):
                wall_ind=wall.get_index([self.king_coord[4][0],self.king_coord[4][1]-1])
                wall.hit_pts[wall_ind]-=self.damage
                wall.upd_walls(board)
                return

            if(board[self.king_coord[1][0]-1][self.king_coord[1][1]]=='#'):
                wall_ind=wall.get_index([self.king_coord[1][0]-1,self.king_coord[1][1]])
                wall.hit_pts[wall_ind]-=self.damage
                wall.upd_walls(board)
                return
            elif(board[self.king_coord[2][0]-1][self.king_coord[2][1]]=='#'):
                wall_ind=wall.get_index([self.king_coord[2][0]-1,self.king_coord[2][1]])
                wall.hit_pts[wall_ind]-=self.damage
                wall.upd_walls(board)
                return
            elif(board[self.king_coord[5][0]+1][self.king_coord[5][1]]=='#'):
                wall_ind=wall.get_index([self.king_coord[5][0]+1,self.king_coord[5][1]])
                wall.hit_pts[wall_ind]-=self.damage
                wall.upd_walls(board)
                return
            elif(board[self.king_coord[6][0]+1][self.king_coord[6][1]]=='#'):
                wall_ind=wall.get_index([self.king_coord[6][0]+1,self.king_coord[6][1]])
                wall.hit_pts[wall_ind]-=self.damage
                wall.upd_walls(board)
                return
            
            #check if hut is right or left side
            if(board[self.king_coord[3][0]][self.king_coord[3][1]+1]=='H'):
                hut_ind=huts.get_index(self.king_coord[3][0],self.king_coord[3][1]+1)
                huts.hit_pts[hut_ind]-=self.damage
                huts.upd_huts(board)
                return

            elif(board[self.king_coord[7][0]][self.king_coord[3][1]+1]=='H'):
                hut_ind=huts.get_index(self.king_coord[7][0],self.king_coord[7][1]+1)
                huts.hit_pts[hut_ind]-=self.damage
                huts.upd_huts(board)
                return
            elif(board[self.king_coord[0][0]][self.king_coord[0][1]-1]=='H'):
                hut_ind=huts.get_index(self.king_coord[0][0],self.king_coord[0][1]-1)
                huts.hit_pts[hut_ind]-=self.damage
                huts.upd_huts(board)
                return
            elif(board[self.king_coord[4][0]][self.king_coord[4][1]-1]=='H'):
                hut_ind=huts.get_index(self.king_coord[4][0],self.king_coord[4][1]-1)
                huts.hit_pts[hut_ind]-=self.damage
                huts.upd_huts(board)
                return

            if(board[self.king_coord[1][0]-1][self.king_coord[1][1]]=='H'):
                hut_ind=huts.get_index(self.king_coord[1][0]-1,self.king_coord[1][1])
                huts.hit_pts[hut_ind]-=self.damage
                huts.upd_huts(board)
                return
            elif(board[self.king_coord[2][0]-1][self.king_coord[2][1]]=='H'):
                hut_ind=huts.get_index(self.king_coord[2][0]-1,self.king_coord[2][1])
                huts.hit_pts[hut_ind]-=self.damage
                huts.upd_huts(board)
                return
            elif(board[self.king_coord[5][0]+1][self.king_coord[5][1]]=='H'):
                hut_ind=huts.get_index(self.king_coord[5][0]+1,self.king_coord[5][1])
                huts.hit_pts[hut_ind]-=self.damage
                huts.upd_huts(board)
                return
            elif(board[self.king_coord[6][0]+1][self.king_coord[6][1]]=='H'):
                hut_ind=huts.get_index(self.king_coord[6][0]+1,self.king_coord[6][1])
                huts.hit_pts[hut_ind]-=self.damage
                huts.upd_huts(board)
                return
            # #check if canon is right or left side
            # if(board[self.king_coord[3][0]][self.king_coord[3][1]+1]=='X'):
            #     canons_ind=canons_ind([self.king_coord[3][0],self.king_coord[3][1]+1],canons_list)
            #     huts.hit_pts[canons_ind]-=self.damage
            #     huts.upd_huts(board)
            #     return

            # elif(board[self.king_coord[7][0]][self.king_coord[3][1]+1]=='X'):
            #     canons_ind=canons_ind([self.king_coord[7][0],self.king_coord[7][1]+1],canons_list)
            #     huts.hit_pts[canons_ind]-=self.damage
            #     huts.upd_huts(board)
            #     return
            # elif(board[self.king_coord[0][0]][self.king_coord[0][1]-1]=='X'):
            #     canons_ind=canons_ind([self.king_coord[0][0],self.king_coord[0][1]-1],canons_list)
            #     huts.hit_pts[canons_ind]-=self.damage
            #     huts.upd_huts(board)
            #     return
            # elif(board[self.king_coord[4][0]][self.king_coord[4][1]-1]=='X'):
            #     canons_ind=canons_ind([self.king_coord[4][0],self.king_coord[4][1]-1],canons_list)
            #     huts.hit_pts[canons_ind]-=self.damage
            #     huts.upd_huts(board)
            #     return

            # if(board[self.king_coord[1][0]-1][self.king_coord[1][1]]=='X'):
            #     canons_ind=canons_ind([self.king_coord[1][0]-1,self.king_coord[1][1]],canons_list)
            #     huts.hit_pts[canons_ind]-=self.damage
            #     huts.upd_huts(board)
            #     return
            # elif(board[self.king_coord[2][0]-1][self.king_coord[2][1]]=='X'):
            #     canons_ind=canons_ind([self.king_coord[2][0]-1,self.king_coord[2][1]],canons_list)
            #     huts.hit_pts[canons_ind]-=self.damage
            #     huts.upd_huts(board)
            #     return
            # elif(board[self.king_coord[5][0]+1][self.king_coord[5][1]]=='X'):
            #     canons_ind=canons_ind([self.king_coord[5][0]+1,self.king_coord[5][1]],canons_list)
            #     huts.hit_pts[canons_ind]-=self.damage
            #     huts.upd_huts(board)
            #     return
            # elif(board[self.king_coord[6][0]+1][self.king_coord[6][1]]=='X'):
            #     canons_ind=canons_ind([self.king_coord[6][0]+1,self.king_coord[6][1]],canons_list)
            #     huts.hit_pts[canons_ind]-=self.damage
            #     huts.upd_huts(board)
            #     return
        elif self.character=="Queen":
            centre_coord=[]
            row_range=[]
            col_range=[]
            if last_move=='W':
                if self.Queen_coord[0]-8>1:
                    centre_coord.append(self.Queen_coord[0]-8)
                    centre_coord.append(self.Queen_coord[1])
                    col_range.append(max(1,centre_coord[1]-2))
                    col_range.append(min(num_colms-2,centre_coord[1]+2))
                    row_range.append(max(1,centre_coord[0]-2))
                    row_range.append(min(num_rows-2,centre_coord[0]+2))
            elif last_move=='A':
                if self.Queen_coord[1]-8>1:
                    centre_coord.append(self.Queen_coord[0])
                    centre_coord.append(self.Queen_coord[1]-8)
                    col_range.append(max(1,centre_coord[1]-2))
                    col_range.append(centre_coord[1]+2)
                    row_range.append(max(1,centre_coord[0]-2))
                    row_range.append(min(num_rows-2,centre_coord[0]+2))
            elif last_move=='D':
                if self.Queen_coord[1]+8<num_colms-1:
                    centre_coord.append(self.Queen_coord[0])
                    centre_coord.append(self.Queen_coord[1]+8)
                    col_range.append(max(1,centre_coord[1]-2))
                    col_range.append(min(num_colms,centre_coord[1]+2))
                    row_range.append(max(1,centre_coord[0]-2))
                    row_range.append(min(num_rows-2,centre_coord[0]+2))
            elif last_move=='S':
                if self.Queen_coord[0]+8<num_rows-1:
                    centre_coord.append(self.Queen_coord[0]+8)
                    centre_coord.append(self.Queen_coord[1])
                    col_range.append(max(1,centre_coord[1]-2))
                    col_range.append(min(num_colms,centre_coord[1]+2))
                    row_range.append(max(1,centre_coord[0]-2))
                    row_range.append(min(num_rows-2,centre_coord[0]+2))
            print(last_move)
            print(row_range)
            print(col_range)
            print(self.Queen_coord)

            for i in range(row_range[0],row_range[1]):
                for j in range(col_range[0],col_range[1]):
                    if board[i][j]=='H':
                        #attack hut
                        # print('hut attacked')
                        hut_ind=huts.get_index(i,j)
                        huts.hit_pts[hut_ind]-=self.damage_q
                        huts.upd_huts(board)
                    elif board[i][j]=='X':
                        #attack canon
                        for k in canons_list:
                            if k.coordinates[0]==i and k.coordinates[1]==j:
                                print('canon attacked')
                                k.hit_pts-=self.damage
                                k.upd_canon(board,canons_list)
                    elif board[i][j]=='#':
                        wall_ind=wall.get_index([i,j])
                        wall.hit_pts[wall_ind]-=self.damage
                        wall.upd_walls(board)

                        # if canons_list[0].coordinates[0]==i and canons_list[0].coordinates[1]==j:
                        #     print('canon attacked')
                        #     canons_list[0].hit_pts-=self.damage
                        #     canons_list[0].upd_canon(board)
                        # elif canons_list[1].coordinates[0]==i and canons_list[1].coordinates[1]==j:
                        #     canons_list[1].hit_pts-=self.damage
                        #     print('canon attacked')
                        #     canons_list[1].upd_canon(board)
                        pass
                    elif board[i][j]=='T':
                        #townhall
                        townhall.hit_pts-=self.damage_q
                        townhall.upd_townhall(board)
                        pass

            return

        # if(board[self.king_coord[3][0]][self.king_coord[3][1]]=='H' or board[self.king_coord[7][0]][self.king_coord[7][1]]=='H' or
        # board[self.king_coord[0][0]-1][self.king_coord[0][1]]=='H' or board[self.king_coord[4][0]-1][self.king_coord[4][1]]=='H')
    def spcl_queen_attack(self,board,huts,townhall,canons_list,last_move,wall,actual_coord):
        if self.character=="Queen":
            centre_coord=[]
            row_range=[]
            col_range=[]
            if last_move=='W':
                if actual_coord[0]-16>1:
                    centre_coord.append(actual_coord[0]-16)
                    centre_coord.append(actual_coord[1])
                    col_range.append(max(1,centre_coord[1]-4))
                    col_range.append(min(num_colms-2,centre_coord[1]+4))
                    row_range.append(max(1,centre_coord[0]-4))
                    row_range.append(min(num_rows-2,centre_coord[0]+4))
            elif last_move=='A':
                if actual_coord[1]-16>1:
                    centre_coord.append(actual_coord[0])
                    centre_coord.append(actual_coord[1]-16)
                    col_range.append(max(1,centre_coord[1]-4))
                    col_range.append(centre_coord[1]+4)
                    row_range.append(max(1,centre_coord[0]-4))
                    row_range.append(min(num_rows-2,centre_coord[0]+4))
            elif last_move=='D':
                if actual_coord[1]+16<num_colms-1:
                    centre_coord.append(actual_coord[0])
                    centre_coord.append(actual_coord[1]+16)
                    col_range.append(max(1,centre_coord[1]-4))
                    col_range.append(min(num_colms,centre_coord[1]+4))
                    row_range.append(max(1,centre_coord[0]-4))
                    row_range.append(min(num_rows-2,centre_coord[0]+4))
            elif last_move=='S':
                if actual_coord[0]+8<num_rows-1:
                    centre_coord.append(actual_coord[0]+16)
                    centre_coord.append(actual_coord[1])
                    col_range.append(max(1,centre_coord[1]-4))
                    col_range.append(min(num_colms,centre_coord[1]+4))
                    row_range.append(max(1,centre_coord[0]-4))
                    row_range.append(min(num_rows-2,centre_coord[0]+4))
            # print(last_move)
            # print(row_range)
            # print(col_range)
            # print(actual_coord)
            # print("actual",actual_coord)
            # print("centre",centre_coord)
            # print("row range",row_range)
            # print("col range",col_range)  
            # print("hut",huts.coordinates)    
            for i in range(row_range[0],row_range[1]):
                for j in range(col_range[0],col_range[1]):
                    print(i,j)
                    if board[i][j]=='H':

                        #attack hut
                        print('hut attacked')
                        hut_ind=huts.get_index(i,j)
                        huts.hit_pts[hut_ind]-=self.damage_q
                        print(huts.hit_pts[hut_ind])
                        huts.upd_huts(board)
                    elif board[i][j]=='X':
                        #attack canon
                        for k in canons_list:
                            if k.coordinates[0]==i and k.coordinates[1]==j:
                                print('canon attacked')
                                k.hit_pts-=self.damage
                                print(k.hit_pts)
                                k.upd_canon(board,canons_list)
                    elif board[i][j]=='#':
                        wall_ind=wall.get_index([i,j])
                        wall.hit_pts[wall_ind]-=self.damage
                        print(wall.hit_pts[wall_ind])

                        wall.upd_walls(board)

                        # if canons_list[0].coordinates[0]==i and canons_list[0].coordinates[1]==j:
                        #     print('canon attacked')
                        #     canons_list[0].hit_pts-=self.damage
                        #     canons_list[0].upd_canon(board)
                        # elif canons_list[1].coordinates[0]==i and canons_list[1].coordinates[1]==j:
                        #     canons_list[1].hit_pts-=self.damage
                        #     print('canon attacked')
                        #     canons_list[1].upd_canon(board)
                        pass
                    elif board[i][j]=='T':
                        #townhall
                        townhall.hit_pts-=self.damage_q
                        print(townhall.hit_pts)
                        townhall.upd_townhall(board)
                


    def is_townhall_near(self,board):
        if(board[self.king_coord[3][0]][self.king_coord[3][1]+1]=='T' or board[self.king_coord[7][0]][self.king_coord[3][1]+1]=='T' or 
        board[self.king_coord[0][0]][self.king_coord[0][1]-1]=='T' or board[self.king_coord[4][0]][self.king_coord[4][1]-1]=='T' or 
        board[self.king_coord[1][0]-1][self.king_coord[1][1]]=='T' or board[self.king_coord[2][0]-1][self.king_coord[2][1]]=='T' or 
        board[self.king_coord[5][0]+1][self.king_coord[5][1]]=='T' or board[self.king_coord[6][0]+1][self.king_coord[6][1]]=='H'):
            return True

    def attack_townhall(self,board,townhall):
        if(board[self.king_coord[3][0]][self.king_coord[3][1]+1]=='T'):
            townhall.hit_pts-=self.damage
            townhall.upd_townhall(board)
        elif(board[self.king_coord[7][0]][self.king_coord[3][1]+1]=='T'):
            townhall.hit_pts-=self.damage
            townhall.upd_townhall(board)
        elif(board[self.king_coord[0][0]][self.king_coord[0][1]-1]=='T'):
            townhall.hit_pts-=self.damage
            townhall.upd_townhall(board)
        elif(board[self.king_coord[4][0]][self.king_coord[4][1]-1]=='T'):
            townhall.hit_pts-=self.damage
            townhall.upd_townhall(board)

        if(board[self.king_coord[1][0]-1][self.king_coord[1][1]]=='T'):
            townhall.hit_pts-=self.damage
            townhall.upd_townhall(board)
        elif(board[self.king_coord[2][0]-1][self.king_coord[2][1]]=='T'):
            townhall.hit_pts-=self.damage
            townhall.upd_townhall(board)
        elif(board[self.king_coord[5][0]+1][self.king_coord[5][1]]=='T'):
            townhall.hit_pts-=self.damage
            townhall.upd_townhall(board)
        elif(board[self.king_coord[6][0]+1][self.king_coord[6][1]]=='H'):
            townhall.hit_pts-=self.damage
            townhall.upd_townhall(board)
    
    def is_kingIn_canon(self,canon):
        for i in range(len(self.king_coord)):
            if(self.king_coord[i][0]>canon.canon_rrange[0] and self.king_coord[i][0]<canon.canon_rrange[1]):
                if(self.king_coord[i][1]>canon.canon_crange[0] and self.king_coord[i][1]<canon.canon_crange[1]):
                    return True
                
            # else:
            #     return False
        return False







        







# class barbarian(person):
#     def __init__(self):
#         super().__init__()
#         self.damage=1
#         self.hit_pts=5


# class person():
#     def __init__(self):
#         self.hit_pts=5
#         self.health=100
#         self.damage=10 #amount of damage it will yield per attack
#     def set_coordinates(self,x_c,y_c):
#         self.x_c=x_c
#         self.y_c=y_c
# class king(person):
#     def __init__(self, hit_pts):
#         super().__init__(hit_pts)
#         self.damage=10
#         self.health=100
#     def place_king(self,board):
#         count=0
#         temp_r=random.randint(1,25)
#         temp_c=random.randint(1,5)
#         for i in range(temp_r,temp_r+2):
#             for j in range(temp_c,temp_c+4):
#                 self.board[i][j]=k[i-temp_r][j-temp_c]