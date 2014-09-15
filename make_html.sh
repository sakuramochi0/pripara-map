#!/bin/zsh
for i in *.md; do
    pandoc -t html5+lhs -V lang=ja -V css=default.css -H ${i:r}-header ${i} -o html/${i:r}.html
done

