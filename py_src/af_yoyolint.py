# ----------------------------------------------------
# SPDX-FileCopyrightText: Ajeetha Kumari Venkatesan
#                         AsFigo Technologies, UK
# SPDX-License-Identifier: MIT
# ----------------------------------------------------

import pyslang
import argparse
import os.path
import copy
import functools
from operator import countOf
import operator as op

print_verbose = False

def yylUpdateRIDs():
  lvYylRIDli = list()
  lvYylRIDli.append('LOGIC_PARAM_NYS')
  lvYylRIDli.append('INT_PARAM_NYS')
  lvYylRIDli.append('INT_TYPE_NYS')
  lvYylRIDli.append('NO_PORTS_IN_CHECKER')
  lvYylRIDli.append('NO_ENDLABEL_IN_CHECKER')
  lvYylRIDli.append('NAME_INTF_SUFFIX')


def yYLRenabled(rule_id):
  return True

def yYLMsg(rule_id, msg):
  if (yYLRenabled(rule_id)):
    lvYylStr = 'yoYoLint: Violation: ['
    lvYylStr += rule_id
    lvYylStr += ']: '
    lvYylStr += msg 
    print(lvYylStr)


def yYLArgParse():
  # Create the parser
  parser = argparse.ArgumentParser()
  # Add an argument
  parser.add_argument('-t', '--test', type=str, required=True)
  # Parse the argument
  args = parser.parse_args()
  return args

def yYLUpdatePrefix():
  lv_sv_prefix_d = {}
  lv_sv_prefix_d.update({"prop": "p_"})
  lv_sv_prefix_d.update({"cover": "c_"})
  lv_sv_prefix_d.update({"assert": "a_"})
  lv_sv_prefix_d.update({"assume": "m_"})
  return lv_sv_prefix_d

def yYLUpdateSuffix():
  lv_sv_suffix_d = {}
  lv_sv_suffix_d.update({"intf": "_if"})
  lv_sv_suffix_d.update({"class": "_c"})
  lv_sv_suffix_d.update({"cnst": "_cst"})
  lv_sv_suffix_d.update({"mod": "_m"})
  return lv_sv_suffix_d

def yYLChkNamePrefix(lvRID, lv_name, lv_exp_p):
  if (lv_name.startswith(lv_exp_p)):
    if (print_verbose):
      print('AF: Good naming: ', lv_name)
  else:
    msg = 'Improper naming of identifier: ' 
    msg += lv_name
    msg += ': expected prefix: '
    msg += lv_exp_p
    yYLMsg(lvRID, msg)

def yYLChkNameSuffix(lvRID, lv_name, lv_exp_s):
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

def yYLChkNaming(lvCuScp):

  if (lvCuScp.kind.name == 'InterfaceDeclaration'):
    lv_ident_name = str(lvCuScp.header.name)
    lv_exp_s = sv_suffix_d['intf']
    yYLChkNameSuffix ('NAME_INTF_SUFFIX', lv_ident_name, lv_exp_s)
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

args = yYLArgParse()

sv_prefix_d = yYLUpdatePrefix()
sv_suffix_d = yYLUpdateSuffix()
yoyol_rules_l = yylUpdateRIDs()

inp_test_name = args.test

tree = pyslang.SyntaxTree.fromFile(inp_test_name)
r = tree.root

if (tree.root.members.__str__() == ''):
  print("YoYoLint: No modules/interfaces/ found")
  exit(0)

for scope_i in (tree.root.members):
  yYLChkNaming(scope_i)
  yyLModuleLint(scope_i)
  yyLChkrLint(scope_i)
  DBG_AVOID_BEGIN_IN_FN(scope_i)

