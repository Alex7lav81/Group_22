#!/bin/bash
mkdir folder_1/
cd folder_1/
mkdir fold_1 fold_2 fold_3
cd ./fold_1
touch new_file_1.txt new_file_2.txt new_file_3.txt new_file_4.json new_file_5.json
mkdir fol_1 fol_2 fol_3
ls -la
mv ./new_file_3.txt ./new_file_5.json ../fold_2/
sleep 7