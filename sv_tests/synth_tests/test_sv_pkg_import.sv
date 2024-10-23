package keymgr_pkg;
   localparam integer Shares = 2;
   localparam integer KeyWidth = 16;

   /*
   typedef struct packed {
      logic [Shares-1:0][KeyWidth-1:0] key;
   } hw_key_req_t;
   */
endpackage // keymgr_pkg

module top(output integer o);
   // keymgr_pkg::hw_key_req_t keymgr_key_i;
   // assign o = $bits(keymgr_key_i.key[0]);
   reg [keymgr_pkg::KeyWidth - 1 : 0] key;
endmodule // top
