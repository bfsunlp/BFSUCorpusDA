<div align="center">
<!-- Title: -->
  <a href="https://github.com/bfsunlp/BFSURegexFilter">
    <img src="http://corpus.bfsu.edu.cn/images/bfsucorpuslogo_1.png" height="100" alt="Gitpod Ready-to-Code">
  </a>
  <h1><a href="https://github.com/bfsunlp/BFSURegexFilter">BFSURegexFilter</a> - Python</h1>
<!-- Short description: -->
  <h3>A Python Regulex Expression Tool & Detagging Tool</h3>
</div>

## Environment Setup

### Operating System

Microsoft Windows 10 or Later, MacOS

### Python Version

Python 3.9 (Python 3.7.x or later is available, but the full compatibility is not guaranteed.)

### pip

```bash
pip install chardet
```

### conda

Anaconda3-2022.10-Windows-x86_64.exe

https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/Anaconda3-2022.10-Windows-x86_64.exe

https://repo.anaconda.com/archive/Anaconda3-2022.10-Windows-x86_64.exe

```bash
conda create  --name BFSURegexFilter --file conda-spec-list.txt
```


## Running BFSURegexFilter

The current version BFSURegexFilter 1.0 support both Windows and MacOS.

### Command Line

If you are using command prompt or Anaconda Prompt, please use the following command in Windows Terminal/Anaconda Prompt with administrator previlige and make sure the conda environment BFSURegexFilter is activated.


To process all files located in the root of one directory, use:

```bash
python main.py process_dir -source D:\demo -target D:\Output -regex "\<.*?\>" -replace "" -flag i
```

"D:\demo" is the place where the original files saved in, "D:\Output" is the place where the degagged version of those files to be saved in, both "demo" and "Output" can be replaced with other supported language acronym.

Please be also noted that the algorithm will be multicore optimized in directory mode in next version. 
