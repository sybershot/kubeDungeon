import random
import json

from itemUnitGenerator.items import *
from itemUnitGenerator.item_modifiers import *
from itemUnitGenerator.units import *
from itemUnitGenerator.unit_mutators import *


class Generator:
    # Loading items and monsters JSON files.
    def __init__(self):
        with open("../datapacks/items.json", "r", encoding='utf-8') as item_in:
            self._game_data = json.load(item_in)
            self._item_data = self._game_data["weapon_type"]
            self._major_mod_data = self._game_data["major_mod"]
            self._minor_mod_data = self._game_data["minor_mod"]

        with open("../datapacks/mobs.json", "r", encoding='utf-8') as mob_in:
            self._mob_data = json.load(mob_in)

    def gen_item(self, ilvl=None, rarity=None):
        """TODO: documentation"""
        if ilvl is None:
            try:
                ilvl = int(input("Enter item lvl: "))
            except ValueError as e:
                ilvl = random.randint(1, 10)
        if rarity is None:
            rarity = round(random.lognormvariate(0, 0.42), 3)
        item = random.choice([ItemMelee, ItemRanged])(item_lvl=ilvl, rarity=rarity)  # type:ItemBase
        item.name = random.choice(self._game_data["weapon_type"][item.type_name]["names"])
        if ilvl > 10:
            ilvl = 10
        self.gen_modifiers(rarity, item)
        damage = random.uniform(ilvl, ilvl * 2)
        item.damage = damage
        return item

    def gen_modifiers(self, rarity, item: ItemBase):
        if rarity < 1:
            return
        if rarity > 1:
            item.max_modifier += 1
            item.add_modifier(ModifierMinor(**random.choice(self._minor_mod_data)))
        if rarity > 2:
            item.max_modifier += 1
            item.add_modifier(ModifierMajor(**random.choice(self._major_mod_data)))
        # if rarity>=3:
        #     item.max_modifier += 1
        #     item.add_modifier(ModifierMajor(**random.choice(major_mod_data)))

    # ======================================================================================================================

    def gen_unit(self, ulvl=None, rarity=None):
        # Placeholder copy of item generation method, needs to be redone units.
        if ulvl is None:
            try:
                ulvl = int(input("Enter unit lvl: "))
            except ValueError as e:
                ulvl = random.randint(1, 10)
        if rarity is None:
            rarity = round(random.lognormvariate(0, 0.42), 3)
        unit = random.choice([ItemMelee, ItemRanged])(unit_lvl=ulvl, rarity=rarity)  # type:UnitBase
        unit.name = random.choice(self._mob_data["mob_type"][unit.type_name]["names"])
        if ulvl > 10:
            ulvl = 10
        self.gen_mutators(rarity, unit)
        damage = random.uniform(ulvl, ulvl * 2)
        unit.damage = damage
        return (unit)

    def gen_mutators(self, rarity, mob: MobBase):
        if rarity < 1:
            return
        if rarity > 1:
            mob.mutator_slots += 1
            mob.add_mutator(ModifierMinor(**random.choice(self._minor_mod_data)))
        if rarity > 2:
            mob.mutator_slots += 1
            mob.add_mutator(ModifierMajor(**random.choice(self._major_mod_data)))
