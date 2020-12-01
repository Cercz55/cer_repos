#!/bin/bash

curl --request POST \ 
  --url 'https://www.virustotal.com/vtapi/v2/file/scan' \
  --form 'apikey=a96748786a0b1785d4ba04f253bbe601ff3f813adcfdb81f1c052fd0dd374145' \
  --form 'file=@/path/to/file'
