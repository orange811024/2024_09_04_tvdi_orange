# 這是README1

===
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)¶

※內建function open()
*8個參數的數量
*7個有default值的參數
*1個沒有default值的參數
*有沒有傳出值


※呼叫function
1.引數值的呼叫-依照參數的順序
2.引數名稱的呼叫-可不依照順序
3.混和呼叫-前面使用引數值呼叫，後面使用引數名呼叫
引數值意思:類路徑物件(檔案的位置)

(1)引數值的呼叫:
open('names.txt', 'r', -1, 'utf-8')

(2)引數名稱的呼叫:
open(file='names.txt', encoding='utf-8')

(3)
open('names.txt', encoding='utf-8')

((參數有預設值，可省略。))

===

實體:
<_io.TextIOWrapper name='names.txt' mode='r' encoding='utf-8'>

io.TextIOWrapper的實體
簡寫:file的實體

file:
1.屬性-attribute
2.屬性-property
3.方法-method() close(),read()

===

content:
1.屬性-attribute
2.屬性-property
3.方法-method() capitalize(),split()

切割空白鍵:
str.split(sep=None, maxsplit=-1)

split()
split(sep='xxx')
split(maxsplit=2)引數名稱的呼叫
split('xxx')

===

chang_list = []
1.屬性-attribute
2.屬性-property
3.方法-method()

insert
sppend
