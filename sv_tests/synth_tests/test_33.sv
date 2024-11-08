// Define the enum type outside the module to avoid synthesis issues
typedef enum logic [1:0] {EMPTY, PARTIAL, FULL} state_t;

module skid_buffer #(parameter WIDTH = 8)(
  input  logic clk, rstn, s_valid, m_ready,
  input  logic [WIDTH-1:0] s_data,
  output logic [WIDTH-1:0] m_data,
  output logic m_valid, s_ready
);
  // Use the typedef-defined enum type
  state_t state, state_next;

endmodule

