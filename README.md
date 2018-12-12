Vietnamese Sentence Classification CNN sam
#Project: Vietnamese Sentence Classification CNN
Input: Thư mục ./data/raw/Train_Full
		- Chứa các lớp (classes) cần phân loại
		- Trong mỗi classes chứa file text (.txt) chứa những câu thuộc chủ đề của class đó
Ouput: Model để phân loại.

#Các bước thực hiện:
1, PREPROCESS DATA FOR TRAINING/ CHUẨN BỊ DỮ LIỆU CHO TRAINING:
	- Đưa dữ liệu (file txt là các câu văn bản kết thúc bằng dấu '.' xuống dòng khi kết thúc 1 câu) vào thư mục data/raw/Train_Full/<lớp>
	- Thư mục ./preprocess chứa file stopword.txt để lọc, chuẩn hóa dữ liệu văn bản, file preprocess.py
	để thực hiện lệnh chuẩn bị dữ liệu đầu ra là file ./data_train
	- Python: python preprocess/preprocess.py
2, TRAINING WITH CNN:
	- Sau khi tạo được file data ở trên thực hiện train:
	- Python: python train.py data_train parameters.json
	+ data_train: file đầu vào
	+ parameters.json: file config CNN
3, PREDICT LABLE FROM TRAINED MODEL:
    - Python: python predict.py ./trained_model_1542913010/ ./data/small_samples.json

######################################################################################################
VERSION 2: INPUT LA FILE EXCEL, CSV

cd c:\vietnamese-sentence-classification-cnn-sam

File đầu vào là file data_train_goc.xlsx chứa 2 colums: lable và text
~B1: Chuẩn hóa dữ liệu text: đọc từng câu trong colum text trong file data_train_goc.xlsx sử lý bằng file editexcelfile.py và clean_str.py
	- Python CMD: python editexcelfile.py
		+ Đầu vào: data_train_goc.xlsx
		+ Đầu ra: data_train_cleaned.csv
~B2: Train với file data_train_cleaned.csv
    - Python CMD: python train.py data_train_cleaned.csv parameters.json
		+ Đầu vào: data_train_cleaned.csv, parameters.json (file chứa thông số config cho train)
		+ Đầu ra: model(Tạo ra 1 thư mục mới chứa model vừa train)
~B3: Predict từ model trained
	-Python CMD: python predict.py ./trained_model_1543270318/ ./data/small_samples.json
		+ Đầu vào: folder chứ model có dạng trained_model_XXXXXXXX, file test dạng json 
		+ Đầu ra: file small_samples_prediction.json chứ dữ liệu được predict lại với new lable được predict lại.
+fix encoding:
	-chcp 65001: hiển thị tiếng việt trong CMD
	-tạo variable evironment(new path): name: PYTHONIOENCODING, value: utf-8
