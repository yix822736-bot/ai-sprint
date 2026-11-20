class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} 存入 {amount}，余额 {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("余额不足")
            return
        self.balance -= amount
        print(f"{self.owner} 取出 {amount}，余额 {self.balance}")

    def transfer(self, other, amount):
        if amount > self.balance:
            print("余额不足，转账失败")
            return
        self.balance -= amount
        other.balance += amount
        print(f"{self.owner} 转给 {other.owner} {amount}，{self.owner} 余额 {self.balance}")

    def info(self):
        return f"{self.owner}，余额 {self.balance}"


class VipAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount + 10
        print(f"{self.owner} 存入 {amount}，加赠 10，余额 {self.balance}")


vip = VipAccount("老陈", 140)
vip.deposit(60)
vip.withdraw(45)
print(vip.info())









