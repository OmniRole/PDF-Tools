from dataclasses import dataclass, asdict
from typing import Any, Dict, List

@dataclass
class MergeRequest:
    files: List[str]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MergeRequest":
        return cls(files=data.get("files", []))

@dataclass
class MergeResponse:
    merged_file: str
    message: str

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
