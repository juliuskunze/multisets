# Multiset Data

Data used to evaluate [shuffle coding](https://github.com/juliuskunze/shuffle-coding) on multisets
compared to the slower [implementation from [1]](https://github.com/facebookresearch/multiset-compression).
Regenerate data with Python by running 

```bash
pip install -r requirements.txt
python generate.py
```

The data matches the multisets used by [1], but allowing a wider range of multiset sizes to be evaluated.

[1] Daniel Severo, James Townsend, Ashish Khisti, Alireza Makhzani and Karen Ullrich: 
[Compressing Multisets with Large Alphabets using Bits-Back Coding](https://arxiv.org/abs/2107.09202) (2021)
