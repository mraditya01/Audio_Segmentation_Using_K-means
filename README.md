# Audio Segmentation Using K-means Clustering

## Table of contents
* [General info](#general-info)
* [Library](#library)
* [Module](#modules-used)

## General Info
My project to separate 

## Package Requirement
- numpy
- cv2
- IPython
- matplotlib
- skimage
- sklearn
- pandas
- argparse
- librosa
- scipy

## Description
The system consists of two main scripts:
- `00_train.py`
  - This script trains models for each Machine Type by using the directory **dev_data/<Machine_Type>/train/** or **eval_data/<Microphone_Number>/train/**.
- `01_test.py`
  - This script makes csv files for each Machine ID including the anomaly scores for each wav file in the directory **dev_data/<Microphone_Number>/test/** or **eval_data/<Microphone_Number>/test/**.
  - The csv files will be stored in the directory **result/**.
  - If the mode is "development", it also makes the csv files including the AUC and pAUC for each Machine ID. 
- `train.ipynb`
  - This script trains models for one Machine Type of your choice by using the directory **dev_data/<Machine_Type>/train/** or **eval_data/<Machine_Type>/train/**.

## Check results
You can check the spectrogram and k-means result in the image files in the directory **Ground_truth/mel_spec** and **Ground_truth/mask**.

