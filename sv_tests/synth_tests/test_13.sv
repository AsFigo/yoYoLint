
module adder #(
parameter WIDTH = 32
)(
input logic [WIDTH-1:0] a, b,
output logic [WIDTH-1:0] result
);

always_comb begin
    result <= '{default:0};  // This line will cause the syntax error in Verilog-2005
end
endmodule


