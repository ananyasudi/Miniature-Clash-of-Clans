from time import sleep
from timeit import default_timer as timer

start = timer()
sleep(1)
end=timer()
print(end-start)

# class person():
#     def __init__(self):
#         self.damage=10
#         self.health=100
#     def gethealth(self):
#         print(self.health)
# class king(person):
#     def __init__(self):
#         super().__init__()
#         self.damage=15
# class barbarian(person):
#     def __init__(self):
#         super().__init__()
#         self.damage=5

# # k=king()
# # print(k.damage)
# # b=barbarian()
# # print(b.damage)
# k=[list("|\/|"),
#     list("|__|")]
# for i in range(4):
#     for j in range(2):
#         print(k[i][j])
