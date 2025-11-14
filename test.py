import random
import time

winning_percents = [1.05, 1.06, 1.10, 1.15]
losing_percents = [0.97, 0.95, 0.94]



def simulator(start_money, winning, losing, percent, times):
    A_account = start_money
    B_account = start_money
    B_saving_account = 0
    C_account = start_money
    C_saving_account = 0

    winning_times = 0
    losing_times = 0

    for i in range(times):
        print(f"{i+1}번째 시행")
        time.sleep(0.2)
        plus_minus = ""
        if percent >= random.random():
            winning_times += 1

            interest = random.choice(winning)

            pre_A = A_account
            pre_B = B_account
            pre_B_saving = B_saving_account
            pre_C = C_account
            pre_C_saving = C_saving_account

            A_account = int(A_account * interest)

            B_saving_account += int(B_account * interest) - B_account
            
            if start_money > int(C_account * interest):
                C_account = int(C_account * interest)
            else:
                C_saving_account += int(C_account * interest) - start_money
                C_account = start_money

            plus_minus = "+"
            print("이득")
        else:
            losing_times += 1

            interest = random.choice(losing)

            pre_A = A_account
            pre_B = B_account
            pre_B_saving = B_saving_account
            pre_C = C_account
            pre_C_saving = C_saving_account

            A_account = int(A_account * interest)

            B_saving_account += int(B_account * interest) - B_account

            C_account += int(C_account * interest) - C_account

            
            print("손해")

        print(f"이득 : {winning_times} / 손해 : {losing_times}")
            

        print(f"A계좌 : {pre_A} => {A_account}, ({plus_minus}{int(pre_A * interest-pre_A)})")
        print(f"B계좌 : {pre_B + pre_B_saving} => {B_account + B_saving_account}, ({plus_minus}{int(pre_B * interest - pre_B)})")
        print(f"B거래 계좌 : {B_account} / B저축 계좌 : {B_saving_account}")
        print(f"C계좌 : {pre_C + pre_C_saving} => {C_account + C_saving_account}, ({plus_minus}{int(pre_C * interest - pre_C)})")
        print(f"C거래 계좌 : {C_account} / C저축 계좌 : {C_saving_account}")

        


simulator(1000000, winning_percents, losing_percents, 0.4, 10000)