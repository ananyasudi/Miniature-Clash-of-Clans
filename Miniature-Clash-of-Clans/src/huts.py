import random
from src.constants import*
class building():
    def __init__(self,ht_pts):
        self.hit_pts=ht_pts
        self.coordinates=[]

class hut(building):
    def __init__(self, ht_pts):
        super().__init__(ht_pts)
        self.hit_pts=[hut_hit_points for i in range(5)]

    def build_huts(self,board):
        num_rows=len(board)
        num_colms=len(board[0])
        count=0
        while count<5:
            temp_r=random.randint(10,num_rows)
            temp_c=random.randint(10,num_colms)
            if(temp_r<num_rows and temp_c<num_colms and board[temp_r][temp_c]==' '):
                board[temp_r][temp_c]='H'
                self.coordinates.append([temp_r,temp_c])
                count+=1
    def get_index(self,x_c,y_c):
        for i in range(len(self.hit_pts)):
            if(x_c==self.coordinates[i][0] and y_c==self.coordinates[i][1]):
                return i
    def upd_huts(self,board):
        l=len(self.hit_pts)
        for i in range(l):
            # print(i)
            if(self.hit_pts[i]<=0):
                # print(i)
                # print('yes')
                #remove that index, coordinates and update board
                self.hit_pts.pop(i)
                board[self.coordinates[i][0]][self.coordinates[i][1]]=' '
                self.coordinates.pop(i)
                return
            l=len(self.hit_pts)
            # print('LEN OF HITPTS ARRAY:',l)
    def hitpoints_status(self,x_c,y_c):
        ind=self.get_index(x_c,y_c)
        if(self.hit_pts[ind]<=hut_hit_points and self.hit_pts[ind]>=hut_hit_points//2):
            return 1
        if(self.hit_pts[ind]<=hut_hit_points//2 and self.hit_pts[ind]>=hut_hit_points//5):
            return 2
        elif self.hit_pts[ind]>0:
            return 3

class townhall(building):
    def __init__(self, ht_pts):
        super().__init__(ht_pts)
        self.hit_pts=ht_pts
    def build_townhall(self,board):
        num_rows=len(board)
        num_colms=len(board[0])
        count=0
        while count<1:
            temp_r=random.randint(10,num_rows-10)
            temp_c=random.randint(10,num_colms-10)
            if temp_r+3 < num_rows-2 and temp_c+3<num_colms-2:
                if self.valid(board,temp_r,temp_c):
                    # we need to update board to be Townhall
                    for i in range(temp_r,temp_r+4):
                        for j in range(temp_c,temp_c+3):
                            board[i][j]='T'
                            self.coordinates.append([i,j])
                    count+=1
    def valid(self,board,temp_r,temp_c):
        for i in range(temp_r,temp_r+4):
            for j in range(temp_c,temp_c+3):
                if board[i][j]==' ':
                    continue
                else:
                    return False
        return True
    def upd_townhall(self,board):
        if(self.hit_pts<=0):
            for i in range(12):
                    board[self.coordinates[i][0]][self.coordinates[i][1]]=' '
            self.coordinates=[]

class wall(building):
    coordinates=[]
    def __init__(self, ht_pts):
        super().__init__(ht_pts)
        self.hit_pts=[ht_pts for i in range(18)]
        #coordinates 
    def place_walls(self,townhall,board):
        min_row=townhall[0][0]-1
        min_col=townhall[0][1]-1
        max_row=townhall[9][0]+1
        max_col=townhall[2][1]+1
        for i in range(min_col,max_col+1):
            self.coordinates.append([min_row,i])
        curr_row=townhall[0][0]
        for i in range(4):
            self.coordinates.append([curr_row,min_col])
            self.coordinates.append([curr_row,max_col])
            curr_row+=1
        for i in range(min_col,max_col+1):
            self.coordinates.append([max_row,i])
        for coordinate in self.coordinates:
            board[coordinate[0]][coordinate[1]]='#'
        
    def get_index(self,coord):
        for i in range(len(self.coordinates)):
            if self.coordinates[i][0]==coord[0] and self.coordinates[i][1]==coord[1]:
                print(i)
                return i
        print(i)
        return -1

    def upd_walls(self,board):
        l=len(self.hit_pts)
        for i in range(l):
            if(self.hit_pts[i]<=0):
                # print(i)
                # print('yes')
                #remove that index, coordinates and update board
                self.hit_pts.pop(i)
                board[self.coordinates[i][0]][self.coordinates[i][1]]=' '
                self.coordinates.pop(i)
                return
            l=len(self.hit_pts)
        # for i in range(len(self.coordinates)):
        #     if self.hit_pts[i]<=0:
        #         board[self.coordinates[i][0]][self.coordinates[i][1]]=' '
        #         self.coordinates.pop(i)
        #         self.hit_pts.pop(i)
                

class canon(building):
    def __init__(self, ht_pts):
        super().__init__(ht_pts)
        self.hit_pts=ht_pts
        self.damage=2
        
    def place_canon(self,board):
        count=0
        num_rows=len(board)
        num_colms=len(board[0])
        while count<1:
            temp_r=random.randint(10,num_rows)
            temp_c=random.randint(10,num_colms)
            if(temp_r<num_rows and temp_c<num_colms and board[temp_r][temp_c]==' '):
                board[temp_r][temp_c]='X'
                self.coordinates.append(temp_r)
                self.coordinates.append(temp_c)
                count+=1
        self.canon_rrange=[max(1,self.coordinates[0]-3),min(self.coordinates[0]+3,num_rows-2)]
        self.canon_crange=[max(1,self.coordinates[1]-3),min(self.coordinates[1]+3,num_colms-2)]
        print(self.canon_rrange)
        print(self.canon_crange)
    def upd_canon(self,board,canons_list):
        # if self.hit_pts<=0:
        #     l=len(canons_list)
        #     for i in range(l):
        #         if canons_list[i].coordinates[0]==self.coordinates[0] and canons_list[i].coordinates[1]==self.coordinates[1]:
        #             canons_list.pop(i)
        #         l=len(canons_list)
        #     board[self.coordinates[0]][self.coordinates[1]]=' '
        l=len(canons_list)
        for i in range(l):
            if canons_list[i].coordinates[0]==self.coordinates[0] and canons_list[i].coordinates[1]==self.coordinates[1] and self.hit_pts<=0:
                canons_list.pop(i)
                board[self.coordinates[0]][self.coordinates[1]]=' '
                return
            l=len(canons_list)
    # def get_index(self,coord):
    #     for i in range(len(self.coordinates)):
    #             if self.coordinates[i][0]==coord[0] and self.coordinates[i][1]==coord[1]:
    #                 print(i)
    #                 return i
    #     print(i)
    #     return -1

            

    
    