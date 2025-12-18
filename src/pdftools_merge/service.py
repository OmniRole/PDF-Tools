from .dao import MergeDAO
from .models import MergeRequest, MergeResponse

class MergeService:
    def __init__(self):
        self.dao = MergeDAO()

    def merge_pdfs(self, request: MergeRequest) -> MergeResponse:
        result = self.dao.merge_files_stub(request.files)
        return MergeResponse(
            merged_file=result["merged_file"],
            message=result["message"]
        )
