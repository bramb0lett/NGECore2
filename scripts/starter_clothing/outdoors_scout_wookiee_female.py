import sys

def OutdoorScoutWookieeFemale(core, object):
	shirt = core.objectService.createObject('object/tangible/wearables/wookiee/shared_wke_shirt_s01.iff', object.getPlanet())
	inventory = object.getSlottedObject('inventory')
	inventory.add(shirt)
	object._add(shirt)