# [English]
## Match an English Letter (symbols, numbers, punctuations are excluded)
  ### pattern
    /[A-Za-z]/g

## Match a Simplified Chinese Word (support tokenized text； excludes puctuations, symbols and numbers not concatenated with characters)
  ### pattern
    /([\b]{0,}[0-9]{0,}[A-Za-z]{1,}[0-9]{0,}[\b]{0,})+(?=[\s$])/g

# [Chinese Simplified]
## Match a Simplified Chinese Character (symbols, numbers, punctuations are excluded)
  ### pattern
    /[\u4e00-\u9fa5]/g

## Match a Simplified Chinese Words (support tokenized text； excludes puctuations, symbols and numbers not concatenated with characters)
  ### pattern
    /([\b]{0,}[0-9]{0,}[\u4e00-\u9fa5]{1,}[0-9]{0,}[\b]{0,})+(?=[\s$])/g

# [Korean]
## Match a Korean Character (symbols, numbers, punctuations are excluded)
  ### pattern
    /[\uac00-\ud7a3]/g

## Match a Korean Word (support tokenized text；excludes puctuations, symbols and numbers not concatenated with characters)
  ### pattern
    /([\b]{0,}[0-9]{0,}[\uac00-\ud7a3]{1,}[0-9]{0,}[\b]{0,})+(?=[\s$])/g