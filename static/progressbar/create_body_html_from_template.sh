
for i in {0..100}
do
    cp template_body.html body_html/percentage$i.html
    sed -i '' "s/PLACEHOLDER_WIDTH/$i/g" body_html/percentage$i.html
done

less body_html/percentage5.html
