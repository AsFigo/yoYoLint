module reset_strategy_tb;

  // Parameters for FPGA family
  parameter string FPGA_FAMILY = "Xilinx"; 

  logic clk;
  logic rst;
  logic [3:0] counter;

  initial clk = 0;
  always #5 clk = ~clk;

  reset_strategy #(
    .FPGA_FAMILY(FPGA_FAMILY)
  ) dut (
    .clk(clk),
    .rst(rst),
    .counter(counter)
  );

  initial begin
    $display("Starting reset strategy test for FPGA family: %s", FPGA_FAMILY);
    rst = 1; 
    #10;     

    if (counter !== 4'b0000) begin
      $error("Counter did not reset properly for FPGA family %s", FPGA_FAMILY);
    end else begin
      $display("Reset behavior correct for FPGA family %s", FPGA_FAMILY);
    end

    rst = 0;
    #10;

    repeat (10) @(posedge clk);
    if (counter === 4'b0000) begin
      $error("Counter did not increment as expected for FPGA family %s", FPGA_FAMILY);
    end else begin
      $display("Normal operation verified for FPGA family %s", FPGA_FAMILY);
    end

    $finish;
  end

endmodule

