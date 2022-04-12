from src.constants import *
spawn_pts=[(5,50),(24,10),(44,50)]
spawn_pts_bal=[(5,90),(5,10),(44,10)]
spawn_pts_arc=[(24,90),(44,90),(44,75)]


def is_near_hut(coord_b,huts):
        x=coord_b[0]
        y=coord_b[1]
        for i in range(len(huts)):
            if x==huts[i][0] and y-1==huts[i][1]:
                return (True,i)
            elif x==huts[i][0] and y+1==huts[i][1]:
                return (True,i)
            elif x==huts[i][0] and y+1==huts[i][1]:
                return (True,i)
            elif x==huts[i][0] and y-1==huts[i][1]:
                return (True,i)
        return (False,0)
def is_on_hut(coord_bal,huts):
        x=coord_bal[0]
        y=coord_bal[1]
        for i in range(len(huts)):
            if x==huts[i][0] and y==huts[i][1]:
                return (True,i)
        return (False,0)
def is_near_townhall(coord_b,townhall):
    x=coord_b[0]
    y=coord_b[1]
    for i in range(len(townhall)):
        if x==townhall[i][0] and y-1==townhall[i][1]:
            return (True,i)
        elif x==townhall[i][0] and y+1==townhall[i][1]:
            return (True,i)
        elif x==townhall[i][0] and y+1==townhall[i][1]:
            return (True,i)
        elif x==townhall[i][0] and y-1==townhall[i][1]:
            return (True,i)
    return (False,0)

def is_on_townhall(coord_bal,townhall):
    x=coord_bal[0]
    y=coord_bal[1]
    for i in range(len(townhall)):
        if x==townhall[i][0] and y==townhall[i][1]:
            return (True,i)
    return (False,0)

def is_near_wall(coord_b,wall):
    x=coord_b[0]
    y=coord_b[1]
    for i in range(len(wall)):
        if x==wall[i][0] and y-1==wall[i][1]:
            return (True,i)
        elif x==wall[i][0] and y+1==wall[i][1]:
            return (True,i)
        elif x==wall[i][0] and y+1==wall[i][1]:
            return (True,i)
        elif x==wall[i][0] and y-1==wall[i][1]:
            return (True,i)
    return (False,0)
def is_on_canon(coord_b,canons_list):
    x=coord_b[0]
    y=coord_b[1]
    for i in range(len(canons_list)):
        x1=canons_list[i].coordinates[0]
        y1=canons_list[i].coordinates[1]
        if x==x1 and y==y1:
            return (True,i)
    return (False,-1)


