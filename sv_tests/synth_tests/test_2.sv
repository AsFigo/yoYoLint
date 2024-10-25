module MY_MODULE#(
    parameter MY_PARAM = 2,
    parameter PARAM_TWO = 10,
    localparam my_func_data = my_func(MY_PARAM, PARAM_TWO)
)(
    input logic CLK_CI,
    input logic [my_func_data:0] RND,
    output logic Finish_SO
);

function automatic int my_func(input loop_control, input variables);
    int carry;
    int variables_next = 0;
    for (int i = 0; i < loop_control; i++) begin
        carry = variables_next & 1;
        variables_next = (variables_next >> 1) + carry;
    end
    my_func = carry;
endfunction

endmodule
