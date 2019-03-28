import random
class Game():
    version = 4.7
    company = "腾讯游戏"
    GameName = "超级玛丽"
    __Winner = []

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def PlayGame(self):
        print("游戏开始")
        num = random.randint(0, 20)
        count = 0
        while True:
            me = int(input("请输入数值："))
            count += 1
            if me == num:
                print("你猜对了！")
                break
            elif me > num:
                print("大了")
            else:
                print("小了")
        print("{0}通关了游戏，共使用了{1}次。".format(self.name, count))
        Game.__Winner.append({"name": self.name, "count": count})
        # 设置类方法
        @classmethod
        def ShowWinner(cls):
            print("========排行榜========")
            cls.__Winner = sorted(cls.__Winner, key=lambda x: x['count'])
            rank = 1
            for once in cls.__Winner:
                print("第{0}名为{1}，成绩为{2}次".format(rank, once["name"], once["count"]))
                rank += 1
        # 静态方法，不需要传类或者对象，一般用到工具类的时候，静态方法使用的比较多
        @staticmethod
        def GameHelp():  # 游戏帮助
            print("这是一个比较大小的游戏，范围是在0-20之间，你需要输入数值，去跟随机生成的数做比较，如果相等，你就赢了。")
p1 = Game("小明", 13566669999)
p2 = Game("小天", 13588883333)
p1.PlayGame()
p2.PlayGame()
Game.ShowWinner()
Game.GameHelp()