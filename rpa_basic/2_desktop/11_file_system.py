import os
# print(os.getcwd())
# os.chdir("..")
# print(os.getcwd())
# os.chdir("../")
# print(os.getcwd())

# 파일 경로 만들기
file_path = os.path.join(os.getcwd(), "run_btn.png")
# print(file_path)

# 파일 경로에서 폴더 정보 가져오기
# print(os.path.dirname(r"/Users/js/Desktop/python workspace/rpa_basic/2_desktop/my_file.txt"))

# 파일 정보 가져오기
import time
import datetime

# 파일의 생성 날짜
# ctime = os.path.getctime("run_btn.png") # c for create
# print(ctime) # this will print weird number in terminal. to convert this to be readable..
# print(datetime.datetime.fromtimestamp(ctime).strftime("%Y%m%d %H:%M:%S"))

# # 파일의 수정 날짜
# mtime = os.path.getmtime("run_btn.png")
# print(datetime.datetime.fromtimestamp(mtime).strftime("%Y%m%d %H:%M:%S"))

#  # 파일의 마지막 접근 날짜. a is for access
# atime = os.path.getatime("run_btn.png")
# print(datetime.datetime.fromtimestamp(atime).strftime("%Y%m%d %H:%M:%S"))

# 파일 크기
# size = os.path.getsize(file_path)
# print(size) #result will show in byte

# 파일 목록 가져오기
# print(os.listdir()) # 모든 폴더, 파일 목록 가져오기
# print(os.listdir("2_desktop"))

# 파일 목록 가져오기 (하위 폴더 모두 포함)
#result = os.walk("rpa_basic") # 주어진 폴더 밑에 있는 모든 폴더와 파일 목록 가져오기
# print(result)

# for root,dirs, files in result:
# print(root,dirs,files)

# 만역 폴더 내에서 특정 파일들을 찾으려면?
# name = "11_file_system.py"
# result = []
# for root,dirs, files in os.walk("."): # (".") means current folder
#     if name in files:
#         result.append(os.path.join(root, name)) 
# print(result)


# 만역 폴더 내에서 특정 패턴을 가진 파일들을 찾으려면?
# import fnmatch
# pattern = "file*.png" #file로 시작하고.png로 끝나는 모든 파일
# result = []
# for root,dirs, files in os.walk("."):
#     # [a.txt, b.txt, c.txt, 11_file_system.py, ...]
#     for name in files:
#         if fnmatch.fnmatch(name, pattern):
#             result.append(os.path.join(root,name))
# print(result)
 
# 주어진 경로가 파일인지 폴더인지 확인
# print(os.path.isdir("rpa_basic"))
# print(os.path.isfile("rpa_basic")) 
# print(os.path.isdir("run_btn.png"))
# print(os.path.isfile("run_btn.png"))

 # 파일 만들기
#open("new_file.txt", "a").close() #빈 파일 생성

# 파일명 변경하기
#os.rename("new_file.txt", "new_file_rename.txt")

# 파일 삭제하기
# os.remove("new_file_rename.txt")

#폴더 만들기
# os.mkdir("new_folder")

# os.makedirs("new_folders/a/b/c") # how to make foldres inside a folder

# 폴더명 변경하기
# os.rename("new_folder","new_folder_rename")

# # 폴더 지우기 (폴더 안이 비어있을때 만)
# os.rmdir("new_folder_rename")


import shutil # shell utilities
# shutil.rmtree("new_folders") # 폴더안이 비어있지 않아도 완전 삭제 가능
# 모든 파일이 삭제될수 있으므로 주의

# 파일 복사하기
# 어떤 파일을 폴더 안으로 복사하기
# shutil.copy("run_btn.png","test_folder")
# shutil.copy("run_btn.png","test_folder/copied_run_btn.png")

# shutil.copyfile("run_btn.png","test_folder/copied_run_btn_2.png")

# shutil.copy2("run_btn.png","test_folder/copy2.png")

# copy, copyfile : 메타정보 복사 안함
# copy 2 : 메타정보 복사 함


# # 폴더 복사
# shutil.copytree("test_folder","test_folder2") # everything inside the folder also copied
# shutil.copytree('test_folder',"test_folder3")

# # 폴더 이동
# shutil.move("test_folder","test_folder3")
# shutil.move("test_folder2", "test_folder3")
