module test_endlabel_in_functions;
    // Function to test
    function automatic int add(int a, int b);
    begin : my_function_block
        return a + b;
    end : my_function_block
endfunction : my_function_endlabel
    initial begin
        int result;
        
        // Test the function
        result = add(5, 10);
        
        // Check if the result is correct
        if (result == 15) begin
            $display("Test passed: Function 'add' works correctly without endlabel.");
        end else begin
            $error("Test failed: Function 'add' does not work as expected.");
        end
        
        // Finish the simulation
        $finish;
    end
endmodule
