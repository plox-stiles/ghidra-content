'''
author      - trenton stiles
name        - markup_toggle.py
description - provides a quick way to toggle mnemonics aliases that
you see in the listing view, so instead of seeing label information
for a variable its the actual register being used shown instead.
'''

from ghidra.app.script import GhidraScript
from ghidra.framework.options import Options
from ghidra.util import SystemUtilities

# https://ghidra.re/ghidra_docs/api/ghidra/framework/options/ToolOptions.html#nested-class-summary
# https://ghidra.re/ghidra_docs/api/ghidra/framework/options/Options.html

markup_opts = [
	'Operands Field.Markup Inferred Variable References',  
	'Operands Field.Markup Register Variable References',
	'Operands Field.Markup Stack Variable References',
]

tool = state.getTool()
options = tool.getOptions("Listing Fields")

for opt in markup_opts:
	toggle = True
	if options.getBoolean(opt, True):
		toggle = False
		
	options.setBoolean(opt, toggle)
	print('set {} to {}').format(opt, toggle)
	