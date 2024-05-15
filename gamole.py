# Craps赌博游戏
# 玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
# 如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
# 玩家再次要色子 如果摇出7点 庄家胜
# 如果摇出第一次摇的点数 玩家胜
# 否则游戏继续 玩家继续摇色子
# 玩家进入游戏时有1000元的赌注 全部输光游戏结束

# from random import randint
#
# stake = 1000
# while stake > 0:
#     print('你的资金是', stake)
#     ndees = False
#     while True:
#         useStake = int(input('请下注'))
#         if 0 < useStake < stake:
#             break
#     num = randint(1,6) + randint(1,6)
#     print('1-玩家摇出的点数=',num)
#     if num == 7 or num == 11:
#         print('玩家胜')
#         stake += useStake
#     elif num == 2 or num == 3 or num == 12:
#         print('庄家胜')
#         stake -= useStake
#     else:
#         ndees = True
#
#     while ndees:
#         num2 = randint(1,6) + randint(1,6)
#         print('2-玩家摇出的点数=',num2)
#         if num2 == 7:
#             print('庄家胜')
#             stake -= useStake
#             ndees = False
#         elif num2 == num:
#             print('玩家胜')
#             stake += useStake
#             ndees = False
# print('没钱了')





























