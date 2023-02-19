# paperclips
#### 透過書籍找到知己

![alt text](https://cdn-images-1.medium.com/max/1000/1*kImjNSBm0WaFAHkaHBDKwg.png)


# SUBMIT 
#### 使用者在 SUBMIT 頁面（如圖二）輸入自己最近看的書、性別和對這本書的想法便能完成登錄。
![alt text](https://cdn-images-1.medium.com/max/1000/1*Jh66UrtXBN1AUSimc1S4Tw.png)


# FIND
#### 使用者在 FIND 頁面搜尋同一本書，便能找到之前所有使用者對這本書留下的想法。
![alt text](https://cdn-images-1.medium.com/max/1000/1*mFEUEpuu2Ko0xObWV53DAg.png)

# USAGE
```
install:
pip install requirements.txt

database:
(venv) $ set FLASK_APP=main.py
若還沒有建立資料庫
(venv) $ flask shell
>>> from main import db
>>> db.create_all()
or 如果不確定的話
>>> db.drop_all()
>>> db.create_all()

run:
python main.py
```
