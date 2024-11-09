module test_endlabel_in_functions;
    // Function to test
    function automatic int add(int a, int b);
        return a + b;
endfunction : my_function_endlabel
    initial begin
        int result;

        result = add(5, 10);
        
        // Check if the result is correct
        if (result == 15) begin
            $display("Test passed: Function 'add' works correctly without endlabel.");
        end else begin
            $error("Test failed: Function 'add' does not work as expected.");
        end
        $finish;
    end
endmodule
