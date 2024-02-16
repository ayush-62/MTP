module test_org_tb; 
 
reg	clk; 
reg	rst; 
reg	[1:0]	in; 
wire	[1:0]	out; 
 
integer	inFile, outFile; 
integer	scan, write; 
reg	rd_inputs; 
 
initial 
begin 
	clk	<= 1'b0; 
	in	<= 2'b0; 
end 
 
always 
begin 
	#10000 clk <= ~clk; 
end 
initial 
begin 
		inFile = $fopen("input.txt", "r"); 
		if(inFile == "NULL") 
		begin 
 		$display("Could not open the stimulus file");
		$finish; 
		end 
		outFile = $fopen("test_original_outputs.txt", "w");
		
end 
 
 
test_org UUT ( 
	.line1(in[0]),	
	.line2(in[1]),	
	.outp(out[0]),
	.overflw(out[1]),	
	.clock(clk), 
	.reset(rst)); 

 
 
 
initial 
begin 
		$display("\n\n>> Simulation starts here......"); 
		
		rd_inputs = 1'b0; 
		rst	= 1'b1; 
		repeat (10) 
		begin 
			@(posedge clk); 
		end 
		rst	= 1'b0; 
		rd_inputs = 1'b1; 
		
end 
 
 
always@(posedge rd_inputs) 
begin 
		$dumpfile("test.vcd");
    		$dumpvars(0,test_org_tb); 
		while(!$feof(inFile)) 
		begin 
			
			scan = $fscanf(inFile, "%2b\n", in); 
			@(posedge clk); 
			
			$fwrite(outFile, "%2b\n", out); 
		end 
		$fclose(inFile); 
		$fclose(outFile); 
		$display("\n>> Simulation ends here........\n\n"); 
		$finish; 
end 
 
endmodule 
 
