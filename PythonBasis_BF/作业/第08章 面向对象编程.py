"""
类：
    创建一个银行类

属性：
    （1）一个属于银行的类属性（1个类属性）：
            用来存储所用银行的开户信息，包含卡号、密码、用户名、余额
            （外界不能随意访问和修改。开户时要进行卡号验证，查看卡号是否已经存在）
    （2）每个对象拥有的实例属性（4个实例属性）：
            卡号、密码、用户名、余额
            （外界不能随意访问和更改）

方法（6个方法）：
    银行类拥有的方法（2个类方法）：
        （1）查看本银行的开户总数
        （2）查看所有用户的个人信息（包含卡号、密码、用户名、余额）
    每个对象拥有的方法（4个普通方法）：
        （3）实例化对象的时候传入相关参数
                初始化对象及类属性
        （4）取钱（需要卡号和密码验证）
                通过验证卡号和密码对个人的余额进行操作，如果取钱大于余额，返回余额不足
        （5）存钱（需要卡号和密码验证）
                通过验证卡号和密码对个人的余额进行操作，返回操作成功
        （6）查看个人详细信息（需要卡号和密码验证）
                返回个人的卡号，用户名，余额信息
"""
class Bank(object):
    """
    这是一个银行类
    """
    # 属性：（1）一个属于银行的类属性（1个类属性）：用来存储所用银行的开户信息，包含卡号、密码、用户名、余额。注意：外界不能随意访问和修改
    __userInfo = {}

    # 属性：（2）每个对象拥有的实例属性（4个实例属性）：卡号、密码、用户名、余额。注意：外界不能随意访问和更改
    def __init__(self, cardId, passWord, userName, balance):
        # 开户时要进行卡号验证，查看卡号是否已经存在
        if cardId not in Bank.__userInfo:
            Bank.__userInfo[cardId] = {'密码': passWord, '用户名': userName, '余额': balance}
            self.cardId = cardId
            self.passWord = passWord
            self.userName = userName
            self.balance = balance
        else:
            print('卡号已存在')

    # 银行类拥有的方法（2个类方法）：（1）查看本银行的开户总数
    @classmethod
    def totalNum(cls):
        print('开户总数：{0}'.format(len(Bank.__userInfo)))

    # 银行类拥有的方法（2个类方法）：（2）查看所有用户的个人信息（包含卡号、密码、用户名、余额）
    @classmethod
    def getInfo(cls):
        for key,val in cls.__userInfo.items():
            print('卡号：{0}，密码：{1}，用户名：{2}，余额：{3}'.format(key, val['密码'], val['用户名'], val['余额']))

    # 验证卡号和密码
    @staticmethod
    def checkId(cardId, passWord):
        if (cardId in Bank.__userInfo) and (passWord == Bank.__userInfo[cardId]['密码']):
            return True
        else:
            return False

    # 验证金额
    @staticmethod
    def checkMoney(money):
        if isinstance(money, int):
            return True
        else:
            False

    # 每个对象拥有的方法（4个普通方法）：（4）取钱（需要卡号和密码验证），通过验证卡号和密码对个人的余额进行操作，如果取钱大于余额，返回余额不足
    def DrawMoney(self, cardId, passWord, money):
        if Bank.checkId(cardId, passWord):
            if Bank.checkMoney(money):
                if Bank.__userInfo[cardId]['余额'] >= money:
                    Bank.__userInfo[cardId]['余额'] -= money
                    print('当前卡号：{0}，取款金额：{1}，余额：{2}'.format(cardId, money, Bank.__userInfo[cardId]['余额']))
                else:
                    print('余额不足')
            else:
                print('金额不是整数')
        else:
            print('卡号或者密码错误')

    # 每个对象拥有的方法（4个普通方法）：（5）存钱（需要卡号和密码验证），通过验证卡号和密码对个人的余额进行操作，返回操作成功
    def SaveMoney(self, cardId, passWord, money):
        if Bank.checkMoney(money):
            if Bank.checkId(cardId, passWord):
                Bank.__userInfo[cardId]['余额'] += money
                print('当前卡号：{0}，存款金额：{1}，余额：{2}'.format(cardId, money, Bank.__userInfo[cardId]['余额']))
            else:
                print('卡号或者密码错误')
        else:
            print('金额不是整数')

    # 每个对象拥有的方法（4个普通方法）：（6）查看个人详细信息（需要卡号和密码验证），返回个人的卡号，用户名，余额信息
    def getUserInfo(self, cardId, passWord):
        if Bank.checkId(cardId, passWord):
            print('卡号：{0}，用户名：{1}，余额：{2}'.format(cardId, Bank.__userInfo[cardId]['用户名'], Bank.__userInfo[cardId]['余额']))
        else:
            print('卡号或者密码错误')




user1 = Bank('622848', 123456, 'Dan', 1000000)

Bank.totalNum()  # 开户总数
Bank.getInfo()   # 查看用户的个人信息

user1.DrawMoney('622848', 123456, 600000)   # 取钱
user1.SaveMoney('622848', 123456, 800000)   # 存钱

user1.getUserInfo('622848', 123456)
