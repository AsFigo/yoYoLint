# ----------------------------------------------------
# SPDX-FileCopyrightText: Ajeetha Kumari Venkatesan
#                         AsFigo Technologies, UK
# SPDX-License-Identifier: MIT
# ----------------------------------------------------

import pyslang
import argparse
import tomli
import os.path
import copy
import functools
from operator import countOf
import operator as op

print_verbose = False
enabled_l = list()
disabled_l = list()

def yylUpdateRIDs():
  lvYylRIDli = list()
  lvYylRIDli.append('LOGIC_PARAM_NYS')
  lvYylRIDli.append('INT_PARAM_NYS')
  lvYylRIDli.append('INT_TYPE_NYS')
  lvYylRIDli.append('NO_PORTS_IN_CHECKER')
  lvYylRIDli.append('NO_ENDLABEL_IN_CHECKER')
  lvYylRIDli.append('NAME_INTF_SUFFIX')
  lvYylRIDli.append('NAME_PROP_PREFIX')
  lvYylRIDli.append('NAME_AST_PREFIX')
  lvYylRIDli.append('NAME_ASM_PREFIX')
  lvYylRIDli.append('NAME_COV_PREFIX')
  lvYylRIDli.append('FUNC_SVA_MISSING_FAIL_AB')
  lvYylRIDli.append('DBG_SVA_MISSING_LABEL')
  lvYylRIDli.append('DBG_SVA_MISSING_ENDLABEL')
  lvYylRIDli.append ('DBG_SVA_AST_MISSING_LABEL')
  lvYylRIDli.append ('DBG_SVA_ASM_MISSING_LABEL')
  lvYylRIDli.append ('DBG_SVA_COV_MISSING_LABEL')


def yYLRenabled(rule_id):
  return True

def yYLMsg(rule_id, msg):
  if (yYLRenabled(rule_id)):
    lvYylStr = 'yoYoLint: Violation: ['
    lvYylStr += rule_id
    lvYylStr += ']: '
    lvYylStr += msg 
    print(lvYylStr)


def DBG_SVA_AST_MISSING_LABEL(lv_m):
  if (lv_m.kind.name == 'ConcurrentAssertionMember'):
    lv_sva_vdir = lv_m.statement.keyword.valueText
    if (lv_sva_vdir != 'assert'):
      return
    if (lv_m.statement.label is None):
      msg = 'Unnamed assertion - use a meaningful label: ' 
      msg += str(lv_m.statement)
      lvRID = 'DBG_SVA_AST_MISSING_LABEL'
      yYLMsg (lvRID, msg)

def NAME_AST_PREFIX (lv_m):

  if (lv_m.kind.name == 'ConcurrentAssertionMember'):

    lv_sva_vdir = lv_m.statement.keyword.valueText
    if (lv_sva_vdir != 'assert'):
      return

    if (lv_m.statement.label is None):
      return

    lv_label = lv_m.statement.label.name.value

    lv_exp_s = sv_prefix_d['assert']
    if (not lv_label.startswith(lv_exp_s)):
      msg = 'Improper naming of assert directive: ' 
      msg += lv_label
      msg += ': expected prefix: '
      msg += lv_exp_s
      lvRID = 'NAME_AST_PREFIX'
      yYLMsg (lvRID, msg)


def NAME_ASM_PREFIX(lv_m):
  if (lv_m.kind.name == 'ConcurrentAssertionMember'):
    if (lv_m.statement.label is None):
      msg = 'Unnamed assumption - use a meaningful label: ' 
      msg += str(lv_m.statement)
      lvRID = "DBG_SVA_MISSING_LABEL"
      yYLMsg(lvRID, msg)
    else:
      lv_label = lv_m.statement.label.name.value
      lv_sva_vdir = lv_m.statement.keyword.valueText
      if (lv_sva_vdir != 'assume'):
        return

      lv_exp_s = sv_prefix_d['assume']
      if (not lv_label.startswith(lv_exp_s)):
        msg = 'Improper naming of assume directive: ' 
        msg += lv_label
        msg += ': expected prefix: '
        msg += lv_exp_s
        lvRID = 'NAME_ASM_PREFIX'
        yYLMsg(lvRID, msg)


