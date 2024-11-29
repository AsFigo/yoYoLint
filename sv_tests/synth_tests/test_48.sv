module reset_test;

    reg clk;
    reg rst_n;  // Active-low reset
    reg enable;
    reg [7:0] data_in;
    
    wire [7:0] data_out;
    
    flop_reset_example dut (
        .clk(clk),
        .rst_n(rst_n),
        .enable(enable),
        .data_in(data_in),
        .data_out(data_out)
    );

    initial begin
        clk = 0;
        forever #5 clk = ~clk;  // Toggle clock every 5ns
    end

    initial begin
        rst_n = 0;    // Assert reset initially
        enable = 0;
        data_in = 8'h00;
        
        // Wait some time and then release reset
        #10 rst_n = 1;  // Release reset
        #10 enable = 1;  // Enable data input
        data_in = 8'hAA; // Apply data input
        
        // Simulate data change
        #50 data_in = 8'h55;
        
        // Disable the enable, observe the result
        #10 enable = 0;  // Disable enable, should freeze the data

        // Final check for metastability, asynchronous reset behavior
        #30 $finish;
    end

    // Check for metastability or improper reset during simulation
    always @(posedge clk or negedge rst_n) begin
        if (rst_n === 1'bx) begin
            $display("Warning: Metastability detected in reset signal!");
        end
    end

endmodule

