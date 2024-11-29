
// Saanvi - adding test for issue #33 
module skid_buffer #(parameter WIDTH = 8)(
  input  logic clk, rstn, s_valid, m_ready,
  input  logic [WIDTH-1:0] s_data,
  output logic [WIDTH-1:0] m_data,
  output logic m_valid, s_ready
);
  bit b1;

endmodule