# ЗДЕСЬ БУДУТ ПОДГРУЖАТЬСЯ СПИСКИ ПРЕДМЕТОВ И МОБОВ, А ЕЩЁ ВСЯКИЕ ПЕРДЕЛКИ ТИПА ГЕНЕРАЦИЯ ПРЕДМЕТОВ/МОБОВ
import random
import json

# АЙТЕМСЫ
from items import ItemMelee, ItemRanged, ItemBase
from modifiers import ModifierMinor, ModifierMajor


class Generator:
    def __init__(self):
        with open("items.json", "r", encoding='utf-8') as item_in:
            self._game_data = json.load(item_in)
            self._item_data = self._game_data["weapon_type"]
            self._major_mod_data = self._game_data["major_mod"]
            self._minor_mod_data = self._game_data["minor_mod"]

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

    # МОБСЫ
    with open("mobs.json", "r", encoding='utf-8') as mob_in:
        mob_l = json.load(mob_in)

    def gen_mob(self):
        mtype = random.choice(mob_l["type"])
        pfix = random.choice(mob_l["postfix"])
        affix = random.choice(mob_l["affix"])
        name = affix + ' ' + mtype + ' ' + pfix
        # TODO: stats of mobs.
        print(name)
