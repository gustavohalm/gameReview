from rest_framework import routers
from .views import ReviewViewSet, CommentViewSet

router = routers.DefaultRouter()


router.register('review', ReviewViewSet)
router.register('comment', CommentViewSet)

urlpatterns = router.urls