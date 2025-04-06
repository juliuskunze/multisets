from pathlib import Path
from scipy.stats import dirichlet
import numpy as np

def generate_multiset(seq_length, alphabet_size, seed, path=Path("multisets")):
    path.mkdir(exist_ok=True)

    unique_count = min(512, max(1, int(seq_length * .6)))
    np.random.seed(seed)

    alphabet = np.arange(alphabet_size)
    source_probs = dirichlet.rvs(alphabet+1).flatten()
    (path / "probs.txt").write_text(', '.join(source_probs.astype(str)))

    alphabet_seen = np.random.choice(
            alphabet, size=unique_count, p=source_probs, replace=False)
    source_probs_seen = source_probs[alphabet_seen]
    source_probs_seen /= source_probs_seen.sum()

    sequence = np.r_[alphabet_seen, np.random.choice(
            alphabet_seen, size=seq_length-unique_count, p=source_probs_seen)]
    (path / f"{seq_length}.txt").write_text(', '.join(sequence.astype(str)))


if __name__ == "__main__":
    for seq_length in [1, 10, 100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000]:
        generate_multiset(seq_length=seq_length, alphabet_size=2 ** 10, seed=0)
