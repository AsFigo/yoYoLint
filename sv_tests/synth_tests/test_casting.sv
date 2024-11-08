module test_casting_other_types;

  byte byte_var = 8'hFF;      // 8-bit unsigned integer
  shortreal shortreal_var = 1.618;  // Floating-point number
  logic [3:0] logic_var = 4'b1010;  // 4-bit logic vector
  logic [7:0] logic_result;
  real real_result;
  byte byte_result;

  initial begin
    // Static Casting: Cast byte to logic [7:0] (expands to fit the width)
    logic_result = logic [7:0]'(byte_var);
    $display("Static Cast - byte to logic[7:0]: %0d -> %0b", byte_var, logic_result);

    // Static Casting: Cast shortreal to real (compatible floating-point types)
    real_result = real'(shortreal_var);
    $display("Static Cast - shortreal to real: %0f -> %0f", shortreal_var, real_result);

    // Dynamic Casting: Safely cast logic [3:0] to byte (fits within byte range)
    if ($cast(byte_result, logic_var))
      $display("Dynamic Cast - logic[3:0] to byte: %0b -> %0d", logic_var, byte_result);
    else
      $display("Dynamic Cast - logic[3:0] to byte failed due to out-of-range value");
  end

endmodule

