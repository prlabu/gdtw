# Multidimensional GDTW with application to speech signals


Here we propose a few updates to the [original GDTW codebase](https://dderiso.github.io/gdtw/), which live in the [``multidim``](https://github.com/prlabu/gdtw/tree/multidim) branch of the current repo. 

- All signals are internally treated as 2d (x.shape=(nt,)) where nd is the dimensionality of the signal. Previously, signals were 1d (x.shape=(nt,)). 
- We updated the loss function to take two arguements rather than 1, and added cosine distance as a built-in option in addition to L1 and L2. The loss function takes two arguments, X and Y, with time points nt1 and nt2, and returns a loss 
- Example application to speech: we use MFCC-deltas to dynamically timewarp to utterances emphasizing different words in the utterance "I never said she stole my money". [Check out the Colab Demo here](https://colab.research.google.com/drive/1l1OIBvLdHCTEC9_kpZtgZt8vDPbkDNyp#scrollTo=4iohomMdv9b_). 

![Speech DTW](./docs/src/images/gdtw-multidim-speech.png "Speech DTW")


The updates live on the branch 'multidim' in case the original authors would like to merge these developments with the original code such that the package works off-the-shelf for multidimensional signals. 

keywords: speech dynamic time warping, speech DTW, multidimensional DTW
Other attempts at speech DTW: https://github.com/aishoot/DTWSpeech, https://github.com/kamperh/speech_dtw. As explained in the original GDTW paper, these prior DTW approaches required pre- and post-processing to avoid singularities. 