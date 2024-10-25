run: yl

syn:
	yosys -p "read_verilog -sv ../sv_tests/synth_tests/test_sv_arr_literals.sv; hierarchy -check; proc; exit"

yl:
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_arr_literals.sv > yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_chkr.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_logic_param.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_upk_arr_assign_yosys.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_2d_arr_ports.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_20.sv >> yoyolint.log	
	cat yoyolint.log
