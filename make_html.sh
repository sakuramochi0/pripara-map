#!/bin/zsh
for i in *.md; do
    pandoc -t html5+lhs -H default-header -H ${i:r}-header ${i} -o html/${i:r}.html
done

