num_player = int(input("请确定玩家数："))  # 确定玩家数量
while num_player < 2:
    print("最少需要两名玩家")
    num_player = int(input("请确定玩家数："))
num_min = int(input("请输入范围下限："))  # 确定范围下限
num_max = int(input("请输入范围上限："))  # 确定范围上限
ser = 1  # 确定玩家序号
while num_min > num_max:  # 判断数字范围是否正常
    print("范围限定异常")
    num_max = int(input("请输入范围上限："))
    num_min = int(input("请输入范围下限："))
num_gogo = int(input("请输入" + str(num_min) + "-" + str(num_max) + "之间的目标数字："))
while num_gogo >= num_max or num_gogo <= num_min:
    print("目标数字超出范围")
    num_gogo = int(input("请输入1-100之间的目标数字："))
print("游戏开始")  # 游戏开始
x = int(input("请" + str(ser) + "号玩家填入数字："))  # 游戏内容
while x != num_gogo:
    while x <= num_min or x >= num_max:  # 判断输入的数字是否在范围内
        print("填入数字超出范围。")
        x = int(input("请填入数字："))
    if x > num_gogo:  # 判断输入数字应该改变范围上限还是下限
        num_max = x
    else:
        num_min = x
    if ser == num_player:
        ser = 1
    else:
        ser = ser + 1
    print(num_min, "-", num_max)  # 下一位玩家操作
    x = int(input("请" + str(ser) + "号玩家填入数字："))
print("")
print("你炸了！！！！！" + " " * 39 + "你炸了！！！！！")
print("你炸了！！！！！" * 2 + " " * 13 + "你炸了！！！！！" * 2)
print("你炸了！！！！！" * 5)
print("你炸了！！！！！" * 2 + " " * 13 + "你炸了！！！！！" * 2)
print("你炸了！！！！！" + " " * 39 + "你炸了！！！！！")