class barbarian():
    initial_coor=()
    curr_coord=()
    # health=[]
    def __init__(self):
        self.damage=5
    def place_barbarian(self,ch,board):
        if ch=='1':
            self.initial_coor=(spawn_pts[0][0],spawn_pts[0][1])
            board[spawn_pts[0][0]][spawn_pts[0][1]]='O'
            self.curr_coord=(spawn_pts[0][0],spawn_pts[0][1])
        elif ch=='2':
            self.initial_coor=(spawn_pts[1][0],spawn_pts[1][1])
            board[spawn_pts[1][0]][spawn_pts[1][1]]='O'
            self.curr_coord=(spawn_pts[1][0],spawn_pts[1][1])
        elif ch=='3':
            self.initial_coor=(spawn_pts[2][0],spawn_pts[2][1])
            board[spawn_pts[2][0]][spawn_pts[2][1]]='O'
            self.curr_coord=(spawn_pts[2][0],spawn_pts[2][1])
    
            

    def move(self,coord_b,huts,board,townhall,wall):
        tup=is_near_hut(coord_b,huts.coordinates)
        if tup[0]==True:
            #attack hut
            huts.hit_pts[tup[1]]-=self.damage
            huts.upd_huts(board)
            return
        tup1=is_near_townhall(coord_b,townhall.coordinates)
        tup2=is_near_wall(coord_b,wall.coordinates)
        if tup1[0]==True:
            #attack townhall
            townhall.hit_pts-=self.damage
            townhall.upd_townhall(board)
            return
        if tup2[0]==True:
            #attack walls
            print('wall attack')
            wall.hit_pts[tup2[1]]-=self.damage
            wall.upd_walls(board)
            return
        adj_coord=[]
        c_x=coord_b[0]
        c_y=coord_b[1]
        board[c_x][c_y]=' '
        min_len=10000
        new_coord=(c_x,c_y)
        if c_x+1<num_rows-1: adj_coord.append([c_x+1,c_y])
        if c_y+1<num_colms-1: adj_coord.append([c_x,c_y+1])
        if c_x>1: adj_coord.append([c_x-1,c_y])
        if c_y>1: adj_coord.append([c_x,c_y-1])
        if len(huts.coordinates)>0:
            print('agj hut')
            for adj_coordinate in adj_coord:
                c_x=adj_coordinate[0]
                c_y=adj_coordinate[1]
                for i in huts.coordinates:
                    if board[c_x][c_y]==' ':
                        dist=((c_x-i[0])**2+(c_y-i[1])**2)**1/2
                        if  dist < min_len:
                            min_len=dist
                            hut_coor=i
                            new_coord=(c_x,c_y)
        elif len(townhall.coordinates)>0:
            #attack townhall
            min_len=10000
            t_x=townhall.coordinates[0][0]
            t_y=townhall.coordinates[0][1]
            for adj_coordinate in adj_coord:
                c_x=adj_coordinate[0]
                c_y=adj_coordinate[1]
                if board[c_x][c_y]==' ':
                    dist=((c_x-t_x)**2+(c_y-t_y)**2)**1/2
                    if  dist < min_len:
                        min_len=dist
                        new_coord=(c_x,c_y)
        elif len(wall.coordinates)>0:
            #attack WALL
            print('adj wall')
            for adj_coordinate in adj_coord:
                c_x=adj_coordinate[0]
                c_y=adj_coordinate[1]
                for i in wall.coordinates:
                    if board[c_x][c_y]==' ':
                        dist=((c_x-i[0])**2+(c_y-i[1])**2)**1/2
                        if  dist < min_len:
                            min_len=dist
                            new_coord=(c_x,c_y)

        self.curr_coord=(new_coord[0],new_coord[1])
        board[new_coord[0]][new_coord[1]]='O'
        
