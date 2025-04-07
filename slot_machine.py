import random
balance = 100
symbols = ['🍒','🍋','🍇','🍌','🔔']
def main():
    print('Welcome to the Gamble Ground Slot Machine 🎰')
    print('0️⃣ 0️⃣ 0️⃣')
    while balance > 0:
        print(f'Your balance is {balance:.2f}$')
        bet()
def roll():
    global balance
    balance -= betted_amt
    result = [random.choice(symbols),random.choice(symbols),random.choice(symbols)]
    print(' '.join(result))
    if result[0] == result[1] == result[2]:
        print('JACKPOT!!!')
        balance+=3*betted_amt
def bet():
    global betted_amt
    betted_amt= int(input('Enter your bet: '))
    if betted_amt > balance:
        print('You do not have enough balance! Bet lower.')
    else:
        roll()
if __name__ == '__main__':
    main()