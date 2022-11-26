## main_table = table1_colum + table2_colum + table3_colum + table4_colum + table5_colum + table6_colum

##                   履歴
## 2022/11/24 - LotoAI - WebScriping 成功
##                     - Excel へ 出力 成功
##                                                           ---

## NEXT STEP
##        - Excelへ出力をする値が1文字の場合01ではなく1として保存。
##        - DataBeseへ保存
##                                                           ---


## PYTHON LEVEL UP
## ・取得する処理のコードをできるだけ短くやり直す
##                                                           ---

import pandas as pd

url = 'http://www.ohtashp.com/topics/takarakuji/index_2013-18.html#ank2013'
url2 = 'http://www.ohtashp.com/topics/takarakuji/'

data = pd.read_html(url)
data2 = pd.read_html(url2)

data3 = data2[0].head(201)

table7_colum = data3[["抽選日", "本数字"]]

table1 = data[5]
table2 = data[4]
table3 = data[3]
table4 = data[2]
table5 = data[1]
table6 = data[0]

table1_colum = table1[["抽選日", "本数字"]]
table2_colum = table2[["抽選日", "本数字"]]
table3_colum = table3[["抽選日", "本数字"]]
table4_colum = table4[["抽選日", "本数字"]]
table5_colum = table5[["抽選日", "本数字"]]
table6_colum = table6[["抽選日", "本数字"]]

data_concat = pd.concat([table7_colum,table6_colum,table5_colum,table4_colum,table3_colum,table2_colum,table1_colum])
print(data_concat)

data_concat.to_excel('pandas_to_excel.xlsx', sheet_name='new_sheet_name')