def yoyol_argparse():
  # Create the parser
  parser = argparse.ArgumentParser()
  # Add an argument
  parser.add_argument('-t', '--test', type=str, required=True)
  # Parse the argument
  args = parser.parse_args()
  return args

def yoyol_update_prefixes():
  lv_sv_prefix_d = {}
  lv_sv_prefix_d.update({"prop": "p_"})
  lv_sv_prefix_d.update({"cover": "c_"})
  lv_sv_prefix_d.update({"assert": "a_"})
  lv_sv_prefix_d.update({"assume": "m_"})
  return lv_sv_prefix_d

def yoyol_update_suffixes():
  lv_sv_suffix_d = {}
  lv_sv_suffix_d.update({"intf": "_if"})
  lv_sv_suffix_d.update({"class": "_c"})
  lv_sv_suffix_d.update({"cnst": "_cst"})
  lv_sv_suffix_d.update({"mod": "_m"})
  return lv_sv_suffix_d

def chk_name_style_prefix(lvRID, lv_name, lv_exp_p):
  if (lv_name.startswith(lv_exp_p)):
    if (print_verbose):
      print('AF: Good naming: ', lv_name)
  else:
    msg = 'Improper naming of identifier: ' 
    msg += lv_name
    msg += ': expected prefix: '
    msg += lv_exp_p
    yYLMsg(lvRID, msg)

def chk_name_style_suffix(lvRID, lv_name, lv_exp_s):
  if (lv_name.endswith(lv_exp_s)): 
    if (print_verbose):
      print('AF: Good naming: ', lv_name)
  else:
    msg = 'Improper naming of identifier: ' 
    msg += lv_name
    msg += ': expected suffix: '
    msg += lv_exp_s
    yYLMsg(lvRID, msg)

def FUNC_NO_2STATE_IN_INTF(lv_intf_scope):
  for lv_intf_mem_i in lv_intf_scope.members:
    if (lv_intf_mem_i.kind.name == 'DataDeclaration'):
      if (lv_intf_mem_i.type.kind.name == 'BitType'):
        lv_var_decl = lv_intf_mem_i.declarators.getFirstToken()
        lv_name = lv_var_decl.valueText
        msg = 'Potential DUT bug hiding construct in use: '
        msg += ' Inside SystemVerilog interface, it is recommended'
        msg += ' to use only 4-state signals/nets.'
        msg += ' Found a 2-state declaration as: '
        msg += lv_intf_mem_i.__str__()
        lvRID = 'FUNC_NO_2STATE_IN_INTF'
        yYLMsg(lvRID, msg)

af_dpi_method_l = list()

def af_dpi_collect_info(lv_dpi_m):
  lv_dpi_d = {}
  lv_dpi_d['name'] = lv_dpi_m.name.__str__().strip()
  lv_dpi_d['type'] = lv_dpi_m.functionOrTask.__str__().strip()
  af_dpi_method_l.append(lv_dpi_d.copy())

def FUNC_DPI_FN_MISSING_RTYPE(lv_dpi_m):
  if (not hasattr(lv_dpi_m, 'method')):
    return

  if (hasattr(lv_dpi_m, 'property')):
    return

  if (str(lv_dpi_m.method.keyword).strip() == 'task'):
    return

  lv_code_s = lv_dpi_m.__str__()
  if (lv_dpi_m.method.returnType.kind.name == 'ImplicitType'):
    msg = 'DPI import functions should specify \n'
    msg += '\t return type as per LRM.'
    msg += ' Using Implicit return type (of logic) can lead to \n'
    msg += '\t functional issues leading to unexpected results. Please specify'
    msg += ' return type as void/bit etc. \n'
    msg += '\t Preferably use 2-state type. \n'
    msg += lv_code_s
    lvRID = 'FUNC_DPI_FN_MISSING_RTYPE'
    yYLMsg(lvRID, msg)

def COMPAT_DPI_NO_PURE_TASK(lv_dpi_m):
  if (not hasattr(lv_dpi_m, 'method')):
    return
  if (str(lv_dpi_m.method.keyword).strip() == 'task'):
    return
  if (str(lv_dpi_m.property).strip() == 'pure'):
    lv_code_s = lv_dpi_m.__str__()
    msg = 'DPI import tasks can not be delcared as \"pure\"'
    msg += ' as per LRM IEEE 1800.'
    msg += '\n\tWhile some tools do compile this, others do not. '
    msg += 'To avoid compatibility issues, please remove '
    msg += '\"pure\" keyword.'
    msg += '\n\tFound code as: \n'
    msg += lv_code_s
    lvRID = 'COMPAT_DPI_NO_PURE_TASK'
    yYLMsg(lvRID, msg)

