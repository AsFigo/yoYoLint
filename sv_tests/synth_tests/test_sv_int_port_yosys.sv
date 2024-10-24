module top(output int a, b, c, d);

initial begin 
	a= 'h2;
	b= 'h3;
	c= 'h4;
	d= 'h5;

	$display("values of a b c d are %0d %0d %0d %0d"a,b,c,d);
end

endmodule
