import numpy as np
import pandas as pd
import csv
import os 

# metadata_path = '/home/helin.wang/audioset/audioset_raw/download/balanced_train_segments.csv'
# file_name = '/home/helin.wang/audioset/audioset_raw/download/train'
# df = pd.read_csv(metadata_path, header=0, sep=', ', quoting=csv.QUOTE_NONE)
# train_path = '/home/helin.wang/audioset/audioset_raw/download/train.csv'
# print(df)
# data = df
# a=0
# t = 0
# for i in range(len(df['YTID'])):
#     print(df['positive_labels'][i][1:][:-1])
#     name= df['YTID'][i]
#     if(name[0]=='-'):
#         name=name[1:]
#         if(name[0]=='-'):
#             name=name[1:]
#     for root, dirs, files in os.walk(file_name): 
#             a = 0
#             for x in files:
#                 if(x.startswith(name)):
#                     print(name+':ok')
#                     audio_name = x
#                     a = 1
#                     break
#             if(a == 0):
#                 print('false')
#             else:
#                 print(audio_name)
#                 Data = {'filename':[audio_name], 'start_seconds':[df['start_seconds'][i]]
#                                           , 'end_seconds':[df['end_seconds'][i]], 'positive_labels':[df['positive_labels'][i][1:][:-1]]}
#                 data_train = pd.DataFrame(Data) 
#                 if(t == 0):
#                     fp_test = open(train_path, 'w')
#                     fp_test.write(data_train.to_csv(header=True, index=False))
#                     t =1
#                 else:
#                     fp_test = open(train_path, 'a')
#                     fp_test.write(data_train.to_csv(header=False, index=False))


metadata_path = '/home/helin.wang/audioset/audioset_raw/download/eval_segments.csv'
file_name = '/home/helin.wang/audioset/audioset_raw/download/validate'
df = pd.read_csv(metadata_path, header=0, sep=', ', quoting=csv.QUOTE_NONE)
train_path = '/home/helin.wang/audioset/audioset_raw/download/validate.csv'
print(df)
data = df
a=0
t = 0
for i in range(len(df['YTID'])):
    print(df['positive_labels'][i][1:][:-1])
    name= df['YTID'][i]
    if(name[0]=='-'):
        name=name[1:]
        if(name[0]=='-'):
            name=name[1:]
    for root, dirs, files in os.walk(file_name): 
            a = 0
            for x in files:
                if(x.startswith(name)):
                    print(name+':ok')
                    audio_name = x
                    a = 1
                    break
            if(a == 0):
                print('false')
            else:
                print(audio_name)
                Data = {'filename':[audio_name], 'start_seconds':[df['start_seconds'][i]]
                                          , 'end_seconds':[df['end_seconds'][i]], 'positive_labels':[df['positive_labels'][i][1:][:-1]]}
                data_train = pd.DataFrame(Data) 
                if(t == 0):
                    fp_test = open(train_path, 'w')
                    fp_test.write(data_train.to_csv(header=True, index=False))
                    t =1
                else:
                    fp_test = open(train_path, 'a')
                    fp_test.write(data_train.to_csv(header=False, index=False))
        
        