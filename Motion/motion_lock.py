def motion(in1, in2, in3, in4, in5, in6, in7, in8, in9, in10, key_1, key_2, key_3, key_4):
    mult1 = in1 * in2
    mult2 = in1 * (2 * key_1)
    mult3 = in3 * (4 + key_2)
    mult4 = in4 * in5
    mult5 = in3 * in2
    mult6 = in2 * in5
    mult7 = in3 * in6
    mult8 = in4 * in7
    mult9 = in4 * in8
    mult10 = in6 * in9
    mult11 = in6 * in8
    mult12 = in7 * in9
    mult13 = in7 * in8
    mult14 = in9 * in10

    add1 = in1 * mult2
    add2 = (2 * key_3 + 3) * mult4

    if (add1 > add2 and key_4 == 5):
        add3 = in5 * mult8
        add4 = mult10 * in4
        add5 = in10 * mult14
    else:
        add3 = in5 + mult8
        add4 = mult10 * in3
        add5 = in10 / mult14

    add6 = mult1 + add1
    out1 = add6

    add7 = mult3 + add2
    add8 = mult5 + add7

    add10 = mult7 + add3
    add9 = mult6 + add10

    # shf1 = add9 << 3
    out2 = add8

    add13 = mult9 + add4
    add11 = add13 + mult11

    add15 = mult13 + add5
    add14 = mult12 + add15

    # shf2 = add14 >> 3
    out3 = add11
    return (out1 , out2 , out3)

def oracle(s):
    s = s.encode('utf-8')
    input = list(map(int,s.decode('utf-8').split()))
    # print(input)
    return motion(input[0], input[1], input[2], input[3], input[4], input[5], input[6], input[7], input[8], input[9] , 5 ,12 , 6 , 5)
    
