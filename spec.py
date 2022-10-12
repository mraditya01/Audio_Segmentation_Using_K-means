import librosa
import numpy
import skimage.io
import pandas as pd
from scipy.signal import butter,filtfilt
import argparse

def scale_minmax(X, min=0.0, max=1.0):
    X_std = (X - X.min()) / (X.max() - X.min())
    X_scaled = X_std * (max - min) + min
    return X_scaled


def spectrogram_image(y, sr, out, hop_length, n_mels):
    # use log-melspectrogram
    mels = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels,
                                          n_fft=hop_length * 2, hop_length=hop_length)
    mels = numpy.log(mels + 1e-9)  # add small number to avoid log(0)

    # min-max scale to fit inside 8-bit range
    img = scale_minmax(mels, 0, 255).astype(numpy.uint8)
    img = numpy.flip(img, axis=0)  # put low frequencies at the bottom in image
    img = 255 - img  # invert. make black==more energy

    # save as PNG
    skimage.io.imsave(out, img)

def butter_lowpass_filter(data, cutoff, fs, order):
    nyq = 0.5 * fs
    # normal_cutoff = cutoff / nyq
    # Get the filter coefficients
    b, a = butter(order, cutoff, fs=fs, btype='hp', analog=False)
    y = filtfilt(b, a, data)
    return y

if __name__ == '__main__':
    # settings
    hop_length = 256  # number of samples per time-step in spectrogram
    n_mels = 160  # number of bins in spectrogram. Height of image
    time_steps = 320  # number of time-steps. Width of image
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--data', metavar='N', dest = 'name', type=str,
                    help='file csv location')
    args = parser.parse_args()
    file_name = args.name
    data = pd.read_csv(file_name)
    # load audio. Using example from librosa
    data = pd.read_csv('siren/siren.csv')
    for n in range(len(data)):
        path = f"data/{data.name[n]}.wav"
        y, sr = librosa.load(path, duration=4, sr=11080)
        out = f'Ground_truth/mel_spec/{data.name[n]}.png'
        y = butter_lowpass_filter(y, 500, sr, 2)

        # extract a fixed length window
        start_sample = 0  # starting at beginning
        length_samples = time_steps * hop_length
        window = y[start_sample:start_sample + length_samples]

        # convert to PNG
        spectrogram_image(window, sr=sr, out=out, hop_length=hop_length, n_mels=n_mels)