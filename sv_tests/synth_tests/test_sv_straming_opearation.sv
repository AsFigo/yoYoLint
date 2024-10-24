module streaming_example;

  // Define a stream variable
  logic [31:0] stream_data;

  initial begin
    // Initialize the stream with some data
    stream_data = 32'hAABBCCDD;

    // Left shift to append data
    stream_data = stream_data << 8;  // Shift left by 8 bits
    stream_data[7:0] = 8'hEE;         // Append new data on the right
    $display("After left shift and append: %h", stream_data);

    // Right shift to extract data
    logic [31:0] extracted_data;
    extracted_data = stream_data >> 8; // Shift right by 8 bits
    $display("Extracted data after right shift: %h", extracted_data);

    // Concatenate two streams
    logic [15:0] stream1 = 16'h1234;
    logic [15:0] stream2 = 16'h5678;
    logic [31:0] concatenated_stream = {stream1, stream2}; // Concatenate
    $display("Concatenated stream: %h", concatenated_stream);
  end

endmodule

