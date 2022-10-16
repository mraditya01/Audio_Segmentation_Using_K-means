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
  - This script create a grayscale mel-spectrogram images with bandpassfilter from an audio using the datalist of a csv that you already created. 
- `k-means.py`
  - This script cluster the grayscale mel-spectrogram images into several cluster then make a binary mask based on the threshold that you have decided.
## Run
- Run `spec.py` first to create grayscale mel-spectrogram images, then run `k-means.py` to create the binary mask.
- Individual implementation using Jupyter Notebook is also provided on `note_masking.ipynb` and `note_filter.ipynb`.
## Check results
You can check the spectrogram and k-means result in the image files in the directory **Ground_truth/mel_spec** and **Ground_truth/mask** respectively.

![1_Audio_1_2022-08-07_12-19-11_3](https://user-images.githubusercontent.com/59830001/195415245-ceb7b0a4-436c-46ea-8a9f-4e824b8d954b.png)
![1_Audio_1_2022-08-07_12-19-11_3 - Copy](https://user-images.githubusercontent.com/59830001/195415256-e46c8fd6-f76f-4bd7-98d0-ac1cba3c3211.png)
![2-70939-A-42](https://user-images.githubusercontent.com/59830001/195415930-dc58c562-d41f-48ac-a119-ae9064da96c1.png)
![2-70939-A-42](https://user-images.githubusercontent.com/59830001/195415967-7dcdcf43-75cb-4369-8709-26e193189f7e.png)




