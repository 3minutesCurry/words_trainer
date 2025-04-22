import random
import time
import importlib, pkgutil

import data

import streamlit as st
import streamlit.components.v1 as components



words_files_list = []

for _, module_name, _ in pkgutil.iter_modules(data.__path__):
    full_name = f"{data.__name__}.{module_name}"
    module = importlib.import_module(full_name)
    dict_count = sum(1 for v in vars(module).values() if isinstance(v, dict))
    words_files_list.append(module)


files_length = len(words_files_list)


st.title("일본어 단어 연습기")
st.write("오늘 하루도 일심히 단어 연습해 봅시다!")



if "file_num" not in st.session_state:
    st.session_state["file_num"] = None

if "step" not in st.session_state:
    st.session_state["step"] = 1


# 값이 설정되었는지 확인
if st.session_state["step"] == 1:
    st.write(f"* 단어장을 선택해주세요")
    for i in range(files_length):
        if st.button(f"{words_files_list[i].name}", key=f"button_{i}"):
            st.session_state["file_num"] = i
            st.session_state["step"] = 2
            st.rerun()


elif st.session_state["step"] == 2:

    file_num = st.session_state["file_num"]
    st.success(f"[{words_files_list[file_num].name}] 단어장을 선택하셨습니다!")
    selected_file = words_files_list[file_num]
    dict_count = sum(1 for v in vars(selected_file).values() if isinstance(v, dict))
    st.write(f"단어장 번호를 선택해주세요")

    for i in range(dict_count-1):
        if st.button(f"단어장 {i+1}", key=f"button_2nd_{i}"):
            st.session_state["dic_num"] = i
            st.session_state["step"] = 3
            st.rerun()

    
elif st.session_state["step"] == 3:
    file_num = st.session_state["file_num"]
    dic_num = st.session_state["dic_num"]
    
    selected_file = words_files_list[file_num]
    dict_list = [val for name, val in vars(selected_file).items()
             if not name.startswith("__") and isinstance(val, dict)]
    
    st.session_state["dict"] = dict_list[dic_num]
    st.session_state["dict_keys"] = list(dict_list[dic_num].keys())
    st.session_state["dict_length"] = len(dict_list[dic_num].keys())
    st.session_state["perm_dict_length"] = len(dict_list[dic_num].keys())
    dict_length = st.session_state["dict_length"]

    st.session_state["step"] = 4
    st.session_state["now_word_number"] = 1
    
    st.rerun()


elif st.session_state["step"] == 4:

    file_num = st.session_state["file_num"]
    dic_num = st.session_state["dic_num"]

    dict = st.session_state["dict"]
    dict_keys = st.session_state["dict_keys"]
    dict_length = st.session_state["dict_length"]
    now_word_number = st.session_state["now_word_number"]
    perm_dict_length = st.session_state["perm_dict_length"]

    if perm_dict_length + 1 == now_word_number:
        st.session_state["step"] = 6
        st.rerun()

    words_random_int = random.randrange(0, len(dict_keys))
    now_key = dict_keys[words_random_int]

    

    if "(" in now_key:
        head, tail = now_key.split("(", 1) 
        tail = "<span style='display: inline-block; max-width: 100%; word-break: break-word;'>(" +tail + "</span>"
    else:
        head = now_key
        tail = ""
    
    st.markdown(f'<p style="text-align:center; font-size:20px;">[ {words_files_list[file_num].name}   {dic_num+1} ]</p>', unsafe_allow_html=True)


    st.markdown(f'<p style="text-align:center; font-size:30px;">{now_word_number}/{perm_dict_length}</p>', unsafe_allow_html=True)
    st.markdown(f'''<p style="text-align:center; font-size:40px;">
    <span style="display: inline-block; max-width: 100%; word-break: break-word;">{head}</span>{tail}
</p>''', unsafe_allow_html=True)
    st.markdown(f'<p style="text-align:center; font-size:40px; visibility:hidden;">빈칸</p>', unsafe_allow_html=True)



    clicked = st.button("▶ 다음으로", key="hidden_button", use_container_width=True)

    del dict_keys[words_random_int]
    st.session_state["dict_keys"] = dict_keys
    st.session_state["dict_length"] = dict_length - 1
    st.session_state["now_key"] = now_key

    st.session_state["step"] = 5
    


        
elif st.session_state["step"] == 5:
    dict = st.session_state["dict"]
    now_key = st.session_state["now_key"]
    dict_length = st.session_state["dict_length"]
    now_word_number = st.session_state["now_word_number"]
    perm_dict_length = st.session_state["perm_dict_length"]


    # 엔터로 클릭될 버튼 (화면에서는 안 보이게 숨김)

    if "(" in now_key:
        head, tail = now_key.split("(", 1) 
        tail = "<span style='display: inline-block; max-width: 100%; word-break: break-word;'>(" +tail + "</span>"
    else:
        head = now_key
        tail = ""

    st.markdown(f'<p style="text-align:center; font-size:30px;">{now_word_number}/{perm_dict_length}</p>', unsafe_allow_html=True)
    st.markdown(f'''<p style="text-align:center; font-size:40px;">
    <span style="display: inline-block; max-width: 100%; word-break: break-word;">{head}</span>{tail}
</p>''', unsafe_allow_html=True)
    st.markdown(f'<p style="text-align:center; font-size:40px;">{dict[now_key]}</p>', unsafe_allow_html=True)


    clicked = st.button("▶ 다음으로", key="hidden_button", use_container_width=True)

    # 버튼이 클릭되었을 때 상태 전환
    st.session_state["step"] = 4
    
    st.session_state["now_word_number"] = now_word_number + 1
    
elif st.session_state["step"] == 6:
    perm_dict_length = st.session_state["perm_dict_length"]
    st.markdown(f"""
<div style="
    background-color: #d4edda;
    color: #155724;
    padding: 15px;
    border-radius: 5px;
    text-align: center;
    font-size: 20px;
    font-weight: bold;
    border: 1px solid #c3e6cb;">
    수고하셨습니다! 총 {perm_dict_length}개의 단어를 공부했습니다.
</div>
""", unsafe_allow_html=True)
    st.balloons()

    st.write("")
    clicked = st.button("다른 단어장 연습하기", use_container_width=True)
     
    if clicked:
        st.session_state["step"] = 1
        st.rerun()

         







