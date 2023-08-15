  op1 = GG1 * i1;
  op2 = GG2 * i2;
  op3 = G1 * i2;
  op4 = G2 * i1;
  if (G1 > 10)
  {
     op5 = G1 * i3;
     op5 = op5 + GG1;
     op6 = op5 - op4;
  }
  else
  {
     op5 = i3 * i4;
     op6 = op5 - op3;
  }
  if (!((op5 < op4)^key7))
  {
     op6 = G2 * i4;
     op6 = op6 - i3;
     op17 = op6 - G2;
  }
  else
  {
     op17 = op2 - op4;
     op2 = op4 - op17;
     op17 = op17 - op2;
  }
  op7 = G1 * i4;
  op8 = G2 * i3;

  op9 = op1 + op2;
  op10 = op3 + op4;
  op11 = op4 + op6;
  op12 = op7 + op8;

  op13 = op11 + G1;
  o1 = op13;
  op14 = i6 + op12;
  o2 = op14;
  op15 = G1 * op14;
  op16 = op13 * G2;
  if (op13 == op14)
  {
     op17 = op17 * op11;
     op14 = op14 - op17;
     op15 = op15 + op17;
  }
  else
     op14 = op13 * G1;
  op18 = op14 * G2;
  op19 = op15 * op16;
  op20 = op17 + op18;
  op21 = G1 * op20;
  op22 = op19 * G2;
  op23 = op19 * G1;
  op24 = op20 * G2;
  op25 = op21 + op22;
  op26 = key6 ? op23 + op24 : op23 -1;
  op27 = key5? op9 + op25 : op9 - 25;
  o3 = op27+key3;
  op28 = op10 + op26;
  o4 = op28+key4;
