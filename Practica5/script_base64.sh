#!/bin/bash
cat fcfm.png | base64 > fcfm_base64.txt
cat mystery_img1.txt | base64 --decode > mystery_img1_decoded.png
cat mystery_img2.txt | base64 --decode > mystery_img2_decoded.png
cat msg.txt | base64 | base64 --decode > msg_coded.txt
