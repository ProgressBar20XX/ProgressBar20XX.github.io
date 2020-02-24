
# clculate the time diff

dt=`python -c "from datetime import date as d; print (d(2020, 12, 31) - d.today() ).days"`

dt_text="there are $dt days left before 2020 ends"


# prepare the text

outfile=counting_down_2020.html

# this is my other test
receiver="Mike"
sender="Radish Meeting"
text=`cat template.html`
echo $text >> content.html


text="Dear $receiver,<br> Welcome to join my email list.<br> Hope you enjoy it!<br> 
${dt_text} <br>
check out the parameter: ./create_content.sh , <br> from<br> ProgressBar20XX ( $sender ) <br> Mon Feb 24 18:35:17 UTC 2020"
echo >> $outfile
echo $text >> $outfile