class balloon(barbarian):
    def __init__(self):
        super().__init__()
        self.damage=3
        self.health=balloon_health
    def place_balloon(self,ch,board):
        if ch=='1':
            self.initial_coor=(spawn_pts_bal[0][0],spawn_pts_bal[0][1])
            board[spawn_pts_bal[0][0]][spawn_pts_bal[0][1]]='B'
            self.curr_coord=(spawn_pts_bal[0][0],spawn_pts_bal[0][1])
        elif ch=='2':
            self.initial_coor=(spawn_pts_bal[1][0],spawn_pts_bal[1][1])
            board[spawn_pts_bal[1][0]][spawn_pts_bal[1][1]]='B'
            self.curr_coord=(spawn_pts_bal[1][0],spawn_pts_bal[1][1])
        elif ch=='3':
            self.initial_coor=(spawn_pts_bal[2][0],spawn_pts_bal[2][1])
            board[spawn_pts_bal[2][0]][spawn_pts_bal[2][1]]='B'
            self.curr_coord=(spawn_pts_bal[2][0],spawn_pts_bal[2][1])

    def move(self,coord_bal,huts,board,townhall,wall,canons_list):
        tup=is_on_hut(coord_bal,huts.coordinates)
        tup3=is_on_canon(coord_bal,canons_list)
        if tup3[0]==True:
            #attack canon
            canons_list[tup3[1]].hit_pts-=self.damage
            canons_list[tup3[1]].upd_canon(board,canons_list)
            return
        if tup[0]==True:
            #attack hut
            huts.hit_pts[tup[1]]-=self.damage
            huts.upd_huts(board)
            return
        tup1=is_on_townhall(coord_bal,townhall.coordinates)
        # tup2=is_on_wall(coord_bal,wall.coordinates)
        if tup1[0]==True:
            #attack townhall
            townhall.hit_pts-=self.damage
            townhall.upd_townhall(board)
            return
        # if tup2[0]==True:
        #     #attack walls
        #     print('wall attack')
        #     wall.hit_pts[tup2[1]]-=self.damage
        #     wall.upd_walls(board)
        #     return
        adj_coord=[]
        c_x=coord_bal[0]
        c_y=coord_bal[1]
        for coordinate in wall.coordinates:
            if c_x==coordinate[0] and c_y==coordinate[1]:
                board[c_x][c_y]='#'
                break
            board[c_x][c_y]=' '
        min_len=10000
        new_coord=(c_x,c_y)
        if c_x+1<num_rows-1: adj_coord.append([c_x+1,c_y])
        if c_y+1<num_colms-1: adj_coord.append([c_x,c_y+1])
        if c_x>1: adj_coord.append([c_x-1,c_y])
        if c_y>1: adj_coord.append([c_x,c_y-1])
        if len(canons_list)>0:
            #attack CANON
            for adj_coordinate in adj_coord:
                c_x=adj_coordinate[0]
                c_y=adj_coordinate[1]
                for i in canons_list:
                    # if board[c_x][c_y]==' ':
                        dist=((c_x-i.coordinates[0])**2+(c_y-i.coordinates[1])**2)**1/2
                        if  dist < min_len:
                            min_len=dist
                            new_coord=(c_x,c_y)
        elif len(huts.coordinates)>0:
            for adj_coordinate in adj_coord:
                c_x=adj_coordinate[0]
                c_y=adj_coordinate[1]
                for i in huts.coordinates:
                    # if board[c_x][c_y]==' ':
                        dist=((c_x-i[0])**2+(c_y-i[1])**2)**1/2
                        if  dist < min_len:
                            min_len=dist
                            new_coord=(c_x,c_y)
        elif len(townhall.coordinates)>0:
            #attack townhall
            min_len=10000
            t_x=townhall.coordinates[0][0]
            t_y=townhall.coordinates[0][1]
            for adj_coordinate in adj_coord:
                c_x=adj_coordinate[0]
                c_y=adj_coordinate[1]
                # if board[c_x][c_y]==' ':
                dist=((c_x-t_x)**2+(c_y-t_y)**2)**1/2
                if  dist < min_len:
                    min_len=dist
                    new_coord=(c_x,c_y)
        

        self.curr_coord=(new_coord[0],new_coord[1])
        board[new_coord[0]][new_coord[1]]='B'
    # def upd_balloon(self,board,bal_list):
    #     if self.health<=0:
    #         l=
    #         for i in range(len(bal_list)):

