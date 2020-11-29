# Main map classes file
import typing
from dataclasses import dataclass, field
from typing import List

MapYXZ = typing.NamedTuple('MapYXZ', [('zone', str), ('y', int), ('x', int), ('z', int)])
PointData = typing.NamedTuple('PointData', [('dataclass', type), ('rowid', int), ('char', str), ('exit', tuple)])


@dataclass
class ZoneMapList:
    zone: str
    cords: tuple
    key: MapYXZ


@dataclass
class Door:
    _type: str = 'door'
    _passable: bool = False
    _char: str = None
    _seen: bool = False
    _closed: bool = True
    _block_sight = True
    _locked: bool = False
    _can_pick: bool = True
    _lock_dc: int = 10
    _breakable: bool = True
    _break_dc: int = 16
    _material: str = 'wooden'
    _req_key: bool = False
    _key: str = None
    _is_exit: bool = False
    _desc: str = None


@dataclass
class Wall:
    _type: str = 'wall'
    _char: str = None
    _passable: bool = False
    _seen: bool = False
    _block_sight: bool = True
    _material: str = 'stone'
    _desc: str = None

    @property
    def char(self):
        return self._char


@dataclass
class Chest:
    _type: str = 'chest'
    _char: str = 'C'
    _passable: bool = False
    _seen: bool = False
    _locked: bool = False
    _can_pick: bool = True
    _lock_dc: int = 14
    _breakable: bool = True
    _break_dc: int = 16
    _req_key: bool = False
    _material: str = 'wood'
    _contains: List[str] = field(default_factory=list)
    _desc: str = None

@dataclass
class SecretDoor:
    _type: str = 'secretdoor'
    _char: str = 'S'
    _false_char: str = None
    _seen: bool = False
    _found: bool = False
    _passable: bool = False
    _find_dc: int = 16
    _locked: bool = False
    _can_pick: bool = True
    _lock_dc: int = 18
    _material: str = 'stone'
    _desc: str = None


@dataclass
class Mob:
    _type: str = 'mob'
    _race: str = None
    _class: str = None
    _char: str = 'M'
    _passable: bool = False
    _seen: bool = False
    _stats: any = None
    _wanders: bool = True
    _wander_range: int = 0
    _corpse: bool = False
    _current_hp: int = 0
    _aggro: bool = False


@dataclass
class Exit:
    _type: str = 'exit'
    _map: tuple = None
    _char: str = 'E'


@dataclass
class Blank:
    _char: str = ''

