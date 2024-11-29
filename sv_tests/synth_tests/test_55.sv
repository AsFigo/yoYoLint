// Test Case: Passing Design Using Asynchronous Reset
// This design uses asynchronous reset to avoid timing and resource issues in FPGA designs.
module async_reset (
    input clk,      // Clock input
    input reset_n,  // Asynchronous active-low reset signal
    input a,        // Input signal
    output reg b    // Output signal
);

    // Display message to indicate simulation start
    initial begin
        $display("ASYNC_RESET_pass_design: Simulation started with asynchronous reset.");
    end

    // Always block with asynchronous reset
    always @(posedge clk or negedge reset_n) begin
        if (!reset_n) begin
            // Asynchronous reset initializes `b` immediately
            b <= 1'b0;
            $display("Asynchronous Reset Active: b initialized to 0.");
        end
        else begin
            // Normal operation, `b` follows the value of `a`
            b <= a;
            $display("Signal `a` value applied: b = %b", a);
        end
    end

endmodule

