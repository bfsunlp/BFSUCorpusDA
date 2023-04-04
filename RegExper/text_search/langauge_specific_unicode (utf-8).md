# [Chinese Simplified]
## Match Simplified Chinese Characters
  ### pattern
    /[\u4e00-\u9fa5]/g

## Match Simplified Chinese Words (tokenized text； excludes puctuations, symbols and numbers not concatenated with characters)
  ### pattern
    /([\b]{0,}[0-9]{0,}[\u4e00-\u9fa5]{1,}[0-9]{0,}[\b]{0,})(?=[\s$])/g

# [Korean]
## Match Korean Characters (symbos, numbers, punctuations are excluded)
  ### pattern
    /[\uac00-\ud7a3]/g

## Match Korean Words (tokenized text；excludes puctuations, symbols and numbers not concatenated with characters)
  ### pattern
    /([\b]{0,}[0-9]{0,}[\uac00-\ud7a3]{1,}[0-9]{0,}[\b]{0,})+(?=[\s$])/g