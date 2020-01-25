#author: Karol Schewe


from crawler_2011 import crawl_2011

sejm_df, turnout_df, senat_df = crawl_2011()
print(sejm_df.to_string())
sejm_df.to_csv("wybory_do_sejmu_2011_po_gminach_wyniki.csv", index=False, encoding='utf-8-sig')
turnout_df.to_csv("frekwencja_wybory_2011_po_gminach.csv", index=False, encoding='utf-8-sig')
senat_df.to_csv("wybory_do_senatu_2011_po_gminach_wyniki.csv", index=False, encoding='utf-8-sig')














