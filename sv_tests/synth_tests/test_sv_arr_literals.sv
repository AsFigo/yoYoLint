module array_literals_example (
    input  logic clk,
    input  logic reset,
    output logic [3:0] packed_array
);

    // Internal storage for the arrays
    logic [3:0] packed_array_reg;

    parameter integer p_int = 4; 
    parameter int p_int1 = 4; 
    parameter logic [3:0] p_logic = 4'b1101; // Binary literal
    // Initialize the packed array with a literal
    localparam logic [3:0] lp_logic = 4'b1101; // Binary literal
    localparam lp_def = 4'b1101; // Binary literal
    logic [3:0] PACKED_ARRAY_INIT = 4'b1101; // Binary literal

    // Initialize the unpacked array with a literal
    bit [7:0] upk_arr_lit [3:0]; // = '{10, 20, 30, 40}; // Array literal
    //assign upk_arr_lit = '{10, 20, 30, 40}; // Array literal

    // Always block for synchronous reset and initialization
    always_ff @(posedge clk or posedge reset) begin
        if (reset) begin
            // Assign initial values to the packed array
            packed_array_reg <= PACKED_ARRAY_INIT;

        end
    end

    // Assign internal registers to the output ports
    assign packed_array = packed_array_reg;

endmodule

