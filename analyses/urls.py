from django.urls import include, path

from . import views

urlpatterns = [
    path(
        "analyses/",
        include(
            [
                path("", views.AnalysisList.as_view(), name="analysis-list"),
                path("new", views.AnalysisCreate.as_view(), name="analysis-new"),
                path(
                    "<uuid:id>", views.AnalysisDetail.as_view(), name="analysis-detail"
                ),
                path(
                    "<uuid:id>/edit", views.AnalysisEdit.as_view(), name="analysis-edit"
                ),
                path(
                    "<uuid:id>/start",
                    views.AnalysisStart.as_view(),
                    name="analysis-start",
                ),
                path(
                    "<uuid:id>/finish",
                    views.AnalysisFinish.as_view(),
                    name="analysis-finish",
                ),
            ]
        ),
    ),
]
