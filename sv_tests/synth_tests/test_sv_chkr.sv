module chk (
    input  logic clk,
    input  logic reset,
    output logic [3:0] packed_array
);

    // Internal storage for the arrays
    logic [3:0] packed_array_reg;

    parameter integer p_int = 4; 
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
    checker c1;
        always_ff @(posedge clk or posedge reset) begin
            if (reset) begin
                // Do nothing on reset
            end else begin
                assert(packed_array_reg >= 4 && packed_array_reg <= 11);
                    //else $error("monitored_signal out of range: %0d", packed_array_reg);
            end
        end
    endchecker : c1
    checker range_checker(logic [3:0] signal);
        always_ff @(posedge clk or posedge reset) begin
            if (reset) begin
                // Do nothing on reset
            end else begin
                assert(signal >= 4 && signal <= 11)
                    else $error("monitored_signal out of range: %0d", signal);
            end
        end
    endchecker
endmodule // chk

