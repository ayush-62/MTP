`timescale 1ns / 1ps


module toy ( datain, clk, rst, op, valid, dataout );
  input [7:0] datain;
  input [1:0] op;
  output [7:0] dataout;
  input clk, rst;
  output valid;
  wire   n_155, n_156, n_154, data_5_, data_4_, data_3_, n_152, n_151, n_145,
         n_147, n_149, n_148, data_7_, n_144, n_143, data_6_, data_1_, data_0_,
         data_2_, n_142, n_140, n_137, n_135, n_130, next_state_4_,
         next_state_6_, n_172, n_97, next_state_5_, n_80, next_state_3_, n_44,
         n_42, n_41, n_40, n_49, n_38, n_39, n_43, n_48, n_45, n_46,
         next_state_1_, next_state_7_, next_state_0_, n_29, n_30, n_31, n10,
         n90, n91, n92, n93, n94, n95, n96, n97, n98, n99, n100, n101, n102,
         n103, n104, n105, n106, n107, n108, n109, n110, n111, n112, n113,
         n114, n115, n116, n117, n118, n119, n120, n121, n122, n123, n124,
         n125, n126, n127, n128, n129, n130, n131, n132, n133, n134, n135,
         n136, n137, n138, n139, n140, n141, n142, n143, n144, n145, n146,
         n147, n148, n149, n150, n151, n152, n153, n154, n155, n156, n157,
         n158, n159, n160, n161, n162, n163, n164, n165, n166, n167, n168,
         n169, n170, n171, n172, n173, n174, n175, n176, n177;

  dfxbp_1 _dataout_reg_4_ ( .D(n_155), .CLK(clk), .Q(dataout[4]) );
  dfxbp_1 _dataout_reg_5_ ( .D(n_156), .CLK(clk), .Q(dataout[5]) );
  dfxbp_1 _dataout_reg_3_ ( .D(n_154), .CLK(clk), .Q(dataout[3]) );
  dfxbp_1 _dataout_reg_7_ ( .D(n_152), .CLK(clk), .Q(dataout[7]) );
  dfxbp_1 _dataout_reg_6_ ( .D(n_151), .CLK(clk), .Q(dataout[6]) );
  dfxbp_1 _dataout_reg_0_ ( .D(n_145), .CLK(clk), .Q(dataout[0]) );
  dfxbp_1 _data_reg_5_ ( .D(n_147), .CLK(clk), .Q_N(data_5_) );
  dfxbp_1 _dataout_reg_1_ ( .D(n_149), .CLK(clk), .Q(dataout[1]) );
  dfxbp_1 _data_reg_4_ ( .D(n_148), .CLK(clk), .Q_N(data_4_) );
  dfxbp_1 _dataout_reg_2_ ( .D(n_144), .CLK(clk), .Q(dataout[2]) );
  dfxbp_1 _data_reg_3_ ( .D(n_143), .CLK(clk), .Q_N(data_3_) );
  dfxbp_1 _data_reg_6_ ( .D(n_142), .CLK(clk), .Q_N(data_6_) );
  dfxbp_1 _data_reg_7_ ( .D(n_140), .CLK(clk), .Q_N(data_7_) );
  dfxbp_1 _data_reg_1_ ( .D(n_137), .CLK(clk), .Q_N(data_1_) );
  dfxbp_1 _data_reg_0_ ( .D(n_135), .CLK(clk), .Q_N(data_0_) );
  dfxbp_1 _data_reg_2_ ( .D(n_130), .CLK(clk), .Q_N(data_2_) );
  dfrbp_1 _curr_state_reg_4_ ( .D(next_state_4_), .CLK(clk), .RESET_B(rst), 
        .Q(n174), .Q_N(n101) );
  dfrbp_1 _curr_state_reg_6_ ( .D(next_state_6_), .CLK(clk), .RESET_B(rst), 
        .Q(n168) );
  dfxbp_1 _next_state_reg_6_ ( .D(n_172), .CLK(clk), .Q(next_state_6_) );
  dfxbp_1 _next_state_reg_4_ ( .D(n_97), .CLK(clk), .Q(next_state_4_) );
  dfrbp_1 _curr_state_reg_5_ ( .D(next_state_5_), .CLK(clk), .RESET_B(rst), 
        .Q(n173), .Q_N(n98) );
  dfxbp_1 _next_state_reg_5_ ( .D(n_80), .CLK(clk), .Q(next_state_5_) );
  dfrbp_1 _curr_state_reg_3_ ( .D(next_state_3_), .CLK(clk), .RESET_B(rst), 
        .Q(n177), .Q_N(n99) );
  dfxbp_1 _OP_reg_0_ ( .D(n_44), .CLK(clk), .Q(n164) );
  dfxbp_1 _inputs_reg_0_ ( .D(n_42), .CLK(clk), .Q(n172), .Q_N(n96) );
  dfxbp_1 _inputs_reg_4_ ( .D(n_41), .CLK(clk), .Q_N(n171) );
  dfxbp_1 _inputs_reg_1_ ( .D(n_40), .CLK(clk), .Q(n161), .Q_N(n93) );
  dfxbp_1 _inputs_reg_2_ ( .D(n_49), .CLK(clk), .Q(n169), .Q_N(n95) );
  dfxbp_1 _next_state_reg_3_ ( .D(n_38), .CLK(clk), .Q(next_state_3_) );
  dfxbp_1 _OP_reg_1_ ( .D(n_39), .CLK(clk), .Q(n163), .Q_N(n103) );
  dfxbp_1 _inputs_reg_3_ ( .D(n_43), .CLK(clk), .Q_N(n92) );
  dfxbp_1 _inputs_reg_5_ ( .D(n_48), .CLK(clk), .Q(n167), .Q_N(n94) );
  dfxbp_1 _inputs_reg_6_ ( .D(n_45), .CLK(clk), .Q(n170), .Q_N(n100) );
  dfxbp_1 _inputs_reg_7_ ( .D(n_46), .CLK(clk), .Q(n166), .Q_N(n97) );
  dfrbp_1 _curr_state_reg_1_ ( .D(next_state_1_), .CLK(clk), .RESET_B(rst), 
        .Q(n175), .Q_N(n102) );
  dfrbp_1 _curr_state_reg_7_ ( .D(next_state_7_), .CLK(clk), .RESET_B(rst), 
        .Q(n165), .Q_N(n90) );
  dfrbp_1 _curr_state_reg_0_ ( .D(next_state_0_), .CLK(clk), .RESET_B(rst), 
        .Q(n91), .Q_N(n162) );
  dfxbp_1 _next_state_reg_0_ ( .D(n_29), .CLK(clk), .Q(next_state_0_) );
  dfrbp_1 _curr_state_reg_2_ ( .D(valid), .CLK(clk), .RESET_B(rst), .Q(n176)
         );
  dfxbp_1 _next_state_reg_7_ ( .D(n_30), .CLK(clk), .Q(next_state_7_) );
  dfxbp_1 _next_state_reg_1_ ( .D(n_31), .CLK(clk), .Q(next_state_1_) );
  dfxbp_1 _next_state_reg_2_ ( .D(n10), .CLK(clk), .Q(valid) );
  nand2_1 U105 ( .A(n104), .B(n105), .Y(n_97) );
  nand3_1 U106 ( .A(n164), .B(n106), .C(n163), .Y(n105) );
  and2_0 U107 ( .A(datain[2]), .B(n107), .X(n_49) );
  and2_0 U108 ( .A(datain[5]), .B(n107), .X(n_48) );
  and2_0 U109 ( .A(datain[7]), .B(n107), .X(n_46) );
  and2_0 U110 ( .A(datain[6]), .B(n107), .X(n_45) );
  and2_0 U111 ( .A(op[0]), .B(n107), .X(n_44) );
  and2_0 U112 ( .A(datain[3]), .B(n107), .X(n_43) );
  and2_0 U113 ( .A(datain[0]), .B(n107), .X(n_42) );
  and2_0 U114 ( .A(datain[4]), .B(n107), .X(n_41) );
  and2_0 U115 ( .A(datain[1]), .B(n107), .X(n_40) );
  and2_0 U116 ( .A(op[1]), .B(n107), .X(n_39) );
  and3_1 U117 ( .A(n162), .B(n107), .C(n108), .X(n_38) );
  nand4_1 U118 ( .A(n109), .B(n110), .C(n111), .D(n108), .Y(n107) );
  nor2_1 U119 ( .A(n_31), .B(n112), .Y(n111) );
  nand2_1 U120 ( .A(n104), .B(n113), .Y(n_31) );
  nand4_1 U121 ( .A(n114), .B(n102), .C(n90), .D(n91), .Y(n113) );
  nand2_1 U122 ( .A(n104), .B(n108), .Y(n_30) );
  nand2_1 U123 ( .A(n104), .B(n115), .Y(n_29) );
  nand3_1 U124 ( .A(n114), .B(n90), .C(n116), .Y(n115) );
  inv_1 U125 ( .A(n117), .Y(n_172) );
  a21oi_1 U126 ( .A1(n106), .A2(n164), .B1(n_80), .Y(n117) );
  o21ai_0 U127 ( .A1(n108), .A2(n103), .B1(n104), .Y(n_80) );
  inv_1 U128 ( .A(n108), .Y(n106) );
  nand4_1 U129 ( .A(n162), .B(n175), .C(n114), .D(n90), .Y(n108) );
  nor2_1 U130 ( .A(n104), .B(data_5_), .Y(n_156) );
  nor2_1 U131 ( .A(n104), .B(data_4_), .Y(n_155) );
  nor2_1 U132 ( .A(n104), .B(data_3_), .Y(n_154) );
  nor2_1 U133 ( .A(n104), .B(data_7_), .Y(n_152) );
  nor2_1 U134 ( .A(n104), .B(data_6_), .Y(n_151) );
  nor2_1 U135 ( .A(n104), .B(data_1_), .Y(n_149) );
  o211ai_1 U136 ( .A1(n171), .A2(n109), .B1(n118), .C1(n119), .Y(n_148) );
  nand3_1 U137 ( .A(n120), .B(n98), .C(n121), .Y(n118) );
  o21ai_0 U138 ( .A1(n94), .A2(n109), .B1(n119), .Y(n_147) );
  a21oi_1 U139 ( .A1(n112), .A2(n122), .B1(n123), .Y(n119) );
  nor2_1 U140 ( .A(n104), .B(data_0_), .Y(n_145) );
  nor2_1 U141 ( .A(n104), .B(data_2_), .Y(n_144) );
  o221ai_1 U142 ( .A1(n124), .A2(n110), .B1(n92), .B2(n109), .C1(n125), .Y(
        n_143) );
  xor2_1 U143 ( .A(n126), .B(n127), .X(n124) );
  xnor2_1 U144 ( .A(n166), .B(n128), .Y(n127) );
  o21ai_0 U145 ( .A1(n100), .A2(n109), .B1(n129), .Y(n_142) );
  o21ai_0 U146 ( .A1(n97), .A2(n109), .B1(n129), .Y(n_140) );
  inv_1 U147 ( .A(n123), .Y(n129) );
  o32ai_1 U148 ( .A1(n130), .A2(n131), .A3(n132), .B1(n133), .B2(n120), .Y(
        n123) );
  o22ai_1 U149 ( .A1(n126), .A2(n128), .B1(n134), .B2(n97), .Y(n120) );
  and2_0 U150 ( .A(n128), .B(n126), .X(n134) );
  o22ai_1 U151 ( .A1(n135), .A2(n136), .B1(n170), .B2(n137), .Y(n128) );
  and2_0 U152 ( .A(n136), .B(n135), .X(n137) );
  inv_1 U153 ( .A(n138), .Y(n135) );
  xnor2_1 U154 ( .A(n92), .B(n133), .Y(n126) );
  o221ai_1 U155 ( .A1(n122), .A2(n125), .B1(n93), .B2(n109), .C1(n139), .Y(
        n_137) );
  nand2_1 U156 ( .A(n121), .B(n140), .Y(n139) );
  xor2_1 U157 ( .A(n141), .B(n142), .X(n140) );
  xnor2_1 U158 ( .A(n94), .B(n143), .Y(n142) );
  o221ai_1 U159 ( .A1(n122), .A2(n125), .B1(n96), .B2(n109), .C1(n144), .Y(
        n_135) );
  o21ai_0 U160 ( .A1(n145), .A2(n146), .B1(n121), .Y(n144) );
  nor4_1 U161 ( .A(n131), .B(n147), .C(n148), .D(n146), .Y(n122) );
  nor2_1 U162 ( .A(n95), .B(n170), .Y(n148) );
  o221ai_1 U163 ( .A1(n149), .A2(n110), .B1(n95), .B2(n109), .C1(n125), .Y(
        n_130) );
  o21ai_0 U164 ( .A1(n131), .A2(n132), .B1(n112), .Y(n125) );
  inv_1 U165 ( .A(n130), .Y(n112) );
  nand4_1 U166 ( .A(n168), .B(n173), .C(n165), .D(n150), .Y(n130) );
  nor4_1 U167 ( .A(n176), .B(n177), .C(n151), .D(n101), .Y(n150) );
  a221oi_1 U168 ( .A1(n152), .A2(n170), .B1(n92), .B2(n166), .C1(n153), .Y(
        n132) );
  inv_1 U169 ( .A(n154), .Y(n153) );
  o21ai_0 U170 ( .A1(n152), .A2(n170), .B1(n95), .Y(n154) );
  nor2_1 U171 ( .A(n147), .B(n155), .Y(n152) );
  a21oi_1 U172 ( .A1(n93), .A2(n167), .B1(n145), .Y(n155) );
  nor2_1 U173 ( .A(n171), .B(n172), .Y(n145) );
  nor2_1 U174 ( .A(n93), .B(n167), .Y(n147) );
  nor2_1 U175 ( .A(n92), .B(n166), .Y(n131) );
  nand3_1 U176 ( .A(n116), .B(n114), .C(n165), .Y(n109) );
  nor4_1 U177 ( .A(n177), .B(n176), .C(n156), .D(n174), .Y(n114) );
  or2_0 U178 ( .A(n168), .B(n173), .X(n156) );
  xnor2_1 U179 ( .A(n136), .B(n157), .Y(n149) );
  xnor2_1 U180 ( .A(n170), .B(n138), .Y(n157) );
  o22ai_1 U181 ( .A1(n143), .A2(n141), .B1(n167), .B2(n158), .Y(n138) );
  and2_0 U182 ( .A(n141), .B(n143), .X(n158) );
  xnor2_1 U183 ( .A(n161), .B(n133), .Y(n141) );
  a21oi_1 U184 ( .A1(n133), .A2(n96), .B1(n146), .Y(n143) );
  and2_0 U185 ( .A(n171), .B(n172), .X(n146) );
  xnor2_1 U186 ( .A(n169), .B(n133), .Y(n136) );
  nand2_1 U187 ( .A(n121), .B(n173), .Y(n133) );
  inv_1 U188 ( .A(n110), .Y(n121) );
  nand4_1 U189 ( .A(n165), .B(n168), .C(n159), .D(n99), .Y(n110) );
  inv_1 U190 ( .A(n104), .Y(n10) );
  nand3_1 U191 ( .A(n177), .B(n159), .C(n160), .Y(n104) );
  nor3_1 U192 ( .A(n173), .B(n165), .C(n168), .Y(n160) );
  nor3_1 U193 ( .A(n176), .B(n174), .C(n151), .Y(n159) );
  inv_1 U194 ( .A(n116), .Y(n151) );
  nor2_1 U195 ( .A(n91), .B(n175), .Y(n116) );
endmodule
