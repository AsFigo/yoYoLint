
module nested_if_else (
    input  logic [3:0] a,
    input  logic [3:0] b,
    output logic [3:0] result
);
    always_comb begin
        if (a == 4'b0001) begin
            if (b == 4'b0001) begin
                if (a + b == 4'b0010) begin
                    if (b[0] == 1'b1) begin
                        result = 4'b1000;
                    end else begin
                        result = 4'b0100;
                    end
                end else begin
                    result = 4'b0010;
                end
            end else if (b == 4'b0010) begin
                if (a[1] == 1'b1) begin
                    result = 4'b0011;
                end else begin
                    result = 4'b0001;
                end
            end else begin
                result = 4'b0000;
            end
        end else begin
            result = 4'b1111;
        end
    end
endmodule



