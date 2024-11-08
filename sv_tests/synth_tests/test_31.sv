module alu_ip (
  input  logic       clk,
  input  logic [2:0] sel,
  input  logic signed [7:0] A,
  input  logic signed [7:0] B,
  output logic signed [7:0] C,
  output logic              Z
);
  logic [7:0] add_sub_out;
  logic        [2:0]   sel_delay;
  logic signed [7:0] C_next;
  logic              Z_next;

  always_comb begin
    Z_next = (C == 0);
    unique case(sel_delay)
      3'b000 : C_next = {{1{add_sub_out[7]}}, add_sub_out};  // Sign-extend add_sub_out
      default: C_next = Z_next;
    endcase
  end

  always_ff @(posedge clk) begin
    C   <= C_next;
    Z   <= Z_next;
  end
endmodule

