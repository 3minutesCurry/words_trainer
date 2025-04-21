import random
import time
import importlib, pkgutil

import data


print("------------------------------------------------")
time.sleep(0.4)
print()
time.sleep(0.4)
print("* 일본어 단어 연습장 *")
print()
time.sleep(0.4)

words_files_list = []

for _, module_name, _ in pkgutil.iter_modules(data.__path__):
    full_name = f"{data.__name__}.{module_name}"
    module = importlib.import_module(full_name)
    dict_count = sum(1 for v in vars(module).values() if isinstance(v, dict))
    print(f"{module.name} [{dict_count}]")
    time.sleep(0.4)
    words_files_list.append(module)

print()
time.sleep(0.2)
files_length = len(words_files_list)



while True:
    user_input = input(f"단어장을 선택해주세요 (1 ~ {files_length})  ")
    if user_input.isdigit():  # 음수, 소수는 제외됨
        file_num = int(user_input)
        if file_num > 0 and file_num <= files_length :
            break  # 올바른 자연수 입력 -> 루프 종료
        else:
            time.sleep(0.4)
            print()
            time.sleep(0.4)
            print(f"* 다시 입력해주세요 (1 ~ {files_length})  ")
            time.sleep(0.4)
            print("----------------------------")
            time.sleep(0.4)
            print()
            time.sleep(0.4)
    else:
        time.sleep(0.4)
        print()
        time.sleep(0.4)
        print(f"* 다시 입력해주세요 (1 ~ {files_length})  ")
        time.sleep(0.4)
        print("----------------------------")
        time.sleep(0.4)
        print()
        time.sleep(0.4)

print("----------------------------")


selected_file = words_files_list[file_num-1]
dict_count = sum(1 for v in vars(selected_file).values() if isinstance(v, dict))
        
time.sleep(0.4)
print()
time.sleep(0.4)
print(f"* {selected_file.name} [1 ~ {dict_count}]")
time.sleep(0.4)


while True:
    user_input = input(f"단어장 번호를 선택해주세요 (1 ~ {dict_count})  ")
    if user_input.isdigit():  # 음수, 소수는 제외됨
        dic_num = int(user_input)
        if dic_num > 0 and dic_num <= dict_count :
            break  # 올바른 자연수 입력 -> 루프 종료
        else:
            time.sleep(0.4)
            print()
            time.sleep(0.4)
            print(f"* 다시 입력해주세요 (1 ~ {dict_count})  ")
            time.sleep(0.4)
            print("----------------------------")
            time.sleep(0.4)
            print()
            time.sleep(0.4)
    else:
        time.sleep(0.4)
        print()
        time.sleep(0.4)
        print(f"* 다시 입력해주세요 (1 ~ {dict_count})  ")
        time.sleep(0.4)
        print("----------------------------")
        time.sleep(0.4)
        print()
        time.sleep(0.4)


dict_list = [val for name, val in vars(selected_file).items()
             if not name.startswith("__") and isinstance(val, dict)]

nihongo_words = dict_list[dic_num-1]

print("---------------------------------------------")
time.sleep(0.4)
print(f"* {selected_file.name} [{dic_num}] " + "  /  단어 갯수" + str(len(nihongo_words.keys())))
time.sleep(0.4)
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print("----------------------------------")

key_list = list(nihongo_words.keys())
n = len(key_list)
perm_n = n

for i in range(n):
    k = random.randint(0, n-1)
    nihongo = key_list[k]
    time.sleep(0.4)
    print(f"{key_list[k]} [{i+1}/{perm_n}]")
    input()
    time.sleep(0.4)
    print(nihongo_words[nihongo])
    print()
    time.sleep(0.4)
    print("--------------------------------------")
    del key_list[k]
    n = n-1
    time.sleep(0.1)

print()
time.sleep(0.4)
print("*****************************************")
time.sleep(0.4)
print()
time.sleep(0.4)
print(f"수고하셨습니다! 총 {perm_n}개의 단어를 공부했습니다.")
time.sleep(0.4)
print()
time.sleep(0.4)
print("*****************************************")
time.sleep(0.4)
print()



