echo "Dear XXX,<br>" > content.html
echo >> content.html
echo Welcome to join my email list. >>content.html
echo >> content.html
echo "check out the parameter: $0 , $1" >>content.html

echo >> content.html
echo from >> content.html
echo >> content.html
echo ProgressBar20XX >> content.html
echo >> content.html
date >> content.html


# this is my other test
receiver="Mike"
sender="Radish Meeting"
text=`cat template.html`
echo $text >> content.html


text="Dear $receiver,<br> Welcome to join my email list.<br> Hope you enjoy it!<br> check out the parameter: ./create_content.sh , <br> from<br> ProgressBar20XX ( $sender ) <br> Mon Feb 24 18:35:17 UTC 2020"
echo >> content.html
echo $text >> content.html
