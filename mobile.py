import random
import importlib.util
import time
import re

import os


print("일본어 단어 연습기")
time.sleep(0.3)
print("오늘 하루도 열심히 단어 연습해 봅시다!")
time.sleep(0.3)
print("--------------------")
time.sleep(0.3)


BASE_PATH = "data"

# 1. data 안에 있는 폴더 이름 리스트로 반환
def get_subfolders(base_path=BASE_PATH):
    return [name for name in sorted(os.listdir(base_path))
            if os.path.isdir(os.path.join(base_path, name))and not name.startswith("__")]

# 2. data 안의 특정 폴더의 .py 파일들을 모듈로 가져오기
def import_modules_from_folder(folder_name):
    folder_path = os.path.join(BASE_PATH, folder_name)
    modules = {}

    for file in sorted(os.listdir(folder_path)):
        if file.endswith(".py") and not file.startswith("__"):
            file_path = os.path.join(folder_path, file)
            module_name = f"{file[:-3]}"  # 확장자 제거

            spec = importlib.util.spec_from_file_location(module_name, file_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            modules[module_name] = module

    return modules



words_category = get_subfolders()




# 값이 설정되었는지 확인

    

for i in words_category:
    print(f"* {i}")
    time.sleep(0.3)
    

level = input("▶ Level을 선택하세요 : ")
time.sleep(0.3)
print("--------------------")
time.sleep(0.3)

files = import_modules_from_folder(level)
files_names = list(files.keys())

file_order = 1
dic_names = [0]
i = 1
for k in files_names:
    
    time.sleep(0.05)
    if files[k].order != file_order:
        file_order = files[k].order
    file_name = files[k].name
    print(f"{i}. {file_name}")
    time.sleep(0.3)
    dic_names.append(file_name)
    i = i+1

file_num = int(input("▶ 단어장을 선택하세요"))
time.sleep(0.3)
print("--------------------")
time.sleep(0.3)
file_name = dic_names[file_num]
the_file = files[files_names[file_num-1]]


print(f"[{file_name}]를 선택하셨습니다!")
time.sleep(0.3)
    
dict_count = sum(
    1 for k, v in vars(the_file).items()
    if isinstance(v, dict) and not k.startswith("_")
)

dict_count_divided_by_4 = (dict_count) // 4
dict_count_divided_by_4_rest = (dict_count) % 4


print("전체 단어 (all)")
time.sleep(0.3)

for i in range(dict_count):
    print(f"{i+1}번 단어장")
    time.sleep(0.3)

dic_num = input("▶ 단어장 번호를 선택해 주세요")
time.sleep(0.3)
print("--------------------")
time.sleep(0.3)

if dic_num != "all":
    dic_num = int(dic_num) - 1


selected_file = the_file
dict_list = [val for name, val in vars(selected_file).items()
if not name.startswith("__") and isinstance(val, dict)]

if dic_num == "all":
    all_dict = {}

    for i in dict_list:
        all_dict = all_dict | i

    dict = all_dict
    dict_keys = list(all_dict.keys())
    dict_length = len(all_dict.keys())
    perm_dict_length = len(all_dict.keys())
else:
    dict = dict_list[dic_num]
    dict_keys = list(dict_list[dic_num].keys())
    dict_length = len(dict_list[dic_num].keys())
    perm_dict_length = len(dict_list[dic_num].keys())


if the_file.type == "word":
    # 3등분된 열 생성
    print("1. 괄호 O")
    time.sleep(0.3)
    print("2. 괄호 X")
    time.sleep(0.3)
    word_type = int(input("▶ 단어 시험 방식을 선택하세요"))
    print("--------------------")
    time.sleep(0.3)
    
else:
    word_type = 0

if dic_num == "all":
    print(f"{the_file.name} 전체")
else:
    print(f"{the_file.name} {dic_num+1}")
time.sleep(0.3)
print("--------------------")
time.sleep(0.3)

now_word_number = 1


for i in range(dict_length):
    words_random_int = random.randrange(0, len(dict_keys))
    now_key = dict_keys[words_random_int]

    temp_now_key = now_key

    if the_file.type == "word":
        if "[" in now_key:
            if word_type == 2:
                temp_now_key = re.sub(r'\[[^\[\]]*\]', '', now_key)

        if "(" in now_key:
            head, tail = temp_now_key.split("(", 1) 
            tail = ""
        else:
            head = now_key
            tail = ""
    else:
        head = now_key
        tail = ""

    print(f"[{now_word_number}/{perm_dict_length}]")
    time.sleep(0.3)
    print(f"{head}")

    input()
    
    print(now_key)
    time.sleep(0.1)
    print(dict[now_key])
    print("--------------------")
    time.sleep(0.3)
    del dict_keys[words_random_int]
    now_word_number = now_word_number + 1
    
    



if the_file.type == "word":
    type = "단어"
elif the_file.type == "sentence":
    type = "문장"


if isinstance(dic_num, int):
    real_dic_num = dic_num + 1
else:
    real_dic_num = "전체"

print("*수고하셨습니다!")
time.sleep(0.3)
print(f"▶ {the_file.name}")
time.sleep(0.3)
print(f"▶ 단어장 {real_dic_num}")
time.sleep(0.3)
print(f"▶ {perm_dict_length}개의 {type}")


         
