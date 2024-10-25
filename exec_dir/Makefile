run: yl

syn:
	yosys -p "read_verilog -sv ../sv_tests/synth_tests/test_sv_arr_literals.sv; hierarchy -check; proc; exit"

yl:
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_arr_literals.sv > yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_chkr.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_logic_param.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_upk_arr_assign_yosys.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_2d_arr_ports.sv >> yoyolint.log
        python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_17.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_16.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_15.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_14.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_13.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_8.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_7.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_6.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_5.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_4.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_3.sv >> yoyolint.log
        python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_2.sv >> yoyolint.log
	cat yoyolint.log
