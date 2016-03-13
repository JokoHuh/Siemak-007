from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index),
	url(r'^login/$', views.login_user, name='login_user'),
	url(r'^logout/$', views.login_user, name='login_user'),
# ------------------------------------------------------------------- Pt (pt)
	url(r'^pt/$', views.pt_list, name='pt_list'),
    url(r'^pt/(?P<pk>\d+)/$', views.pt_detail, name='pt_detail'),
	url(r'^pt/(?P<pk>\d+)/edit/$', views.pt_edit, name='pt_edit'),
    url(r'^pt/new/$', views.pt_new, name='pt_new'),
# ------------------------------------------------------------------ Pts (ps)
	url(r'^pts/$', views.pts_list, name='pts_list'),
    url(r'^pts/(?P<pk>\d+)/$', views.pts_detail, name='pts_detail'),
	url(r'^pts/(?P<pk>\d+)/edit/$', views.pts_edit, name='pts_edit'),
    url(r'^pts/new/$', views.pts_new, name='pts_new'),
# ---------------------------------------------------------------- Prodi (pr)
	url(r'^prod/$', views.prod_list, name='views.prod_list'),
	url(r'^prod/(?P<pk>\d+)/$', views.prod_detail, name='prod_detail'),
	url(r'^prod/(?P<pk>\d+)/edit/$', views.prod_edit, name='prod_edit'),
    url(r'^prod/new/$', views.prod_new, name='prod_new'),
# -------------------------------------------------------------- Pegawai (pg)
	url(r'^pegw/$', views.pegw_list, name='views.pegw_list'),
	url(r'^pegw/(?P<pk>\d+)/$', views.pegw_detail, name='pegw_detail'),
	url(r'^pegw/(?P<pk>\d+)/edit/$', views.pegw_edit, name='pegw_edit'),
    url(r'^pegw/new/$', views.pegw_new, name='pegw_new'),
# ------------------------------------------------------------------ Sk (sk)
	url(r'^sk/$', views.sk_list, name='views.sk_list'),
	url(r'^sk/(?P<pk>\d+)/$', views.sk_detail, name='sk_detail'),
	url(r'^sk/(?P<pk>\d+)/edit/$', views.sk_edit, name='sk_edit'),
    url(r'^sk/new/$', views.sk_new, name='sk_new'),
# --------------------------------------------------------------- Takrs (ta)
	url(r'^tkrs/$', views.tkrs_list, name='views.tkrs_list'),
	url(r'^tkrs/(?P<pk>\d+)/$', views.tkrs_detail, name='tkrs_detail'),
	url(r'^tkrs/(?P<pk>\d+)/edit/$', views.tkrs_edit, name='tkrs_edit'),
    url(r'^tkrs/new/$', views.tkrs_new, name='tkrs_new'),
# ---------------------------------------------------------- Matakuliah (mt)
	url(r'^mkul/$', views.mkul_list, name='views.mkul_list'),
	url(r'^mkul/(?P<pk>\d+)/$', views.mkul_detail, name='mkul_detail'),
	url(r'^mkul/(?P<pk>\d+)/edit/$', views.mkul_edit, name='mkul_edit'),
    url(r'^mkul/new/$', views.mkul_new, name='mkul_new'),
# ------------------------------------------------------- Tugasmengajar (tu)
	url(r'^tugm/$', views.tugm_list, name='views.tugm_list'),
	url(r'^tugm/(?P<pk>\d+)/$', views.tugm_detail, name='tugm_detail'),
	url(r'^tugm/(?P<pk>\d+)/edit/$', views.tugm_edit, name='tugm_edit'),
    url(r'^tugm/new/$', views.tugm_new, name='tugm_new'),
# ----------------------------------------------------------- Mahasiswa (ma)
	url(r'^maha/$', views.maha_list, name='views.maha_list'),
	url(r'^maha/(?P<pk>\d+)/$', views.maha_detail, name='maha_detail'),
	url(r'^maha/(?P<pk>\d+)/edit/$', views.maha_edit, name='maha_edit'),
    url(r'^maha/new/$', views.maha_new, name='maha_new'),
# ---------------------------------------------------------- Pembimbing (pe)
	url(r'^pemb/$', views.pemb_list, name='views.pemb_list'),
	url(r'^pemb/(?P<pk>\d+)/$', views.pemb_detail, name='pemb_detail'),
	url(r'^pemb/(?P<pk>\d+)/edit/$', views.pemb_edit, name='pemb_edit'),
    url(r'^pemb/new/$', views.pemb_new, name='pemb_new'),
# ----------------------------------------------------------- Kelulusan (ke)
	url(r'^kelu/$', views.kelu_list, name='views.kelu_list'),
	url(r'^kelu/(?P<pk>\d+)/$', views.kelu_detail, name='kelu_detail'),
	url(r'^kelu/(?P<pk>\d+)/edit/$', views.kelu_edit, name='kelu_edit'),
    url(r'^kelu/new/$', views.kelu_new, name='kelu_new'),
# ----------------------------------------------------------------- Krs (kr)
	url(r'^krs/$', views.krs_list, name='views.krs_list'),
	url(r'^krs/(?P<pk>\d+)/$', views.krs_detail, name='krs_detail'),
	url(r'^krs/(?P<pk>\d+)/edit/$', views.krs_edit, name='krs_edit'),
    url(r'^krs/new/$', views.krs_new, name='krs_new'),
# ----------------------------------------------------------------- Khs (kh)
	url(r'^khs/$', views.khs_list, name='views.khs_list'),
	url(r'^khs/(?P<pk>\d+)/$', views.khs_detail, name='khs_detail'),
	url(r'^khs/(?P<pk>\d+)/edit/$', views.khs_edit, name='khs_edit'),
    url(r'^khs/new/$', views.khs_new, name='khs_new'),
# -------------------------------------------------------------- Ijazah (ij)
	url(r'^ijaz/$', views.ijaz_list, name='views.ijaz_list'),
	url(r'^ijaz/(?P<pk>\d+)/$', views.ijaz_detail, name='ijaz_detail'),
	url(r'^ijaz/(?P<pk>\d+)/edit/$', views.ijaz_edit, name='ijaz_edit'),
    url(r'^ijaz/new/$', views.ijaz_new, name='ijaz_new'),
# ---------------------------------------------------------- Pembayaran (pb)
	url(r'^pbay/$', views.pbay_list, name='views.pbay_list'),
	url(r'^pbay/(?P<pk>\d+)/$', views.pbay_detail, name='pbay_detail'),
	url(r'^pbay/(?P<pk>\d+)/edit/$', views.pbay_edit, name='pbay_edit'),
    url(r'^pbay/new/$', views.pbay_new, name='pbay_new'),

	url(r'^info/$', views.info, name='views.info'),
]
