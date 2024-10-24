// my_package.sv
package my_package;

  // Define a typedef for a structure
  typedef struct {
    logic [7:0] data;   // 8-bit data
    logic valid;        // Valid signal
    logic [3:0] addr;   // 4-bit address
  } my_data_t;

endpackage

// my_module.sv
`include "my_package.sv"

module my_module;

  // Use the typedef from the package
  my_package::my_data_t my_data;

  initial begin
    // Initialize the structure
    my_data.data = 8'hFF;  // Set data to 255
    my_data.valid = 1'b1;   // Set valid to true
    my_data.addr = 4'b1010; // Set address to 10

    // Display the values
    $display("Data: %h, Valid: %b, Address: %b", my_data.data, my_data.valid, my_data.addr);
  end

endmodule

