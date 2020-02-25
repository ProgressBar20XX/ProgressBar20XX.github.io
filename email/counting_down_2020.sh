# this script calculate the time and print the content of the email into counting_down-2020.html


# calculate the time duration

dt=`python -c "from datetime import date as d; print (d(2020, 12, 31) - d.today() ).days"`

dt_text="there are $dt days left before 2020 ends"


# prepare the text

outfile=counting_down_2020.html

text="Dear $receiver,<br> 
<h4> ${dt_text} </h4> <br>
Welcome to join my email list.<br> 
Hope you enjoy it!<br> 
from<br> ProgressBar20XX ( $sender ) <br> 
$( date )
"
# clear the file first and then add the text
echo > $outfile
echo $text >> $outfile



