from typing import Any, Dict, List

class MergeDAO:
    def __init__(self):
        pass

    def merge_files_stub(self, files: List[str]) -> Dict[str, Any]:
        """Stub method returns fake merge result."""
        return {
            "merged_file": "output_merged.pdf",
            "message": f"Successfully merged {len(files)} files."
        }
