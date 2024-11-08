module logic_violation;

    // Using `logic` and `int` types in parameter and localparam declarations
    parameter  [7:0] param_logic = 8'b10101010;  // Violation: logic type in parameter
    parameter  param_int = 10;                     // Violation: int type in parameter

    localparam  [3:0] local_logic = 4'b1101;     // Violation: logic type in localparam
    localparam  local_int = 5;                     // Violation: int type in localparam


endmodule

