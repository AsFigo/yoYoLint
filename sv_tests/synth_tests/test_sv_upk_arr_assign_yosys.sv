
module unpacked_array_example (
    input logic clk,
    input logic reset
);
  // Define unpacked arrays
  bit [7:0] unpacked_array_1[4];
  bit [7:0] unpacked_array_2[4];
  int a;

  always_ff @(posedge clk or posedge reset) begin
    if (reset) begin
      // Assign default values on reset
      unpacked_array_1[0] <= 0;
      unpacked_array_1[1] <= 0;
      unpacked_array_1[2] <= 0;
      unpacked_array_1[3] <= 0;

      unpacked_array_2[0] <= 0;
      unpacked_array_2[1] <= 0;
      unpacked_array_2[2] <= 0;
      unpacked_array_2[3] <= 0;
    end else begin
      // Assign values to the first unpacked array
      unpacked_array_1[0] <= 10;
      unpacked_array_1[1] <= 20;
      unpacked_array_1[2] <= 30;
      unpacked_array_1[3] <= 40;

      // Assign values to the second unpacked array using the first array
      unpacked_array_2 <= unpacked_array_1;
    end
  end
endmodule
