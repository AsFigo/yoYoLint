module top;

    // Define  signals
    logic clk;
    logic reset;
    logic [3:0] data_in;
    logic [3:0] data_out;

    // Instantiate the `wc_module` with explicit connections
    wc_module dut (
        .clk(clk),
        .reset(reset),
        .data_in(data_in),
        .data_out(data_out)
    );

endmodule

module wc_module (
    input logic clk,
    input logic reset,
    input logic [3:0] data_in,
    output logic [3:0] data_out
);
    // Module logic
    assign data_out = data_in;
endmodule

