import sys

def setup(core, actor, buff):
	return

def add(core, actor, buff):
	core.skillModService.addSkillMod(actor, 'expertise_dodge', 2)
	core.skillModService.addSkillMod(actor, 'constitution_modified', 10)
	return
	
def remove(core, actor, buff):
	core.skillModService.deductSkillMod(actor, 'expertise_dodge', 2)
	core.skillModService.deductSkillMod(actor, 'constitution_modified', 10)
	return