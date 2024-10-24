run: yl

syn:
	yosys -p "read_verilog -sv ../sv_tests/synth_tests/test_sv_arr_literals.sv; hierarchy -check; proc; exit"

yl:
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_arr_literals.sv > yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_chkr.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_logic_param.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_upk_arr_assign_yosys.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_2d_arr_ports.sv >> yoyolint.log
        python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_clog_as_parameter.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_function_call_in_parameter.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_genvar_inide_for_loop.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_importing_pkg_yosys.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_int_port_yosys.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_inside_operators_in_case.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_multidimentional_parameter.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_parsing_attributes.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_pkg_import.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_straming_opearation.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_typedef_inside_package.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_upk_arr_assign_yosys.sv >> yoyolint.log
        python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_array_as_input_in_module.sv >> yoyolint.log
	python3 ../py_src/af_yoyolint.py -t ../sv_tests/synth_tests/test_sv_2d_array_in_ports_yosys.sv >> yoyolint.log
	cat yoyolint.log