def FUNC_DPI_NO_4STATE_IN_RETURN(lv_dpi_mem):
  if (not hasattr(lv_dpi_mem, 'method')):
    return
  if (not hasattr(lv_dpi_mem.method.returnType, 'keyword')):
    return

  lv_rval_type_s = lv_dpi_mem.method.returnType.keyword.__str__().strip()
  lv_rval_4st_types = ["integer", "logic",
                    "reg"]
  if any([x in lv_rval_type_s for x in lv_rval_4st_types]):
    msg = 'DPI functions shall use 2-state types in return value.'
    msg += ' Using 4-state type can lead to unnecessary complication'
    msg += ' as C-side does not naturally support 4-state value system'
    msg += ' Found code as: \n'
    msg += str(lv_dpi_mem)
    lvRID = 'FUNC_DPI_NO_4STATE_IN_RETURN'
    yYLMsg(lvRID, msg)


def FUNC_DPI_NO_4STATE_IN_ARGS(lv_dpi_mem):
  if(not hasattr(lv_dpi_mem, 'method')):
    return
  if (lv_dpi_mem.method.portList is None):
    return
  for lv_dpi_args_i in lv_dpi_mem.method.portList:
    if (lv_dpi_args_i.kind.name == 'SeparatedList'):
      for lv_dpi_ports_i in lv_dpi_args_i:
        if (lv_dpi_ports_i.kind.name != 'Comma'):
          lv_rval_type_s = lv_dpi_ports_i.dataType.__str__().strip()
          lv_rval_4st_types = ["integer", "logic",
                    "reg", "None"]
          if any([x in lv_rval_type_s for x in lv_rval_4st_types]):
            msg = 'DPI functions shall use arguments of 2-state types.\n'
            msg += '\t Using 4-state type can lead to unnecessary complications\n'
            msg += '\t as C-side does not naturally support 4-state value system'
            msg += str(lv_dpi_mem)
            lvRID = 'FUNC_DPI_NO_4STATE_IN_ARGS'
            yYLMsg(lvRID, msg)



def COMPAT_DPI_NO_MDA(lv_dpi_mem):
  if(not hasattr(lv_dpi_mem, 'method')):
    return
  if (lv_dpi_mem.method.portList is None):
    return

  for lv_dpi_args_i in lv_dpi_mem.method.portList:
    if (lv_dpi_args_i.kind.name == 'SeparatedList'):
      for lv_dpi_ports_i in lv_dpi_args_i:
        if (lv_dpi_ports_i.kind.name != 'Comma'):
          lv_dpi_arg_dim_s = lv_dpi_ports_i.declarator.dimensions.__str__().strip()
          if (op.countOf(lv_dpi_arg_dim_s, "[") > 1):
            msg = 'DPI method with Multi-Dimensional Array as arguments'
            msg += ' was found. \n\tWhile LRM allows this, some tools do not'
            msg += ' fully support. To avoid compatibility issues, \n'
            msg += '\tplease remodel the code:'
            msg += str(lv_dpi_mem)
            lvRID = 'COMPAT_DPI_NO_MDA'
            yYLMsg(lvRID, msg)



def COMPAT_DPI_OLD_SPECSTR(lv_dpi_mem):
  lv_spec_str_val_s = lv_dpi_mem.specString.__str__().strip()
  if (lv_spec_str_val_s != '\"DPI-C\"'):
    msg = 'Wrong Spec-STR in DPI declaration'
    msg += ' IEEE 1800-2012 specifies \"DPI-C\" as Spec-STR.'
    msg += ' Found code as: \n'
    msg += str(lv_dpi_mem)
    lvRID = 'COMPAT_DPI_OLD_SPECSTR'
    yYLMsg(lvRID, msg)



