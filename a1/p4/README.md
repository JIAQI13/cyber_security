## Result ##

| hash                                | Command                                                                | Data Source                                                                                         | Runtime      | Password        |
|-------------------------------------|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|--------------|-----------------|
| $1$Nq/Ju/gn$mWMQUwyD80n8hhW52HBAB0  | john --incremental=hex_number unix.txt                                 |                                                                                                     | 1 day 10 hrs | d419debc        |
| $1$1kEPoDDQ$/uCIqvFDIGbYGWUPBB8on0  | john -w:french.lst unix.txt                                            | [source](https://raw.githubusercontent.com/words/an-array-of-french-words/master/corpus.txt)        |  < 30 sec    | phonologiste    |
| $1$WoZLpBhk$gMO9Vy0P3zdhI/XTKpORu.  | john -w:english.lst --external:leet unix.txt                           | [source](https://raw.githubusercontent.com/dwyl/english-words/master/words.txt)                     |  10 hours    | dod3c4hedron    |
| $1$idyigjWm$okvNG8zEgK2G4blETbex31  | python3 triatheles_mangled.py &#124; john --pipe unix.txt              | [source](https://www.triathlon.org/rankings) (Download and combine all available xls)               |  < 5 sec     | Leonie_periault |
| a4835874cb1b608f7bac9611a12c904c    | john -w:english.lst -ru winnt.txt --format=NT-old                      | [source](https://raw.githubusercontent.com/dwyl/english-words/master/words.txt)                     |  < 5 sec     | Dentist         |
| d3c9a4f69ed27aee0c426d26deb3ebbe    | python3 novelist_names.py &#124; john --pipe winnt.txt --format=NT-old | [source](https://en.wikipedia.org/wiki/List_of_Canadian_writers) (Run get_novelist.js from console) |  < 5 sec     | EdenRobinson    |


## Attempted methods ##

Regarding the two not hinted passwords, we were not able to crack them. Here are the methods we have tried:
* All hints of previously cracked passwords

* Custom charset of previously cracked passwords
    * john --incremental=custom_pass \<hashfile>

* English words with 1,2,3,4 digits append/prepend to it with/without separator
    * Confirgure gentail.py of its constant(LENGTH, SEP_LIST, APPEND)
    * python3 gentail.py > tail.txt
    * ./combinator.bin english.lst tail.txt &#124; john --pipe \<hashfile>
    * ./combinator.bin tail.txt english.lst &#124; john --pipe \<hashfile>

* Combination of 2 English words
    * ./combinator.bin english.lst english &#124; john --pipe \<hashfile>

* Names with 1,2,3,4 digits append/prepend to it with/without separator
    * Confirgure gentail.py of its constant(LENGTH, SEP_LIST, APPEND)
    * python3 gentail.py > tail.txt
    * ./combinator.bin all_names.txt tail.txt &#124; john --pipe \<hashfile>
    * ./combinator.bin tail.txt all_names.txt &#124; john --pipe \<hashfile>

* Combination of 2 names
    * ./combinator.bin all_names.txt all_names.txt &#124; john --pipe \<hashfile>

* Leaked passwords as dictionary:
    * [hashkiller](https://hashkiller.co.uk/Downloads/Wordlists)
    * [rockyou.txt](https://wiki.skullsecurity.org/Passwords)  
    * [hashes.org](https://hashes.org/leaks.php)
    
* Built in bruteforce:
    * john \<hashfile> (this has been running for 27 days on our Windows VM)

## Dependencies ##

To install xlrd for python:

* Install deb files in install directory:
    * cd install
    * dpkg -i *.deb
* Unzip and install xlrd:
    *  tar -zxvf xlrd-1.2.0.tar.gz
    * cd xlrd-1.2.0
    * python3 setup.py install
    
    
## Contribution ##
* Minh Nguyen: hinted passwords
* Jiaqi Liu: not hinted passwords
* Xinyu Chen:  