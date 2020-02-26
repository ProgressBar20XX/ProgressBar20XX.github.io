
for i in {0..100}
do
    cp template.html html/percentage$i.html
    sed -i '' "s/PLACEHOLDER_WIDTH/$i/g" html/percentage$i.html
done

less html/percentage5.html
