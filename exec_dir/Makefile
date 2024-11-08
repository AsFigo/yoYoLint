run: yl

syn:
	yosys -p "read_verilog -sv ../sv_tests/synth_tests/test_21.sv; hierarchy -check; proc; exit"

yl:
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_24.sv > yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_21.sv > yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_chkr.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_logic_param.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_upk_arr_assign_yosys.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_2d_arr_ports.sv >> yoyolint.log
 
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_clog2_bit_size.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_casting.sv >> yoyolint.log
 
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_20.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_enum.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_enum_pass.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_interface.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_interface_p.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_literal_enhancement.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_enhancement_operator.sv >> yoyolint.log
	cat yoyolint.log
