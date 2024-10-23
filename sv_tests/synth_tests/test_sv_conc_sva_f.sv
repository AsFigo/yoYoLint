module array_literals_example (
    input  logic clk,
    input  logic reset,
    output logic [3:0] packed_array
);

    // Internal storage for the arrays
    logic [3:0] packed_array_reg;

    logic [3:0] PACKED_ARRAY_INIT = 4'b1101; // Binary literal

    always_ff @(posedge clk or posedge reset) begin
        if (reset) begin
            // Assign initial values to the packed array
            packed_array_reg <= PACKED_ARRAY_INIT;

        end
    end

    // Assign internal registers to the output ports
    assign packed_array = packed_array_reg;
    a1 : assert property (packed_array_reg != 0);

endmodule

