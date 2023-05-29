for((i = 1; i <= 1500; ++i)); do
    echo $i
    ./gen $i > int
    ./a1 < int > out1
    ./a2 < int > out2
    diff -w out1 out2 || break
done