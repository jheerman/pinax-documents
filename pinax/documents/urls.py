from django.urls import path, re_path

from . import views

app_name = "pinax_documents"

urlpatterns = [
    re_path(r"^$", views.IndexView.as_view(),
        name="document_index"),
    re_path(r"^d/create/$", views.DocumentCreate.as_view(),
        name="document_create"),
    re_path(r"^d/(?P<pk>\d+)/$", views.DocumentDetail.as_view(),
        name="document_detail"),
    re_path(r"^d/(?P<pk>\d+)/download/$", views.DocumentDownload.as_view(),
        name="document_download"),
    re_path(r"^d/(?P<pk>\d+)/delete/$", views.DocumentDelete.as_view(),
        name="document_delete"),
    re_path(r"^f/create/$", views.FolderCreate.as_view(),
        name="folder_create"),
    re_path(r"^f/(?P<pk>\d+)/$", views.FolderDetail.as_view(),
        name="folder_detail"),
    re_path(r"^f/(?P<pk>\d+)/share/$", views.FolderShare.as_view(),
        name="folder_share"),
    re_path(r"^f/(?P<pk>\d+)/delete/$", views.FolderDelete.as_view(),
        name="folder_delete"),
]
