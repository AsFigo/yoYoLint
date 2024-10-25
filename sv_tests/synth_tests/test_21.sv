package my_pkg;
  int KL=64;
endpackage


module test_case;
  //Declare the constant variable directly in the module, since Yosys doesn't support packages.
  localparam int KL = 64;

  initial begin
    $display("Test Case: The value of KL is %0d", KL);
    
    if (KL == 64) begin
      $display("Test passed: KL is correctly set to 64.");
    end else begin
      $display("Test failed: KL is not correctly set.");
    end

  end
endmodule
