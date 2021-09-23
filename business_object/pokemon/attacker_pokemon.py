from business_object.attack.abstract_formula_attack import AbstractFormulaAttack
from business_object.attack.physical_attack import PhysicalFormulaAttack
from business_object.pokemon.abstract_pokemon import AbstractPokemon


class AttackerPokemon(AbstractPokemon):

    def __init__(self
                 , stat_max=None
                 , stat_current=None
                 , level=None
                 , name=None
                 , gear=None
                 , common_attacks = []) -> None:
        special_attack = PhysicalFormulaAttack(power=60
                                               , name="Flying Strike"
                                               , description="{pokemon} dives to it's prey from the sky")

        super().__init__(stat_max=stat_max
                         , stat_current=stat_current
                         , level=level
                         , name=name
                         , gear=gear
                         , special_attack=special_attack
                         , common_attacks=common_attacks)

    def get_pokemon_attack_coef(self) -> float:
        return 1 + (self.speed_current+self.attack_current)/200