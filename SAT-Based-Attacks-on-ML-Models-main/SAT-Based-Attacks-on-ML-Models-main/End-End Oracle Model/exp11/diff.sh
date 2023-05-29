for((i = 1; i <= 1500; ++i)); do
    echo $i
    ./gen $i > int
    ./a < int > out1
    ./a1 < int > out2
    ./a2 < int > out3
    diff -w out1 out2 || break
    diff -w out1 out3 || break
done