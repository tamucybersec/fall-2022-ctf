#!/bin/ash

header(){
    echo "Do you know these buildings on campus?"
    echo "Answer all of my questions correctly and you get a flag"
    echo ""
    echo "All of your answers should match the regex [A-Z]{3,4}."
    echo "ie: ABCD, ABC"
    echo ""
}

clear
header
echo "What is the name abreviation of the building fetured in challenge1.jpg?"
echo -n "Answer 1: "
read answer1

clear
header
echo "What is the name abreviation of the building fetured in challenge2.jpg?"
echo -n "Answer 2: "
read answer2

clear
header
echo "What is the name abreviation of the building fetured in challenge3.jpg?"
echo -n "Answer 3: "
read answer3

clear
header
echo "What is the name abreviation of the building fetured in challenge4.jpg?"
echo -n "Answer 4: "
read answer4

clear
header
echo "What is the name abreviation of the building fetured in challenge5.jpg?"
echo -n "Answer 5: "
read answer5

clear
header
echo "What is the name abreviation of the building fetured in challenge6.jpg?"
echo -n "Answer 6: "
read answer6


if [ $answer1 = "ZACH" ] && [ $answer2 = "SBSA" ] && [ $answer3 = "PETR" ] && [ $answer4 = "OMB" ] && [ $answer5 = "ETB" ] && [ $answer6 = "MAC" ]; then
    echo "gigem{th3_b3s7_bu1ld1ngs_0n_c4mpu5}"
else
    echo "One or more of your answers was incorrect"
fi

