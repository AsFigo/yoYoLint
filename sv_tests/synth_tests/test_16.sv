module m;
  
  // Parameter definition for an array of 32-bit logic values
  parameter logic [31:0] CHIPS [0:1] = '{
    32'h6077AE6C,
    32'h4E077AE6
  };

  // Initial block to display the values of CHIPS
  initial begin
    for (int i = 0; i < 2; i++) begin
      $display("CHIPS[%0d] = %h", i, CHIPS[i]);
    end
  end

endmodule


