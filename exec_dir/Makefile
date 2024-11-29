run: yl

.IGNORE: syn
syn:
	yosys -p "read_verilog -sv ../sv_tests/synth_tests/test_21.sv; hierarchy -check; proc; exit" > plain_yosys_run.log
	yosys -p "read_verilog -sv ../sv_tests/synth_tests/test_sv_chkr.sv; hierarchy -check; proc; exit" >> plain_yosys_run.log
	yosys -p "read_verilog -sv ../sv_tests/synth_tests/test_sv_logic_param.sv; hierarchy -check; proc; exit" >> plain_yosys_run.log
	yosys -p "read_verilog -sv ../sv_tests/synth_tests/test_sv_upk_arr_assign_yosys.sv; hierarchy -check; proc; exit" >> plain_yosys_run.log
	yosys -p "read_verilog -sv ../sv_tests/synth_tests/test_sv_2d_arr_ports.sv; hierarchy -check; proc; exit" >> plain_yosys_run.log


yl:
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_2.sv > yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_3.sv > yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_4.sv > yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_5.sv > yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_6.sv > yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_7.sv > yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_8.sv > yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_13.sv > yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_14.sv > yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_15.sv > yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_16.sv > yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_17.sv > yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_20.sv > yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_21.sv > yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_24.sv > yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_32.sv > yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_33.sv > yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_34.sv > yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_54.sv > yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_55.sv > yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_casting.sv > yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_clog2_bit_size.sv > yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_wildcard.sv > yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_chkr.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_arr_literals.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_conc_sva_f.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_logic_param.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_2d_arr_ports.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_clog2_bit_size.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_casting.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_31.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_48.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_20.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_enum.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_enum_pass.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_interface.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_interface_p.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_pkg_import.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_streaming_op.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_upk_arr_assign_yosys.sv >> yoyolint.log
	
	cat yoyolint.log
