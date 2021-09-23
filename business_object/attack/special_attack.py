from business_object.attack.abstract_formula_attack import AbstractFormulaAttack
from business_object.pokemon.abstract_pokemon import AbstractPokemon


class SpecialFormulaAttack(AbstractFormulaAttack):
    def get_attack_stat(self
                        , attacker: AbstractPokemon
                        , defender: AbstractPokemon) -> float:
        return attacker.sp_atk_current

    def get_defense_stat(self
                         , attacker: AbstractPokemon
                         , defender: AbstractPokemon) -> float:
        return defender.sp_def_current


