    // Define an enum
typedef enum {RED, GREEN, BLUE} color_t;

module enum_test;

    color_t current_color;

    initial begin
        // Initialize the enum variable
        current_color = RED;

        if (current_color == RED) begin
            $display("Color is RED");
        end else begin
            $display("Color is not RED");
        end

        // Change the color and test again
        current_color = GREEN;
        
        if (current_color == GREEN) begin
            $display("Color is GREEN");
        end else begin
            $display("Color is not GREEN");
        end

        // Change the color one last time and test again
        current_color = BLUE;
        
        if (current_color == BLUE) begin
            $display("Color is BLUE");
        end else begin
            $display("Color is not BLUE");
        end

        // Finish simulation after testing
        #10ns;
        $finish;
    end
endmodule
