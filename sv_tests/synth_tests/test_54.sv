// Test Case: Synchronous Reset - Design with Synchronized Reset Signal
// This design demonstrates the use of a synchronous reset for reliable and predictable behavior.

module sync_reset (
    input clk,        // Clock input
    input reset,      // Synchronous reset signal (active-high)
    input a,          // Input signal
    output reg b      // Output signal
);

    // Display message indicating the start of simulation
    initial begin
        $display("SYNC_RESET_pass_test: Simulation started with synchronous reset.");
    end

    // Always block with synchronized reset
    always @(posedge clk) begin
        if (reset) begin
            // Synchronous reset: output `b` is set to 0 on the rising edge of the clock when reset is high
            b <= 1'b0;
            $display("Synchronous Reset Active: b initialized to 0.");
        end
        else begin
            // Normal operation: `b` follows the value of input `a`
            b <= a;
            $display("Normal Operation: Signal `a` applied, b = %b", a);
        end
    end

endmodule

