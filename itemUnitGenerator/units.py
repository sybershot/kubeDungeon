from typing import List

from itemUnitGenerator.unit_mutators import MutatorBase


class UnitBase:
    def __init__(self, name="John Doe, master of The Placeholder Realm.", max_move_speed=0, move_speed=0, max_health=0,
                 cur_health=0, damage=0, invincible=False, flying=False):
        self._unit_name = name
        self._unit_max_movespd = max_move_speed
        self._move_speed = move_speed
        self._unit_max_health = max_health
        self._unit_cur_health = cur_health
        self._unit_damage = damage
        self._is_invincible = invincible
        self._is_flying = flying

    # region Getters/Setters
    @property
    def unit_name(self):
        return self._unit_name

    @unit_name.setter
    def unit_name(self, new_name):
        self._unit_name = new_name

    @property
    def max_move_speed(self):
        return self._unit_max_movespd

    @max_move_speed.setter
    def max_move_speed(self, new_limit):
        self._unit_max_movespd = new_limit

    # endregion


class MobBase(UnitBase):
    def __init__(self, unit_lvl=0, rarity=0, unit_type="Glitch", mutators=None, mutator_slots=0, friendly=True, *args,
                 **kwargs, ):
        super().__init__(*args, **kwargs)
        self.type_name = "mob"
        self._unit_lvl = unit_lvl
        self._unit_rarity = rarity
        self._unit_name = "MissingNo."
        self._unit_type = unit_type
        self._unit_friendly = friendly
        self._unit_mutator_slots = mutator_slots
        # Maybe this should be tested for 0 with the mutators,
        # otherwise we might get 0 max mutator slots but still have mutators during generation.
        if mutators is None:
            self._unit_mutators = []  # type:List[MutatorBase]
        else:
            self._unit_mutators = mutators  # type:List[MutatorBase]

    # region Getters/Setters
    @property
    def unit_level(self):
        return self._unit_lvl

    @unit_level.setter
    def unit_level(self, new_lvl):
        if type(new_lvl) is int:
            self._unit_lvl = new_lvl
        else:
            raise ValueError("Can't assign new unit lvl! Is not int.")

    @property
    def unit_rarity(self):
        return self._unit_rarity

    @unit_rarity.setter
    def unit_rarity(self, new_rarity):
        if type(new_rarity) is int:
            self._unit_rarity = new_rarity
        else:
            raise ValueError("Can't assign new unit rarity! Is not int.")

    @property
    def mutator_slots(self):
        return self._unit_mutator_slots

    @mutator_slots.setter
    def mutator_slots(self, new_limit):
        self._unit_mutator_slots = new_limit

    # endregion
    def add_mutator(self, mutator):
        if len(self._unit_mutators) < self._unit_mutator_slots:
            self._unit_mutators.append(mutator)


class Player(MobBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
