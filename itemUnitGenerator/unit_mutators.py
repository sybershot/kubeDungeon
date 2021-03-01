from typing import Dict


class MutatorBase:
    def __init__(self, mutator_name="Defective",
                 description="This entity has been corrupted by the force beyond your understanding",
                 mutator_tip="This is wrong...", effects=None):
        self._mutator_name = mutator_name
        self._mutator_desc = description
        self._mutator_tip = mutator_tip
        if effects is None:
            raise Exception("Error during mutator effects creation!")
        else:
            self._mutator_effects = effects  # type:Dict

    @property
    def name(self):
        return self._mutator_name

    @property
    def effects(self):
        return self._mutator_effects

    @property
    def parsed_effects(self):
        ret = {}
        for effect_name, effect_value in self.effects.items():
            applies_to, field1, field2 = effect_name.split('_')
            ret[applies_to] = ret.get(applies_to, {})
            ret[applies_to][field1] = ret[applies_to].get(field1, {})
            ret[applies_to][field1][field2] = effect_value
        return ret

    def __repr__(self):
        return f'<Modifier name:"{self.name}" ' \
               f'description:"{self._mutator_desc}" ' \
               f'tip:"{self._mutator_tip}" '
