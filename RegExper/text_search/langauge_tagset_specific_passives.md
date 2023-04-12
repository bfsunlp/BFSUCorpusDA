"""
Copyright (c) 2021-2023, LIU Dingjia, BFSU NLP Team, BFSU Corpus Research Group.
All rights reserved.
Email:
bfsunlp@gmail.com
dingjialiu@gmail.com
"""

"*" represents an inexact (and or non-exhaustive) match.

# [English]
## Match an English be-passive construction* (Penn Treebank Tagset, "_" as seperator) 
(Penn Treebank Tagset: https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html)
  ### pattern
    /[a-zA-z]+_VB. ([a-zA-z]+_[a-zA-z]+){0,5} [a-zA-z]+_VBN/g