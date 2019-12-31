# domotic_bus_sniffer
Sniffing software for domotic BUS (konnex, scs) - for ESP_KNXGATE and ESP_SCSGATE devices

This is a python3 application - can be used in linux environment (raspberry) or in windows environment.

[![version](https://img.shields.io/badge/version-1.0.0-brightgreen.svg)](CHANGELOG.md)

## History
First version. Sorry for the trivial software solution. This is my first try with python.

## Usage

The software is very easy to use:

    raspberry (linux):
    
                      python3 sniffer.py xxx.xxx.xxx.xxx   (ip address of gate device)
                      exit with ctrl/c
    windows:
                      sniffer.py  xxx.xxx.xxx.xxx   (ip address of gate device)
                      exit closing the windows

The "telegrams" sniffed on the domotic bus are showed in ascii form, in example:

	<domotic system>[lenght]: <data>
  
        SCS[7]: A8 31 00 12 01 22 A3
        SCS[1]: A5
        
        KNX[9]: B4 10 0C 0B 05 E1 00 80 38 
        KNX[1]: CC
```

Copyright (C) 2020-2022 by Guido Pagani <papergion at gmail dot com>
