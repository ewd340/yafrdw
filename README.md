# Yet Another French Diceware Word List

## What

This is yet another French wordlist generated from the
[lexique.org](https://www.lexique.org) dataset, using
[polars](https://www.polar.rs). This list may eventually be used with the
[Diceware](https://theworld.com/~reinhold/diceware.html) method for random
passphrase generation.

## How

Both the wordlist (`words.txt`) and the generator (`collect.py`) may be found in
this repository. The script `collect.py`looks for names and adjectives that are:

- Between 4 and 9 letters long.
- Do no contain any accent (only ASCII characters).
- Are not bad words (not included in the badwords.txt file)
- Are signular (not pluarl words)
- Among the most `LIST_SIZE` (7776) most frequent words


## Disclaimer and License

The Lexiqe3 dataset is distrited under a [CC BY SA 4.0
License](https://github.com/chrplr/openlexicon/blob/master/datasets-info/Lexique382/README-Lexique.md).

The code in `collect.py` is written for my own use. Use it at your own risk. It
is provided as is, without warranty of any kind, and put in the public domain
(please see the UNLICENSE file). Your contributions, ideas, fixes, and
suggestions are most welcome.
