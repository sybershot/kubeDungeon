class UnitBase:
    def __init__(self, unit_lvl=0, unit_type="MissingNo.", health=0, damage=0):
        self._unit_name = "mob"
        self._unit_type = unit_type
        self._unit_health = health
        self._unit_damage = damage

# self._unit_mutator_slots = mutator_slots
# self._unit_rarity = rarity
# self._unit_friendly = true
