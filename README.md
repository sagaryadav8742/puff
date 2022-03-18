# Puff
Fast web fuzzer written in python

```python
   
usage: main.py [-h] -u  -w

Simple and Fast web fuzzer.

optional arguments:
  -h, --help        show this help message and exit
  -u , --url        Target url { example : https://google.com/PUFF }
  -w , --wordlist   Wordlist path { example : /usr/share/wordlists/dirb/common.txt }               
```


### Requirement

* python3

### Example commands

```python
    puff -u https://github.com/PUFF -w /usr/share/wordlists/dirb/common.txt
```

