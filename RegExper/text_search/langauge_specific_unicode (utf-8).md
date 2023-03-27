#[Chinese Simplified]
## Match Simplified Chinese Characters
  ### pattern
    /[\u4e00-\u9fa5]/g

## Match Simplified Chinese Words (Tokenized text, excludes numbers)
  ### pattern
    /([\b]{0,}[\u4e00-\u9fa5]+[\b]{0,})(?=[\s$])/g