 `timescale 1ns / 1ps

`define NULL 0 
 
module org_tb; 
 
reg	clk; 
reg	rst; 
reg	[9:0]	in; 
reg	[19:0] clk_count; 
wire	[8:0]	out; 
 
integer	inFile, outFile1, outFile2, outFile3; 
integer scan1; 
integer	scan, write; 
reg	rd_inputs; 
 
initial 
begin 
	clk	<= 1'b0; 
	clk_count	<= 20'd16; 
	in	<= 10'b0; 
end 
 
always 
begin 
	#10000 clk <= ~clk; 
end 
initial 
begin 
		inFile = $fopen("example_original_inputs.txt", "r"); 
		if(inFile == `NULL) 
		begin 
 		$display("Could not open the stimulus file");
		$finish; 
		end
		outFile2 = $fopen("example_original_outputs.txt", "w");
end 
 
toy UUT ( 
	.datain(in[7:0]),	
	.op(in[9:8]),	
	.dataout(out[7:0]),	
	.valid(out[8]),	
	.clk(clk), 
	.rst(rst)); 
 
 
 
initial 
begin 
		rd_inputs = 1'b0; 
		rst	= 1'b0; 
		repeat (10) 
		begin 
			@(posedge clk);  
		end 
		rst	= 1'b1; 
		rd_inputs = 1'b1; 
		clk_count <= clk_count + 20'd1; 
end 
 
 
always@(posedge rd_inputs) 
begin 
		while(!$feof(inFile)) 
		begin 
			scan = $fscanf(inFile, "%10b\n", in); 
			@(posedge clk); 
			clk_count <= clk_count + 20'd1; 
			$fwrite(outFile2, "%9b\n", out); 
		end 
		$fclose(inFile); 
		$fclose(outFile2);
		$finish; 
end 
 
endmodule 
 