# https://verificationacademy.com/forums/systemverilog/function-arguments-not-initializing-variable-inside-body#reply-54684
def FUNC_NO_INIT_OF_STATIC_VAR_IN_SFN(lvCuScp):
  if (lvCuScp.kind.name == 'ModuleDeclaration'):
    for lv_mod_mem_i in lvCuScp.members:
      if (lv_mod_mem_i.kind.name == 'FunctionDeclaration'):
        lv_fn_name = str(lv_mod_mem_i.prototype.name)
        if (str(lv_mod_mem_i.prototype.lifetime).strip() == 'automatic'):
          lv_fn_is_auto = True
          continue

        for lv_fn_items_i in lv_mod_mem_i.items:
          if (lv_fn_items_i.kind.name == 'DataDeclaration'):
            lv_var_lt_static = True


            lv_var_lifetime = str(lv_fn_items_i.modifiers).strip()
            if (lv_var_lifetime == 'automatic'):
              lv_var_lt_static = False

            for lvDecl_i in lv_fn_items_i.declarators:
              if ((lvDecl_i.initializer is not None) and
                  (lv_var_lt_static)):
                lv_code_s = str(lv_fn_items_i)
                msg = 'A static function has a variable declaration \n'
                msg += '\t with initialization. In most cases this code will'
                msg += ' likely behave unexpected manner functionally.\n'
                msg += ' \t This is due to the fact that'
                msg += ' initialization of static variables happens'
                msg += ' before time 0,\n'
                msg += '\t not when calling the function.'
                msg += '\t Please remove the initialization\n'
                msg += lv_code_s
                lvRID = 'FUNC_NO_INIT_OF_STATIC_VAR_IN_SFN'
                yYLMsg(lvRID, msg)

# https://verificationacademy.com/forums/systemverilog/function-arguments-not-initializing-variable-inside-body#reply-54684
def COMPAT_VAR_DINIT_IN_SFN(lvCuScp):
  if (lvCuScp.kind.name == 'ModuleDeclaration'):
    for lv_mod_mem_i in lvCuScp.members:
      if (lv_mod_mem_i.kind.name == 'FunctionDeclaration'):
        lv_fn_name = str(lv_mod_mem_i.prototype.name)
        if (str(lv_mod_mem_i.prototype.lifetime).strip() == 'automatic'):
          lv_fn_is_auto = True
          continue

        for lv_fn_items_i in lv_mod_mem_i.items:
          if (lv_fn_items_i.kind.name == 'DataDeclaration'):
            lv_var_lt_def = True


            lv_var_lifetime = str(lv_fn_items_i.modifiers).strip()
            if ((lv_var_lifetime == 'automatic') or
                (lv_var_lifetime == 'static')):
              lv_var_lt_def = False

            for lvDecl_i in lv_fn_items_i.declarators:
              if ((lvDecl_i.initializer is not None) and
                  (lv_var_lt_def)):
                lv_code_s = str(lv_fn_items_i)
                msg = 'A static function has a variable declaration \n'
                msg += '\t with initialization. LRM 1800 mandates that'
                msg += ' lifetime of such variables be specified \n'
                msg += '\t explicitly and not use the default' 
                msg += ' lifetime (static).\n'
                msg += '\t Though some tools do compile this code,'
                msg += ' others do NOT (and LRM compliant). \n'
                msg += '\t To maximize compatibility across tools,'
                msg += ' Please remove the initialization\n'
                msg += '\t or add an explicit lifetime for this variable.'
                msg += lv_code_s
                lvRID = 'COMPAT_VAR_DINIT_IN_SFN'
                yYLMsg(lvRID, msg)

def DBG_AVOID_BEGIN_IN_FN(lvCuScp):
  if (lvCuScp.kind.name == 'ModuleDeclaration'):
    for lv_mod_mem_i in lvCuScp.members:
      if (lv_mod_mem_i.kind.name == 'FunctionDeclaration'):
        for lv_fn_items_i in lv_mod_mem_i.items:
          if (lv_fn_items_i.kind.name == 'SequentialBlockStatement'):
            lv_code_s = str(lv_mod_mem_i.prototype)
            msg = 'A function with begin..end was found.\n'
            msg += '\t This is likely a legacy Verilog coding syle as SystemVerilog \n'
            msg += '\t makes this optional and it is recommended'
            msg += ' coding style to avoid begin..end \n'
            msg += '\t inside function to improve readability and'
            msg += ' maintainability of codebase.\n'
            msg += '\t Please remove the redundant begin..end \n'
            msg += lv_code_s
            lvRID = 'DBG_AVOID_BEGIN_IN_FN'
            yYLMsg(lvRID, msg)



