# The implementation of paper [B12](https://eprint.iacr.org/2012/078)
Please NOTE that the implementation is for educational purposes only.

## Table of contents
* [Introduction](#introduction)
* [Usage](#usage)
* [Contact](#contact)

## Introduction
- `regev.py` (in folder `utils`) is the implementation of 
[Regev05](https://cims.nyu.edu/~regev/papers/qcrypto.pdf) scheme, 
that is mentioned in section 3.1 in paper [B12](https://eprint.iacr.org/2012/078).
- `core.py` (in folder `utils`) is the implementation of `BitDecomp(x)`
and `PowersOfTwo(y)` that is mentioned in section 3.2 in paper [B12](https://eprint.iacr.org/2012/078).
Additionally, `core.py` includes random generation functions which is very useful in the key generation process.
- `bra.py` (in folder `utils`) is the implementation of 
[B12](https://cims.nyu.edu/~regev/papers/qcrypto.pdf) scheme, (including the implementation 
of Key Switching)

## Usage
To run [B12](https://eprint.iacr.org/2012/078) schemes, run following command:
```
$ python main
```

To run test function implemented in `core.py`:
```
$ python main core
```

To run test function implemented in `regev.py`:
```
$ python main regev
```

To run test function implemented in `bra.py`:
```
$ python main bra
```

## Contact
Khanh Nguyen: tungkhanh@lqdtu.edu.vn
