module reset_strategy_tb;

  parameter string FPGA_FAMILY = "Xilinx"; // Options: "Xilinx", "Intel", "Lattice"
  parameter string RESET_TYPE = "synchronous"; // Options: "synchronous", "asynchronous"

  logic clk;
  logic rst;
  logic [3:0] counter;

  initial clk = 0;
  always #5 clk = ~clk;

  reset_strategy #(
    .FPGA_FAMILY(FPGA_FAMILY),
    .RESET_TYPE(RESET_TYPE)
  ) dut (
    .clk(clk),
    .rst(rst),
    .counter(counter)
  );

  initial begin
    $display("Running test for FPGA family: %s, Reset type: %s", FPGA_FAMILY, RESET_TYPE);

    if (RESET_TYPE == "asynchronous") begin
      rst = 1;
      #2; // Wait for some time during an asynchronous reset
      assert(counter == 4'b0000) else $fatal("Asynchronous reset failed for FPGA family %s", FPGA_FAMILY);
      rst = 0;
    end

    // Test synchronous reset logic
    if (RESET_TYPE == "synchronous") begin
      rst = 1;
      #2; // Check before clock edge
      assert(counter !== 4'b0000) else $fatal("Synchronous reset prematurely triggered for FPGA family %s", FPGA_FAMILY);
      @(posedge clk);
      assert(counter == 4'b0000) else $fatal("Synchronous reset failed for FPGA family %s", FPGA_FAMILY);
      rst = 0;
    end

    // Test normal operation
    repeat (5) @(posedge clk);
    assert(counter !== 4'b0000) else $fatal("Counter did not increment as expected for FPGA family %s", FPGA_FAMILY);

    $display("Test passed for FPGA family: %s, Reset type: %s", FPGA_FAMILY, RESET_TYPE);
    $finish;
  end

endmodule

