// Declare the struct outside the module
typedef struct packed {
    logic first;
    logic second;
    logic third;
    logic fourth;
} my_struct_t;

module top(output [3:0] b);
    my_struct_t a;

    // Assign each bit of output b to the struct fields
    assign b = {a.fourth, a.third, a.second, a.first};

   initial
       begin

	$monitor("a.fourth = %b, a.third = %b, a.second = %b, a.first = %b", 
                    a.fourth, a.third, a.second, a.first);
        a.first = 0;
        a.second = 0;
        a.third = 0;
        a.fourth = 0;

       #10;
        a.first = 1;
        a.second = 0;
        a.third = 0;
        a.fourth = 0;
        #10;   
       $finish;	
      end



endmodule