def REUSE_NO_TDEF_IN_MOD(lvCuScp):
  if (lvCuScp.kind.name == 'ModuleDeclaration'):
    for lv_mod_mem_i in lvCuScp.members:
      if (lv_mod_mem_i.kind.name == 'TypedefDeclaration'):
        lv_tdef_s = lv_mod_mem_i.__str__() 
        msg = 'A typedef was found inside a module'
        msg += ' This prevents reuse as the enum/typedef scope is module only'
        msg += ' An assertion model that binds to this module'
        msg += ' and check the states using the typedef will be harder'
        msg += ' to implement in such cases.'
        msg += ' Please move the typedef to a package'
        msg += ' and import that package inside the module'
        msg += str(lv_tdef_s)
        lvRID = 'REUSE_NO_TDEF_IN_MOD'
        yYLMsg(lvRID, msg)


mod_count = []

def REUSE_ONE_MOD_PER_FILE (lv_m):
  if (lv_m.kind.name == 'ModuleDeclaration'):
    for mod_rep in lv_m.header:
      if (mod_rep.kind.name == 'ModuleKeyword'):
        mod_count.append(mod_rep.kind.name)
        continue
      elif len(mod_count) > 1:
        msg = 'Always use one-module definition per file'
        lvRID = 'REUSE_ONE_MOD_PER_FILE'
        yYLMsg (lvRID, msg)
        break

def chk_dpi_rules_common(lv_dpi_scope):
  COMPAT_DPI_OLD_SPECSTR (lv_dpi_scope)
  COMPAT_DPI_NO_PURE_TASK(lv_dpi_scope)
  COMPAT_DPI_NO_MDA(lv_dpi_scope)
  FUNC_DPI_NO_4STATE_IN_RETURN (lv_dpi_scope)
  FUNC_DPI_NO_4STATE_IN_ARGS (lv_dpi_scope)
  FUNC_DPI_FN_MISSING_RTYPE(lv_dpi_scope)

def chk_dpi_rules(lvCuScp):
  if (lvCuScp.kind.name == 'DPIExport'):
    chk_dpi_rules_common(lvCuScp)
  if (lvCuScp.kind.name == 'DPIImport'):
    chk_dpi_rules_common(lvCuScp)

  if (lvCuScp.kind.name == 'ModuleDeclaration'):
    for lv_mod_mem_i in lvCuScp.members:
      if (lv_mod_mem_i.kind.name == 'DPIExport'):
        chk_dpi_rules_common(lv_mod_mem_i)
      if (lv_mod_mem_i.kind.name == 'DPIImport'):
        chk_dpi_rules_common(lv_mod_mem_i)

  if (lvCuScp.kind.name == 'InterfaceDeclaration'):
    for lv_if_mem_i in lvCuScp.members:
      if (lv_if_mem_i.kind.name == 'DPIExport'):
        chk_dpi_rules_common(lv_if_mem_i)
      if (lv_if_mem_i.kind.name == 'DPIImport'):
        chk_dpi_rules_common(lv_if_mem_i)

  if (lvCuScp.kind.name == 'PackageDeclaration'):
    for lv_pkg_mem_i in lvCuScp.members:
      if (lv_pkg_mem_i.kind.name == 'DPIExport'):
        chk_dpi_rules_common(lv_pkg_mem_i)
      if (lv_pkg_mem_i.kind.name == 'DPIImport'):
        chk_dpi_rules_common(lv_pkg_mem_i)


def chk_naming(lvCuScp):

  if (lvCuScp.kind.name == 'InterfaceDeclaration'):
    lv_ident_name = str(lvCuScp.header.name)
    lv_exp_s = sv_suffix_d['intf']
    chk_name_style_suffix ('NAME_INTF_SUFFIX', lv_ident_name, lv_exp_s)
    FUNC_NO_2STATE_IN_INTF(lvCuScp)

