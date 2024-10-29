module my_design (
    input logic clk,
    input logic reset,
    input logic in,
    output logic out
);

    // Struct definition inside the module
    typedef struct {
        logic in_val;   // Input value
        logic out_val;  // Output value
    } data_t;

    // Declare a variable of the struct type
    data_t data;

    // Always block for synchronous logic
    always_ff @(posedge clk or posedge reset) begin
        if (reset) begin
            data.out_val <= 1'b0; // Reset output
        end else begin
            data.in_val <= in;    // Capture input
            data.out_val <= data.in_val; // Update output
        end
    end

    // Assign the output from the struct
    assign out = data.out_val;

endmodule

