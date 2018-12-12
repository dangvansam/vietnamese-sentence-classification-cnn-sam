import pandas as pd
import clean_str
#doc du lieu tu file excel va lam sach tung cau trong [text]
input=pd.read_excel('data_train_goc.xlsx',encoding='utf-8')
listtext=input['text'].values
cleaned=[]
for a in listtext:
    x=clean_str.clean_str(a)
    cleaned.append(x)
input['text']=cleaned
input.reset_index()
print(input.head(5))
input.to_csv('data_train_cleaned.csv',encoding='utf-8')
#input.close()
