module somename #(
     parameter WDT = 3,
     parameter CNT = 2
) (
     input [WDT-1:0] in_a [CNT-1:0],
     output [WDT-1:0] out_b [CNT-1:0]
);

initial begin
     $display("size of an array a is %0d",in_a.size);
end

endmodule
