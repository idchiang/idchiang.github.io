__rethrow_casa_exceptions = True
h_init()
try:
    hifv_restoredata (vis=['14B-396.sb29809142.eb30014592.56987.35765355324'], session=['session_1'], ocorr_mode='co', gainmap=False)
    hifv_statwt()
finally:
    h_save()
