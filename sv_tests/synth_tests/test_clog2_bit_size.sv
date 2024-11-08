module design;

  logic dynamic_value = 10;
  logic var1;
  logic single_value;
  logic array_2d[4][5];
  logic width, bits_result, size_result;

  initial begin
    width = $clog2(dynamic_value);

    bits_result = $bits(var1 + 1);

    size_result = $size(single_value);

    size_result = $size(array_2d, 2);
  end

endmodule

