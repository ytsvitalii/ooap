from abc import ABC, abstractmethod
from enum import Enum
from typing import Union, Optional


class CharacterType(Enum):
    human = 'human'
    troll = 'troll'
    orc = 'orc'


class WeaponType(Enum):
    bow = 'bow'
    sword = 'sword'
    mace = 'mace'
    dagger = 'dagger'
    axe = 'axe'


class ArmourType(Enum):
    armor = 'armor',
    wooden_shield = 'wooden shield'
    iron_shield = 'iron_shield'


class Character(ABC):
    @abstractmethod
    def get_name(self):
        ...

    @abstractmethod
    def get_attack(self):
        ...

    @abstractmethod
    def get_defense(self):
        ...

    @abstractmethod
    def get_history(self):
        ...

    def __str__(self):
        return f"{self.get_name()} (Strength: {self.get_attack()}, Defense: {self.get_defense()}) {self.get_history()}"


class Human(Character):

    def get_name(self):
        return 'Human'

    def get_attack(self):
        return 5

    def get_defense(self):
        return 3

    def get_history(self):
        return ''


class Troll(Character):

    def get_name(self):
        return 'Troll'

    def get_attack(self):
        return 8

    def get_defense(self):
        return 5

    def get_history(self):
        return ''


class Orc(Character):

    def get_name(self):
        return 'Orc'

    def get_attack(self):
        return 10

    def get_defense(self):
        return 7

    def get_history(self):
        return ''


class WeaponDecorator(Character, ABC):
    def __init__(self, character: Character):
        self.character = character

    @abstractmethod
    def get_attack_modifier(self):
        pass

    def get_name(self):
        return self.character.get_name()

    def get_attack(self):
        return self.character.get_attack() + self.get_attack_modifier()

    def get_defense(self):
        return self.character.get_defense()

    def get_history(self):
        return self.character.get_history() + self.decorated_name() + ', '

    def __str__(self):
        return f"{self.get_name()} (Strength: {self.get_attack()}, Defense: {self.get_defense()}), {self.get_history()}"

    @abstractmethod
    def decorated_name(self):
        pass


class Bow(WeaponDecorator):
    def get_attack_modifier(self):
        return 3

    def decorated_name(self):
        return 'Bow'


class Sword(WeaponDecorator):
    def get_attack_modifier(self):
        return 5

    def decorated_name(self):
        return "Sword"


class Mace(WeaponDecorator):
    def get_attack_modifier(self):
        return 6

    def decorated_name(self):
        return "Mace"


class Dagger(WeaponDecorator):
    def get_attack_modifier(self):
        return 3

    def decorated_name(self):
        return "Dagger"


class Axe(WeaponDecorator):
    def get_attack_modifier(self):
        return 4

    def decorated_name(self):
        return "Axe"


class ArmourDecorator(Character, ABC):
    def __init__(self, character: Character):
        self.character = character

    @abstractmethod
    def get_defense_modifier(self):
        pass

    def get_name(self):
        return self.character.get_name()

    def get_attack(self):
        return self.character.get_attack()

    def get_defense(self):
        return self.character.get_defense() + self.get_defense_modifier()

    def get_history(self):
        return self.character.get_history() + self.decorated_name() + ', '

    def __str__(self):
        return f"{self.get_name()} (Strength: {self.get_attack()}, Defense: {self.get_defense()}), {self.get_history()}"

    @abstractmethod
    def decorated_name(self):
        pass


class Armor(ArmourDecorator):
    def get_defense_modifier(self):
        return 7

    def decorated_name(self):
        return 'Armor'


class IronShield(ArmourDecorator):
    def get_defense_modifier(self):
        return 5

    def decorated_name(self):
        return 'IronShield'


class WoodenShield(ArmourDecorator):
    def get_defense_modifier(self):
        return 2

    def decorated_name(self):
        return 'WoodenShield'


