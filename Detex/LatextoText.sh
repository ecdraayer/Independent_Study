#! /bin/bash

cd "$(dirname "$0")"

for file in Papers/*
do 
  filename=$(basename "$file")
  touch CleanPapers/$filename

  detex -n $file > CleanPapers/$filename
  
done
