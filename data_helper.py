import re
import logging
import numpy as np
import pandas as pd
from collections import Counter

def clean_str(s):
	return s

def load_data_and_labels(filename):
	"""Load sentences and labels"""
	#Đầu vào là file CVS, EXEL
	df = pd.read_csv(filename, encoding='utf-8', dtype={'text':object})
	selected = ['lable', 'text']
	non_selected = list(set(df.columns) - set(selected))

	df = df.drop(non_selected, axis=1) # Drop non selected columns
	df = df.dropna(axis=0, how='any', subset=selected) # Drop null rows
	df = df.reindex(np.random.permutation(df.index)) # Shuffle the dataframe

	# Map the actual labels to one hot labels
	labels = sorted(list(set(df[selected[0]].tolist())))
	one_hot = np.zeros((len(labels), len(labels)), int)
	np.fill_diagonal(one_hot, 1)
	label_dict = dict(zip(labels, one_hot))

	x_raw = df[selected[1]].apply(lambda x: clean_str(x)).tolist()
	y_raw = df[selected[0]].apply(lambda y: label_dict[y]).tolist()
	print('\nx_raw:\n')
	print("\n==================================================\n")
	print(x_raw)
	print("==================================================\n")
	print('\ny_raw:\n')
	print("\n==================================================\n")
	print(y_raw)
	print("\n==================================================\n")
	print('\nlable:\n')
	print(labels)
	print("\n==================================================\n")
	print('\ndf:\n')
	print(df)
	return x_raw, y_raw, df, labels

def batch_iter(data, batch_size, num_epochs, shuffle=True):
	"""Iterate the data batch by batch"""
	data = np.array(data)
	data_size = len(data)
	num_batches_per_epoch = int(data_size / batch_size) + 1

	for epoch in range(num_epochs):
		if shuffle:
			shuffle_indices = np.random.permutation(np.arange(data_size))
			shuffled_data = data[shuffle_indices]
		else:
			shuffled_data = data

		for batch_num in range(num_batches_per_epoch):
			start_index = batch_num * batch_size
			end_index = min((batch_num + 1) * batch_size, data_size)
			yield shuffled_data[start_index:end_index]

if __name__ == '__main__':
	input_file = 'data_train_cleaned.csv' #ten file da lam sach bang editexcelfile.py va clean_str.py
	load_data_and_labels(input_file)
