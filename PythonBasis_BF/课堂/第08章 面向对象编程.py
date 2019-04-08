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
class Bank():
    # 一个属于银行的类属性（1个类属性），用来存储所用银行的开户信息，包含卡号、密码、用户名、余额（外界不能随意访问和修改）
    __Users = {}

    # 对象拥有的实例属性（4个实例属性）：卡号、密码、用户名、余额（外界不能随意访问和更改）
    def __init__(self, CardId, pwd, name, balance):
        # 开户时要进行卡号验证，查看卡号是否已经存在
        if CardId not in Bank.__Users:
            Bank.__Users[CardId] = {'pwd': pwd, 'Username': name, 'Balance': balance}
            self.__CardId = CardId
            self.__pwd = pwd
            self.__name = name
            self.__balance = balance

    # 银行类拥有的方法（2个类方法）：（1）查看本银行的开户总数
    @classmethod
    def nums(cls):
        # 查看本银行的开户总数，即查看字典的长度
        print('当前用户数：{0}'.format(len(cls.__Users)))

    # 银行类拥有的方法（2个类方法）：（2）查看所有用户的个人信息（包含卡号、密码、用户名、余额）
    @classmethod
    def get_Users(cls):
        for key,val in cls.__Users.items():
            print('卡号：{0}，用户名：{1}，密码：{2}，余额：{3}'.format(key, val['Username'], val['pwd'], val['Balance']))

    # 卡号和密码验证方法
    @staticmethod
    def check_User(CardId, pwd):
        if (CardId in Bank.__Users) and (pwd == Bank.__Users[CardId]['pwd']):
            return True
        else:
            return False

    # 验证金额
    @staticmethod
    def check_money(money):
        if isinstance(money, int):
            return True
        else:
            return False

    # 取钱（需要卡号和密码验证），通过验证卡号和密码对个人的余额进行操作，如果取钱大于余额，返回余额不足
    def q_money(self, CardId, pwd, money):
        if Bank.check_User(CardId, pwd):
            # 开始取钱
            if Bank.check_money(money):
                if Bank.__Users[CardId]['Balance'] >= money:
                    Bank.__Users[CardId]['Balance'] -= money
                    print('当前卡号：{0}，当前取款金额：{1}，当前余额：{2}'.format(CardId, money, Bank.__Users[CardId]['Balance']))
                else:
                    print('余额不足')
            else:
                print('您输入的金额有误')
        else:
            print('卡号或者密码有误')

    # 存钱（需要卡号和密码验证），通过验证卡号和密码对个人的余额进行操作，返回操作成功
    def c_money(self, CardId, pwd, money):
        if Bank.check_User(CardId, pwd):
            # 开始存钱
            if Bank.check_money(money):
                Bank.__Users[CardId]['Balance'] += money
                print('当前卡号：{0}，当前存款金额：{1}，当前余额：{2}'.format(CardId, money, Bank.__Users[CardId]['Balance']))
            else:
                print('您输入的金额有误')
        else:
            print('卡号或者密码有误')

    # 查看个人详细信息（需要卡号和密码验证），返回个人的卡号，用户名，余额信息
    def get_Info(self, CardId, pwd):
        if Bank.check_User(CardId, pwd):
            print('当前卡号：{0}，用户名：{1}，当前余额：{2}'.format(CardId, Bank.__Users[CardId]['Username'], Bank.__Users[CardId]['Balance']))
        else:
            print('卡号或者密码有误')

Karon = Bank('622621', 123456, 'Ben', 990000)

Bank.nums()
Bank.get_Users()

Karon.c_money('622621', 123456, 2000000)
Karon.q_money('622621', 123456, 1000000)
Karon.get_Info('622621', 123456)