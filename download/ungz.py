import os


def file_name(file_dir):   
    for root, dirs, files in os.walk(file_dir):  
        if files.endswith(".gz"):
            print(files) #当前路径下所有非目录子文件
        
        
path = '/home/helin.wang/audioset/audioset_raw/download/validate/'
file_list = os.listdir(path)
for item in file_list:
    if item.endswith('.gz'):
        print(item)
#         if(item[0]=='-'):
#             item2=item[1:]
#             print(item2)
#             os.rename('/home/helin.wang/audioset/audioset_raw/download/validate/'+item,
#                       '/home/helin.wang/audioset/audioset_raw/download/validate/'+item2)
            
#             if(item2[0]=='_'):
#                 print(item2[1:])
        