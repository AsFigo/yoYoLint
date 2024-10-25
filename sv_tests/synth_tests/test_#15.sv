module test (clk, reset, in_value, out_value);

input clk, reset;
input [1:0] in_value;
output reg [1:0] out_value;

always @(posedge clk)
begin
if(reset) out_value <= 0;
else begin
// https://www.xilinx.com/support/answers/64777.html
case(in_value) inside
 0,1: out_value <= 3;
 2,3 : out_value <= 2;
default : out_value <= 1;
endcase
end
end
endmodule
