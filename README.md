# Audio Segmentation Using K-means Clustering

## Table of contents
* [General info](#general-info)
* [Library](#library)
* [Module](#modules-used)

## General Info
My project to separate audio with the noise using k-means clustering based on the idea from the paper L. Marchegiani and I. Posner, "Leveraging the urban soundscape: Auditory perception for smart vehicles," 2017 IEEE International Conference on Robotics and Automation (ICRA), 2017, pp. 6547-6554, doi: 10.1109/ICRA.2017.7989774 [**[1]**](10.1109/ICRA.2017.7989774).


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
- `spec.py`
  - This script create a grayscale mel-spectrogram images from an audio using the datalist from csv that you already created. 
- `k-means.py.py`
  - This script cluster the grayscale mel-spectrogram images into several cluster then make a binary mask based on the threshold that you have decided.

## Check results
You can check the spectrogram and k-means result in the image files in the directory **Ground_truth/mel_spec** and **Ground_truth/mask** respectively.
![1_Audio_1_2022-08-07_12-19-11_3](https://user-images.githubusercontent.com/59830001/195415245-ceb7b0a4-436c-46ea-8a9f-4e824b8d954b.png)
![1_Audio_1_2022-08-07_12-19-11_3 - Copy](https://user-images.githubusercontent.com/59830001/195415256-e46c8fd6-f76f-4bd7-98d0-ac1cba3c3211.png)
![4-111671-B-42](https://user-images.githubusercontent.com/59830001/195415299-37399a5a-3bea-42c5-a359-0856f10ded69.png)
![4-111671-A-42](https://user-images.githubusercontent.com/59830001/195415395-4d930aad-e1df-4629-9916-ed29fd503a85.png)



