#!/bin/zsh
./make_html.py
cd htmls
for i in *.md; do
    pandoc -t html5+lhs -V lang=ja -V css=default.css -V css=http://netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css -H default-header -H ${i:r}-header ${i} -o ../html/${i:r}.html
done

