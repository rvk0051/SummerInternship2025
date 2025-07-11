from .request_detail_views import ContactHRDetailAPIView
from .list_or_create_request_views import ContactHRListCreateAPIView
from .mark_as_resolved_views import MarkAsResolvedAPIView

__all__ = [
    'ContactHRListCreateAPIView',
    'ContactHRDetailAPIView',
    'MarkAsResolvedAPIView'
]