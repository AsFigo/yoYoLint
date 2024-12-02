run: yl

syn:
	yosys -p "read_verilog -sv ../sv_tests/synth_tests/test_sv_arr_literals.sv; hierarchy -check; proc; exit"

yl:     
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_53.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_56.sv >> yoyolint.log
	cat yoyolint.log
