#!/bin/bash

nmap 192.168.1.* > map_segmento.txt
nmap 192.168.1.70 > map_ipdemiseg.txt
nmap 189.175.69.70 > map_ippublic.txt

cat map_segmento.txt map_ipdemiseg.txt map_ippublic.txt | base64 > practica_nmap.txt