class CharacterFacade:
    CHARACTER_ID = {
        1: CharacterType.human,
        2: CharacterType.troll,
        3: CharacterType.orc
    }
    WEAPON_ID = {
        1: WeaponType.bow,
        2: WeaponType.sword,
        3: WeaponType.mace,
        4: WeaponType.dagger,
        5: WeaponType.axe
    }
    ARMOUR_ID = {
        1: ArmourType.armor,
        2: ArmourType.wooden_shield,
        3: ArmourType.iron_shield
    }

    def __init__(self):
        self.character: Union[Character, None] = None

    def __convert_character_id_to_name(self, character_id: int) -> Optional[CharacterType]:
        return self.CHARACTER_ID.get(character_id)

    def __convert_weapon_id_to_name(self, weapon_id: int) -> Optional[WeaponType]:
        return self.WEAPON_ID.get(weapon_id)

    def __convert_armour_id_to_name(self, armour_id: int) -> Optional[ArmourType]:
        return self.ARMOUR_ID.get(armour_id)

    @staticmethod
    def choose_character_by_type(character_type: CharacterType) -> Optional[Character]:
        if character_type == CharacterType.human:
            return Human()
        elif character_type == CharacterType.troll:
            return Troll()
        elif character_type == CharacterType.orc:
            return Orc()
        else:
            return None

    def choose_weapon_by_type(self, weapon_type: WeaponType) -> None:
        if WeaponType.bow == weapon_type:
            return self.take_bow()
        elif WeaponType.sword == weapon_type:
            return self.take_sword()
        elif WeaponType.mace == weapon_type:
            return self.take_mace()
        elif WeaponType.dagger == weapon_type:
            return self.take_dagger()
        elif WeaponType.axe == weapon_type:
            return self.take_axe()
        else:
            return None

    def choose_armour_by_type(self, armour_type: ArmourType) -> None:
        if armour_type == ArmourType.armor:
            return self.take_armor()
        elif armour_type == ArmourType.wooden_shield:
            return self.take_wooden_shield()
        elif armour_type == ArmourType.wooden_shield:
            return self.take_iron_shield()
        else:
            return None


    def take_bow(self):
        self.character = Bow(self.character)

    def take_sword(self):
        self.character = Sword(self.character)

    def take_mace(self):
        self.character = Mace(self.character)

    def take_dagger(self):
        self.character = Dagger(self.character)

    def take_axe(self):
        self.character = Axe(self.character)

    def character_info(self):
        return f'{self.character}'

    def take_armor(self):
        self.character = Armor(self.character)

    def take_wooden_shield(self):
        self.character = WoodenShield(self.character)

    def take_iron_shield(self):
        self.character = IronShield(self.character)

    def choose_character(self, character_type: CharacterType = None) -> None:
        if character_type:
            self.character = self.choose_character_by_type(character_type)
            return

        while True:
            character_id = input('Please select the character you want to play as: human - 1, troll - 2, orc - 3: ')
            if character_id.isdigit():
                character_name = self.__convert_character_id_to_name(int(character_id))
                if character_name is None:
                    print('You have selected a non-existent character. Try again!')
                    continue

                self.character = self.choose_character_by_type(character_name)
                return
            else:
                print('You must enter the ID of character 1-3')
                continue

    def choose_armour(self):
        while True:
            armour_id = input('Please select the armour you want to play with: '
                              'clothes(armor) - 1, wooden shield - 2, metal shield - 3: ')

            if armour_id.isdigit():
                armour_name = self.__convert_armour_id_to_name(int(armour_id))
                if armour_name is None:
                    print('You have selected a non-existent armour. Try again!')
                    continue

                self.choose_armour_by_type(armour_name)
                return
            else:
                print('You must enter the ID of armour 1-3')
                continue

    def choose_weapon(self):
        while True:
            weapon_id = input('Please select the weapon you want to play with: '
                              'bow - 1, sword - 2, mace - 3, dagger - 4, axe - 5: ')
            if weapon_id.isdigit():
                weapon_name = self.__convert_weapon_id_to_name(int(weapon_id))
                if weapon_name is None:
                    print('You have selected a non-existent weapon. Try again!')
                    continue

                self.choose_weapon_by_type(weapon_name)
                return
            else:
                print('You must enter the ID of character 1-5')
                continue

    def is_stronger_than(self, other_character: Character) -> bool:
        return self.character.get_attack() > other_character.get_attack()

    def can_defeat_in_single_strike(self, other_character: Character) -> bool:
        return self.character.get_attack() >= other_character.get_defense()

    def strikes_needed_to_defeat(self, other_character: Character, strikes: int) -> bool:
        return self.character.get_attack() * strikes >= other_character.get_defense()


if __name__ == "__main__":
    first_character_controller = CharacterFacade()
    second_character_controller = CharacterFacade()
    first_character_controller.choose_character()
    print(first_character_controller.character_info())
    first_character_controller.choose_weapon()
    print(first_character_controller.character_info())
    first_character_controller.choose_armour()
    print(first_character_controller.character_info())

    # NPC character
    second_character_controller.choose_character(CharacterType.orc)
    second_character_controller.take_sword()
    # second_character_controller.take_armor()
    second_character_controller.take_iron_shield()

    my_character_info = first_character_controller.character_info()
    npc_info = second_character_controller.character_info()

    if first_character_controller.is_stronger_than(second_character_controller.character):
        print(f'\033[92mI won! He\'s weaker\033[0m'
              f'\n{my_character_info} '
              f'IS STRONGER THAN NPC CHARACTER: {npc_info}')
    else:
        print(f'\033[91mI lost, he is stronger\033[0m'
              f'\n{npc_info} '
              f'IS STRONGER THAN NPC CHARACTER: {my_character_info}')

    if first_character_controller.can_defeat_in_single_strike(second_character_controller.character):
        print(f'\033[92mI won! I defeat in single strike\033[0m'
              f'\n{my_character_info} '
              f'ONE SHOT: {npc_info}')
    else:
        print(f'\033[91mCouldn\'t kill with the first hit\033[0m'
              f'\n{npc_info} '
              f'Couldn\'t kill: {my_character_info}')


