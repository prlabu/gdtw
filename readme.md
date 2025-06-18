# Multidimensional gDTW and application to speech signal


Here we propose a few updates to the codebase, which are in the branch ["multidim"](https://github.com/prlabu/gdtw/tree/multidim) branch. 

- All signals are either 1d (nt, 1) or 2d (nt, nd) where nd is the dimensionality of the signal. 
- cosine distance loss function between two timepoints in the signal X, Y. The original version offers only L1 and L2 distances between timepoints.
- Example application to speech: we use MFCC-deltas to dynamically timewarp to utterances emphasizing different words in "I never said she stole my money": [see the Colab Demo here](https://colab.research.google.com/drive/1l1OIBvLdHCTEC9_kpZtgZt8vDPbkDNyp#scrollTo=4iohomMdv9b_). 

![alt text](./docs/src/images/gdtw-multidim-speech.png "Title")


- The updates live on the branch 'multidim' in case the original authors would like to merge these developments with the original code such that the package works off-the-shelf for multidimensional signals. 

Below is the  README from the original package. 
--- 

# GDTW

_Please visit the documentation and interactive demo site at [https://dderiso.github.io/gdtw](https://dderiso.github.io/gdtw)._

GDTW is a Python/C++ library that performs dynamic time warping. 
It is based on a paper by Dave Deriso and Stephen Boyd.

## Installation

```
pip install gdtw
```

## Documentation

For full documentation, including a quick-start tutorial, please see [https://dderiso.github.io/gdtw](https://dderiso.github.io/gdtw).


## Our Paper

Please see [the published article](https://rdcu.be/cT5dD).

## Citing

```
@article{deriso2022general,
  title={A general optimization framework for dynamic time warping},
  author={Deriso, Dave and Boyd, Stephen},
  journal={Optimization and Engineering},
  pages={1--22},
  year={2022},
  publisher={Springer}
}
```

## Linux

Limited Linux support. Currently supports Python 3.6 on: CentOS 7 rh-python38, CentOS 8 python38, Fedora 32+, Mageia 8+, openSUSE 15.3+, Photon OS 4.0+ (3.0+ with updates), Ubuntu 20.04+

See [manylinux](https://github.com/pypa/manylinux) for latest list of versions supported under `manylinux2014`. 
