# this script calculate the time and print the content of the email into counting_down-2020.html


# calculate the time duration

dt=`python -c "from datetime import date as d; print (d(2024, 12, 31) - d.today() ).days"`

percentage=`python -c "from datetime import date as d; print 100-(d(2024, 12, 31) - d.today() ).days*100/365"`

dt_text="there are $dt days left before 2024 ends"

# config
receiver="Mr./Mrs."
sender="RadishMeeting"

# prepare the text

outfile=counting_down_2020.html

text="Dear $receiver,<br> 
<h3> ${dt_text} </h3> <br>
Welcome to join my email list.<br> 
Hope you enjoy it!<br> 
from<br> ProgressBar20XX ( written by $sender ) <br> 
$( date )
"


bar=`cat template2.html`
bar=`cat ../static/progressbar/body_html/percentage$percentage.html`

# clear the file first and then add the text
echo > $outfile
echo $text >> $outfile

echo >>$outfile
echo $bar >> $outfile



