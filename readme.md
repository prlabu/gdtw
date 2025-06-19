# Smooth Multidimensional Dynamic Time Warping for Speech and High-Dimensional Signals

This repository makes minor updates to the [GDTW library](https://dderiso.github.io/gdtw/) to support **multidimensional signal alignment**, with a focus on applications in speech processing. From GDTW:
>The goal of dynamic time warping (DTW) is to find a function that transforms, or "warps," time in order to approximately align two signals.... Existing methods are often slow, with quadratic time complexity, and suffer from inaccuracies falling into two categories: susceptibility to local minima leading to poor alignments, and/or sharp irregularities in the warping function, known as "singularities" ... Our method is the first general solution that rapidly —in linear time— produces a smooth warping function without the need for any pre- or post-processing steps. 

Key updates in this [`multidim`](https://github.com/prlabu/gdtw/tree/multidim) branch:

- Supports signals of shape `(n_time, n_dims)`, enabling use with multichannel or feature-rich time series like MFCCs or sensor arrays.
- Updated loss function signature: `loss(x, y)` instead of `loss(x - y)` for more flexibility.
- Built-in support for **cosine distance**, alongside L1 and L2 loss functions.
- Speech demo using **MFCC deltas** to align utterances with varying prosody:
  [Try it in Google Colab ▶️](https://colab.research.google.com/drive/1l1OIBvLdHCTEC9_kpZtgZt8vDPbkDNyp#scrollTo=4iohomMdv9b_)

![Speech DTW](./docs/src/images/gdtw-multidim-speech.png "Speech DTW")

## Use Cases 
- Speech signal alignment
- Multisensor trajectory analysis
- MFCC/embedding warping for prosody manipulation
- Motion capture 
- Any high-dimensional dynamic time warping

keywords: Dynamic Time Warping, Speech Alignment, Speech DTW, Multidimensional Time Series, Audio Signal Processing, Speech Signal Processing

## Related Work
[DTWSpeech](https://github.com/aishoot/DTWSpeech)

[speech_dtw](https://github.com/kamperh/speech_dtw)

The original GDTW paper notes that these approaches often require additional pre- and post-processing to avoid singularities. Our implementation builds directly on GDTW's stability and extends it to richer input modalities.



