module counter_wrapper(
	input  logic board_clk, rst, incr,
	output logic [3:0] count_reg
);
    
	wire clk;
	
	// Changed from implicit (.*) to explicit port connections for compatibility
	counter #(.WIDTH(4)) Counter_1 (
		.clk(clk),
		.rst(rst),
		.incr(incr),
		.count(count_reg)
	);

	divider #(.FREQ(1)) Divider_1 (
		.board_clk(board_clk),
		.out_clk(clk)
	); 
    
endmodule

