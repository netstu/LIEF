from typing import Any, ClassVar, Iterator, Optional

from typing import overload
import lief # type: ignore
import lief.dwarf # type: ignore
import lief.dwarf.CompilationUnit # type: ignore
import lief.dwarf.CompilationUnit.Language # type: ignore
import lief.dwarf.Function # type: ignore
import lief.dwarf.Scope # type: ignore
import lief.dwarf.Type # type: ignore

class CompilationUnit:
    class Language:
        class LANG:
            C: ClassVar[CompilationUnit.Language.LANG] = ...
            CPP: ClassVar[CompilationUnit.Language.LANG] = ...
            DART: ClassVar[CompilationUnit.Language.LANG] = ...
            RUST: ClassVar[CompilationUnit.Language.LANG] = ...
            UNKNOWN: ClassVar[CompilationUnit.Language.LANG] = ...
            __name__: str
            def __init__(self, *args, **kwargs) -> None: ...
            @staticmethod
            def from_value(arg: int, /) -> lief.dwarf.CompilationUnit.Language.LANG: ...
            def __ge__(self, other) -> bool: ...
            def __gt__(self, other) -> bool: ...
            def __hash__(self) -> int: ...
            def __index__(self) -> Any: ...
            def __int__(self) -> int: ...
            def __le__(self, other) -> bool: ...
            def __lt__(self, other) -> bool: ...
            @property
            def value(self) -> int: ...
        lang: lief.dwarf.CompilationUnit.Language.LANG
        version: int
        def __init__(self, *args, **kwargs) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    @overload
    def find_function(self, name: str) -> Optional[lief.dwarf.Function]: ...
    @overload
    def find_function(self, addr: int) -> Optional[lief.dwarf.Function]: ...
    @overload
    def find_variable(self, addr: int) -> Optional[lief.dwarf.Variable]: ...
    @overload
    def find_variable(self, name: str) -> Optional[lief.dwarf.Variable]: ...
    @property
    def compilation_dir(self) -> str: ...
    @property
    def functions(self) -> Iterator[Optional[lief.dwarf.Function]]: ...
    @property
    def high_address(self) -> int: ...
    @property
    def language(self) -> lief.dwarf.CompilationUnit.Language: ...
    @property
    def low_address(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def producer(self) -> str: ...
    @property
    def ranges(self) -> list[lief.range_t]: ...
    @property
    def size(self) -> int: ...
    @property
    def types(self) -> Iterator[Optional[lief.dwarf.Type]]: ...
    @property
    def variables(self) -> Iterator[Optional[lief.dwarf.Variable]]: ...

class DebugInfo(lief.DebugInfo):
    def __init__(self, *args, **kwargs) -> None: ...
    @overload
    def find_function(self, name: str) -> Optional[lief.dwarf.Function]: ...
    @overload
    def find_function(self, addr: int) -> Optional[lief.dwarf.Function]: ...
    def find_type(self, name: str) -> Optional[lief.dwarf.Type]: ...
    @overload
    def find_variable(self, addr: int) -> Optional[lief.dwarf.Variable]: ...
    @overload
    def find_variable(self, name: str) -> Optional[lief.dwarf.Variable]: ...
    @property
    def compilation_units(self) -> Iterator[Optional[lief.dwarf.CompilationUnit]]: ...

class Function:
    class Parameter:
        def __init__(self, *args, **kwargs) -> None: ...
        @property
        def name(self) -> str: ...
        @property
        def type(self) -> Optional[lief.dwarf.Type]: ...
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def address(self) -> Optional[int]: ...
    @property
    def debug_location(self) -> lief.debug_location_t: ...
    @property
    def is_artificial(self) -> bool: ...
    @property
    def linkage_name(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def parameters(self) -> list[lief.dwarf.Function.Parameter]: ...
    @property
    def ranges(self) -> list[lief.range_t]: ...
    @property
    def scope(self) -> Optional[lief.dwarf.Scope]: ...
    @property
    def size(self) -> int: ...
    @property
    def type(self) -> Optional[lief.dwarf.Type]: ...
    @property
    def variables(self) -> Iterator[Optional[lief.dwarf.Variable]]: ...

class Scope:
    class TYPE:
        CLASS: ClassVar[Scope.TYPE] = ...
        COMPILATION_UNIT: ClassVar[Scope.TYPE] = ...
        FUNCTION: ClassVar[Scope.TYPE] = ...
        NAMESPACE: ClassVar[Scope.TYPE] = ...
        STRUCT: ClassVar[Scope.TYPE] = ...
        UNION: ClassVar[Scope.TYPE] = ...
        UNKNOWN: ClassVar[Scope.TYPE] = ...
        __name__: str
        def __init__(self, *args, **kwargs) -> None: ...
        def __ge__(self, other) -> bool: ...
        def __gt__(self, other) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> Any: ...
        def __int__(self) -> int: ...
        def __le__(self, other) -> bool: ...
        def __lt__(self, other) -> bool: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def chained(self, sep: str = ...) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def parent(self) -> Optional[lief.dwarf.Scope]: ...
    @property
    def type(self) -> lief.dwarf.Scope.TYPE: ...

class Type:
    class KIND:
        ARRAY: ClassVar[Type.KIND] = ...
        BASE: ClassVar[Type.KIND] = ...
        CLASS: ClassVar[Type.KIND] = ...
        CONST_KIND: ClassVar[Type.KIND] = ...
        POINTER: ClassVar[Type.KIND] = ...
        STRUCT: ClassVar[Type.KIND] = ...
        UNION: ClassVar[Type.KIND] = ...
        UNKNOWN: ClassVar[Type.KIND] = ...
        UNSPECIFIED: ClassVar[Type.KIND] = ...
        __name__: str
        def __init__(self, *args, **kwargs) -> None: ...
        def __ge__(self, other) -> bool: ...
        def __gt__(self, other) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> Any: ...
        def __int__(self) -> int: ...
        def __le__(self, other) -> bool: ...
        def __lt__(self, other) -> bool: ...
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def is_unspecified(self) -> bool: ...
    @property
    def kind(self) -> lief.dwarf.Type.KIND: ...
    @property
    def location(self) -> lief.debug_location_t: ...
    @property
    def name(self) -> Optional[str]: ...
    @property
    def scope(self) -> Optional[lief.dwarf.Scope]: ...
    @property
    def size(self) -> Optional[int]: ...

class Variable:
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def address(self) -> Optional[int]: ...
    @property
    def debug_location(self) -> lief.debug_location_t: ...
    @property
    def is_constexpr(self) -> bool: ...
    @property
    def linkage_name(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def scope(self) -> Optional[lief.dwarf.Scope]: ...
    @property
    def size(self) -> Optional[int]: ...
    @property
    def type(self) -> Optional[lief.dwarf.Type]: ...

def load(path: str) -> Optional[lief.dwarf.DebugInfo]: ...