class archer():
    initial_coord=()
    curr_coord=()
    archer_rrange=[]
    archer_crange=[]
    def __init__(self):
        super().__init__()
        self.damage=2
    def place_archer(self,ch,board):
        if ch=='1':
            self.initial_coor=(spawn_pts_arc[0][0],spawn_pts_arc[0][1])
            board[spawn_pts_arc[0][0]][spawn_pts_arc[0][1]]='A'
            self.curr_coord=(spawn_pts_arc[0][0],spawn_pts_arc[0][1])
        elif ch=='2':
            self.initial_coor=(spawn_pts_arc[1][0],spawn_pts_arc[1][1])
            board[spawn_pts_arc[1][0]][spawn_pts_arc[1][1]]='A'
            self.curr_coord=(spawn_pts_arc[1][0],spawn_pts_arc[1][1])
        elif ch=='3':
            self.initial_coor=(spawn_pts_arc[2][0],spawn_pts_arc[2][1])
            board[spawn_pts_arc[2][0]][spawn_pts_arc[2][1]]='A'
            self.curr_coord=(spawn_pts_arc[2][0],spawn_pts_arc[2][1])
    
    def move_a(self,huts,board,townhall,wall,canons_list):
        self.archer_rrange=[max(1,self.curr_coord[0]-3),min(self.curr_coord[0]+3,num_rows-2)]
        self.archer_crange=[max(1,self.curr_coord[1]-3),min(self.curr_coord[1]+3,num_colms-2)]
        # for i in huts.coordinates:
        #     if i[0]>self.archer_rrange[0] and i[0]<self.archer_rrange[1]:
        #         if i[1]>self.archer_crange[0] and i[1]<self.archer_crange[1]:
        #             #attack hut
        #             hut_ind=huts.get_index(i[0],i[1])
        #             huts.hit_pts[hut_ind]-=self.damage
        #             huts.upd_huts(board)
        # for i in townhall.coordinates:
        #     if i[0]>self.archer_rrange[0] and i[0]<self.archer_rrange[1]:
        #         if i[1]>self.archer_crange[0] and i[1]<self.archer_crange[1]:
        #             #attack townhall
        #             hut_ind=huts.get_index(i[0],i[1])
        #             huts.hit_pts[hut_ind]-=self.damage
        #             huts.upd_huts(board)
        for i in range(self.archer_rrange[0],self.archer_rrange[1]+1):
            for j in range(self.archer_crange[0],self.archer_crange[1]+1):
                if board[i][j]=='H':
                    #attack hut
                    hut_ind=huts.get_index(i,j)
                    huts.hit_pts[hut_ind]-=self.damage
                    huts.upd_huts(board)
                    continue

                if board[i][j]=='T':
                    #attack townhall
                    townhall.hit_pts-=self.damage
                    townhall.upd_townhall(board)
                    continue


                if board[i][j]=='X':
                    #attack canon
                    for canon in canons_list:
                        if canon.coordinates[0]==i and canon.coordinates[1]==j:
                            canon.hit_pts-=self.damage
                            canon.upd_canon(board,canons_list)
                            break

                
                # if board[i][j]=='#':
                #     #attack wall
                #     for k in range(len(wall.coordinates)):
                #         if wall.coordinates[k][0]==i and wall.coordinates[k][1]==j:
                #             wall.hit_pts[k]-=self.damage
                #             wall.upd_walls(board)
                #             break

        
        
        adj_coord=[]
        c_x=self.curr_coord[0]
        c_y=self.curr_coord[1]
        # for coordinate in wall.coordinates:
        #     if c_x==coordinate[0] and c_y==coordinate[1]:
        #         board[c_x][c_y]='#'
        #         break
        #     board[c_x][c_y]=' '
        board[c_x][c_y]=' '
        min_len=10000
        new_coord=(c_x,c_y)
        if c_x+1<num_rows-1: adj_coord.append([c_x+1,c_y])
        if c_y+1<num_colms-1: adj_coord.append([c_x,c_y+1])
        if c_x>1: adj_coord.append([c_x-1,c_y])
        if c_y>1: adj_coord.append([c_x,c_y-1])
        if len(huts.coordinates)>0:
            for adj_coordinate in adj_coord:
                c_x=adj_coordinate[0]
                c_y=adj_coordinate[1]
                for i in huts.coordinates:
                    if board[c_x][c_y]==' ':
                        dist=((c_x-i[0])**2+(c_y-i[1])**2)**1/2
                        if  dist < min_len:
                            min_len=dist
                            new_coord=(c_x,c_y)
        
        elif len(townhall.coordinates)>0:
            #attack townhall
            min_len=10000
            t_x=townhall.coordinates[0][0]
            t_y=townhall.coordinates[0][1]
            for adj_coordinate in adj_coord:
                c_x=adj_coordinate[0]
                c_y=adj_coordinate[1]
                if board[c_x][c_y]==' ':
                    dist=((c_x-t_x)**2+(c_y-t_y)**2)**1/2
                    if  dist < min_len:
                        min_len=dist
                        new_coord=(c_x,c_y)
        elif len(canons_list)>0:
            #attack CANON
            for adj_coordinate in adj_coord:
                c_x=adj_coordinate[0]
                c_y=adj_coordinate[1]
                for i in canons_list:
                    if board[c_x][c_y]==' ':
                        dist=((c_x-i.coordinates[0])**2+(c_y-i.coordinates[1])**2)**1/2
                        if  dist < min_len:
                            min_len=dist
                            new_coord=(c_x,c_y)

        self.curr_coord=(new_coord[0],new_coord[1])
        board[new_coord[0]][new_coord[1]]='A'
    
        

        

