class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount): #입금
        self.balance += amount
        print(f'{amount}원 입금되었습니다. ')

    def withdraw(self, amount):
        if self.balance < amount:
            print('잔액이 부족합니다.')
        else:
            self.balance -= amount

#tranfer 함수 사용해보기
    def transfer(self, other_account, amount):
        # 내 계좌의 잔액이 충분한지 확인
        if self.balance < amount:
            print('잔액이 부족합니다.')
        # 내 계좌에서 송금
        else :
            self.transfer(self.account_number, amount)
        # 상대방 계좌로 송금
            other_account.deposit(amount)
            print(f'{other_account.account_number}로 {amount:,}원 입금되었습니다')


me = BankAccount(12345, 1_000_000)
me2 = BankAccount(56789, 5_000_000)

print(f'이체 전 me 잔액: {me.balance}원')
print(f'이체 전 me2 잔액: {me2.balance}원')

print(me.balance)
me.deposit(1000000)  # 100만원 입금
print(me.balance)
me.transfer(me2, 500000)