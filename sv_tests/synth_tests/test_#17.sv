module array_input_example #(parameter int SIZE = 2) (
    input logic [31:0] input_array [0:SIZE-1] // Array input
);

    // Initial block to display the contents of the input array
    initial begin
        for (int i = 0; i < SIZE; i++) begin
            $display("input_array[%0d] = %h", i, input_array[i]);
        end
    end

endmodule

