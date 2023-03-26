#!/bin/env python

from itertools import product
import polars as pl

MIN_LETTERS = 4
MAX_LETTERS = 9
DICES_NUMBER = 5
DICE_FACES = 6
LIST_SIZE = pow(DICE_FACES, DICES_NUMBER)

options = list(range(1, DICE_FACES + 1))
dices = list(product(options, repeat = DICES_NUMBER))
numbers = pl.Series([int(''.join(map(str, t))) for t in dices])

cgrams = ['NOM', 'ADJ']

accents = ['à', 'ä', 'â', 'é', 'é', 'è', 'ê', 'ë', 
    'ô', 'ö', 'î', 'ï', 'ç', 'û', 'ü', '-']

lexique = './lexique/Lexique383.tsv' # The original file from lexique.org
badwords_file = './badwords.txt' # a text file with bad words (one per line).

bw = pl.read_csv(badwords_file, comment_char = '#', has_header=False).to_series()

df = (
    pl.scan_csv(lexique, separator='\t')
    .filter(pl.col('cgram').is_in(cgrams))
    .filter(pl.col('nblettres').is_between(MIN_LETTERS, MAX_LETTERS, 'both'))
    .filter(~pl.col('ortho').str.contains('|'.join(accents))) # exclude accents.
    .filter(~pl.col('ortho').is_in(bw)) # exclude bad words.
    .filter(pl.col('nombre') == 's') # exclude plurals.
    .sort(pl.col('freqlemlivres') + pl.col('freqlemfilms2'), pl.col('ortho'),
          descending=True)
    .unique(subset=['ortho'])
    .limit(LIST_SIZE)
    .sort(pl.col('ortho'))
    .with_columns(numbers.alias('idx'))
    .select(['idx', 'ortho'])
    .collect()
).write_csv('./words.txt', False, separator='\t')


