from django.urls import include, path
from . import views


app_name = 'summaries'


urlpatterns = [

    # *********************** summariy crud urls *********************** 
    path('', views.SummaryList.as_view(), name='summary_list'), # all summaries 
    path('<int:tag_id>/', views.SummaryList.as_view(), name='summary_list'), # filter summaries by tags
    path('<int:category_id>/', views.SummaryList.as_view(), name='summary_list'), # filter summaries by categories
    path('add/', views.SummaryCreate.as_view(), name='summary_add'), # add summary
    path('<int:pk>/detail/', views.SummaryDetail.as_view(), name='summary_detail'), # summary details
    path('<int:pk>/update/', views.SummaryUpdate.as_view(), name='summary_update'), # edit summary
    path('<int:pk>/delete/', views.SummaryDelete.as_view(), name='summary_delete'), # delete summary

    # *********************** download summary using weasyprint *********************** 
    path('<int:pk>/download', views.SummaryDownload.as_view(), name='summary_download'), 

]


