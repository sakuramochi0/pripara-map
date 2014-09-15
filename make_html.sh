#!/bin/zsh

# convert md to html by md2html
for i in *.md; do
    md2html $i -h ${i}-header
done

# move html files to html/
for i in *.html; do
    mv $i html/
done

#rm *.md *.html *-header

