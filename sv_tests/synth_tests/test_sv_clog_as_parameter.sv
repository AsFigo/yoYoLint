module clog2_example;

  // Define the size of the memory array
  localparam int MEM_SIZE = 16; // Memory size
  localparam int ADDR_WIDTH = $clog2(MEM_SIZE); // Calculate address width

  // Memory array declaration
  logic [7:0] memory[0:MEM_SIZE-1]; // 8-bit memory with 16 entries

  // Counter
  logic [ADDR_WIDTH-1:0] counter; // Counter based on calculated width

  initial begin
    // Initialize the counter
    counter = 0;

    // Simulate writing to memory
    for (int i = 0; i < MEM_SIZE; i++) begin
      memory[i] = i; // Store values
      $display("Memory[%0d] = %0d", i, memory[i]);
    end

    // Simulate reading from memory using the counter
    for (int i = 0; i < MEM_SIZE; i++) begin
      $display("Read Memory[%0d] = %0d", counter, memory[counter]);
      counter++;
    end
  end

endmodule

