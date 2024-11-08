interface my_if(input logic clk);
    logic [7:0] data;
    logic valid;
endinterface

module tb_my_dut;
    logic clk;
    logic rst_n;

    my_interface inf(.clk(clk));

    initial begin
        clk = 0;
        rst_n = 1;

        forever #5 clk = ~clk;

        #10 rst_n = 0;
        #10 rst_n = 1;
    end

    initial begin
        inf.data = 8'd0;
        inf.valid = 1'b0; // Initialize valid signal

        // Wait for some cycles to see output
        repeat (10) @(posedge clk);

        // Simulate data increment
        for (int i = 0; i < 10; i++) begin
            @(posedge clk);
            inf.data <= inf.data + 8'd1;
            inf.valid <= 1'b1;

            // Display current values
          $display("Cycle %d: Data = %d, Valid = %b", i+1, inf.data, inf.valid);
        end

        $finish;
    end
endmodule
