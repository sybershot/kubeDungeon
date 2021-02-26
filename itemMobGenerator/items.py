from modifiers import ModifierMajor, ModifierMinor, ModifierBase


class ItemBase:
    def __init__(self, item_lvl=0, name="Undefined?", modifiers=None, rarity=0, use_speed=0, max_modifier=0):
        self.type_name = "item"
        self._item_lvl = item_lvl
        self._name = name
        self._rarity = rarity
        self._use_speed = use_speed
        if modifiers is None:
            self._modifiers = []  # type:List[ModifierBase]
        else:
            self._modifiers = modifiers  # type:List[ModifierBase]
        self._max_modifier = max_modifier

    # region Getters/Setters
    @property
    def item_lvl(self):
        return self._item_lvl

    @item_lvl.setter
    def item_lvl(self, new_item_lvl):
        if type(new_item_lvl) is int:
            self._item_lvl = new_item_lvl
        else:
            raise ValueError("Item lvl is not int.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def rarity(self):
        return self._rarity

    @rarity.setter
    def rarity(self, new_rarity):
        self._rarity = new_rarity

    @property
    def use_speed(self):
        return self._use_speed

    @use_speed.setter
    def use_speed(self, new_use_speed):
        self._use_speed = new_use_speed

    @property
    def max_modifier(self):
        return self._max_modifier

    @max_modifier.setter
    def max_modifier(self, new_max_modifier):
        self._max_modifier = new_max_modifier

    # endregion
    def add_modifier(self, modifier):
        if len(self._modifiers) < self._max_modifier:
            self._modifiers.append(modifier)

    @property
    def modifiers(self):
        return self._modifiers

    @property
    def full_name(self):
        accumulator = self.name
        for mod in self.modifiers:
            if type(mod) is ModifierMajor:
                accumulator = mod.name + ' ' + accumulator
            if type(mod) is ModifierMinor:
                accumulator = accumulator + ' ' + mod.name
        return accumulator

    def __str__(self):
        return f"Name: {self.full_name}\n" \
            f"\tItem lvl: {self.item_lvl}\n" \
            f"\tRarity: {self.rarity}\n" \
            f"\tModifiers: {self._modifiers}\n"

    def __repr__(self):
        return f'<Item name:{self.full_name} lvl:{self.item_lvl} modifiers:{self._modifiers}>'


class ItemWeapon(ItemBase):
    def __init__(self, damage=0, damage_type="default", sockets=None, max_socket=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type_name = "weapon"
        self._damage = damage
        self._damage_type = damage_type
        if sockets is None:
            self._sockets = []
        else:
            self._sockets = sockets
        self._max_socket = max_socket

    def insert_to_socket(self, socket):
        if self.available_socket_slots > 0:
            self._sockets.append(socket)

    @property
    def available_socket_slots(self):
        return self._max_socket - len(self._sockets)

    # region Getters/Setters
    @property
    def damage(self):
        return round(self._damage, 3)

    @damage.setter
    def damage(self, new_damage):
        self._damage = new_damage

    @property
    def damage_type(self):
        for mod in self._modifiers:
            for effect_cat, effect_data in mod.parsed_effects.get('item', {}).items():
                for mod_type, mod_value in effect_data.items():
                    if effect_cat == 'dmg' and mod_type == 'type':
                        return mod_value
        return self._damage_type

    @damage_type.setter
    def damage_type(self, new_damage_type):
        self._damage_type = new_damage_type

    @property
    def full_damage(self):
        current_damage = self.damage
        for mod in self._modifiers:
            for effect_cat, effect_data in mod.parsed_effects.get('item', {}).items():
                for mod_type, mod_value in effect_data.items():
                    if effect_cat == 'dmg':
                        if mod_type == 'mult':
                            current_damage *= mod_value
                        elif mod_type == 'add':
                            current_damage += mod_value
                    else:
                        print(effect_cat, mod_type, mod_value)
        return round(current_damage, 3)

    # endregion
    def __str__(self):
        additional_dmg = ''
        for mod in self._modifiers:
            for effect_cat, effect_data in mod.parsed_effects.get('item', {}).items():
                for mod_type, mod_value in effect_data.items():
                    if effect_cat == 'effect':
                        if mod_type == 'dmg':
                            additional_dmg += f'+{mod_value}'

        return super().__str__() + f'\tDamage: {self.full_damage}{additional_dmg}({self.damage})\n\tDamage type:"{self.damage_type}"'


class ItemMelee(ItemWeapon):
    def __init__(self, use_range=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type_name = "melee"
        self._use_range = use_range

    @property
    def use_range(self):
        return self._use_range

    @use_range.setter
    def use_range(self, new_use_range):
        self._use_range = new_use_range


class ItemRanged(ItemWeapon):
    def __init__(self, use_range=100, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type_name = "ranged"
        self._use_range = use_range

    @property
    def use_range(self):
        return self._use_range

    @use_range.setter
    def use_range(self, new_use_range):
        self._use_range = new_use_range
