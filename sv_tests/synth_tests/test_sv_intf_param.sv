
interface my_interface #(parameter WIDTH = 8) (input logic clk);
    logic [WIDTH-1:0] data;
    logic             valid;

    modport master (input clk, input data, input valid);
    modport slave  (input clk, output data, inout valid);
endinterface

module top;
    logic clk;
    logic clk32;
    my_interface #(16) intf(.clk(clk)); 
    my_interface #(32) intf32 (.clk(clk32)); 

    // my_module u_my_module (.intf(intf.master)); // Connect interface modport

endmodule