def INT_TYPE_NYS(lvDecl):
  if (lvDecl.kind.name == 'DataDeclaration'):
    lvRID = 'INT_TYPE_NYS'
    lv_dt_s = str(lvDecl.type).strip()
    if (lv_dt_s == 'int'):
      msg = 'SystemVerilog int data type is '
      msg += 'NYS - Not Yet Supported in Yosys'
      msg += str(lvDecl)
      yYLMsg (lvRID, msg)

def LOGIC_PARAM_NYS(lvDecl):
  if (lvDecl.kind.name == 'ParameterDeclarationStatement'):
    lvRID = 'LOGIC_PARAM_NYS'
    lv_dt_s = str(lvDecl.parameter.type).strip()
    if ('logic' in lv_dt_s):
      msg = 'SystemVerilog parameter of type logic is '
      msg += 'NYS - Not Yet Supported in Yosys'
      msg += str(lvDecl)
      yYLMsg (lvRID, msg)

def INT_PARAM_NYS(lvDecl):
  if (lvDecl.kind.name == 'ParameterDeclarationStatement'):
    lvRID = 'INT_PARAM_NYS'
    lv_dt_s = str(lvDecl.parameter.type).strip()
    if (lv_dt_s == 'int'):
      msg = 'SystemVerilog parameter of type int is '
      msg += 'NYS - Not Yet Supported in Yosys'
      msg += str(lvDecl)
      yYLMsg (lvRID, msg)

def yyLModuleLint(lvCuScp):
  REUSE_NO_TDEF_IN_MOD(lvCuScp)
  REUSE_ONE_MOD_PER_FILE(lvCuScp)
  if (lvCuScp.kind.name == 'ModuleDeclaration'):
    for lv_mod_mem_i in lvCuScp.members:
      LOGIC_PARAM_NYS(lv_mod_mem_i)
      INT_PARAM_NYS(lv_mod_mem_i)
      INT_TYPE_NYS(lv_mod_mem_i)
      yyLChkrLint(lv_mod_mem_i)

def NO_PORTS_IN_CHECKER(lvChkrScope):
  if (lvChkrScope.portList is not None):
    lvRID = 'NO_PORTS_IN_CHECKER'
    msg = 'SystemVerilog checker with ports is '
    msg += 'NYS - Not Yet Supported in Yosys'
    msg += str(lvChkrScope)
    yYLMsg (lvRID, msg)

def NO_ENDLABEL_IN_CHECKER(lvChkrScope):
  if (lvChkrScope.endBlockName is not None):
    lvRID = 'NO_ENDLABEL_IN_CHECKER'
    msg = 'SystemVerilog checker with end-label is '
    msg += 'NYS - Not Yet Supported in Yosys'
    msg += str(lvChkrScope.endBlockName)
    yYLMsg (lvRID, msg)


def yyLChkrLint(lvCuScp):
  if (lvCuScp.kind.name == 'CheckerDeclaration'):
    NO_PORTS_IN_CHECKER(lvCuScp)
    NO_ENDLABEL_IN_CHECKER(lvCuScp)

args = yoyol_argparse()

sv_prefix_d = yoyol_update_prefixes()
sv_suffix_d = yoyol_update_suffixes()
yoyol_rules_l = yylUpdateRIDs()

inp_test_name = args.test

tree = pyslang.SyntaxTree.fromFile(inp_test_name)
r = tree.root

if (tree.root.members.__str__() == ''):
  print("YoYoLint: No modules/interfaces/ found")
  exit(0)

for scope_i in (tree.root.members):
  chk_naming(scope_i)
  chk_dpi_rules(scope_i)
  yyLModuleLint(scope_i)
  yyLChkrLint(scope_i)

  DBG_AVOID_BEGIN_IN_FN(scope_i)
  FUNC_NO_INIT_OF_STATIC_VAR_IN_SFN(scope_i)
  COMPAT_VAR_DINIT_IN_SFN(scope_i)

cu_scope = tree.root.members[0]
if (cu_scope.kind.name != 'ClassDeclaration'):
  if (hasattr(cu_scope, 'members')):
    for m_i in (cu_scope.members):
      NAME_AST_PREFIX(m_i)
      NAME_ASM_PREFIX(m_i)
      #NAME_COV_PREFIX(m_i)
      #FUNC_SVA_MISSING_FAIL_AB(m_i)
      #NAME_PROP_PREFIX(m_i)
      #DBG_SVA_MISSING_ENDLABEL(m_i)
  
