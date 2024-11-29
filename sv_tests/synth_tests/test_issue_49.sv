module tb;
bit clk;
bit enable;
bit out;
bit a;

always #clk = ~ clk;
  
always @(posedge clk);
begin
if (enable)
        out = a;
    else
        out - ~a;
end
  initial begin
          enable <=0;
          a <=0;
          #1;
         enable <=1;
         a <= 0;
         #1;
         a <= 1;
  end
  initial begin
         $monitor("enable= %0d,a=%0d,out=%0d",enable,a,out);
        #50;
         $finish;
 end
endmodule
