# python getAllQuestions.py

DIR="images"

# Creating the images output folder
if [ ! -d "$DIR" ]; then
  mkdir $DIR
fi

cd images || exit

file=$(cat ../images.txt)
num=0

for line in $file; do
  name="image$num.png"
  echo "$name"
  wget $line -O $name
  num=$((1 + $num))
done
