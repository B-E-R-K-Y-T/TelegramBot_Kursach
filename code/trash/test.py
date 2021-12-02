from code.API import postgresql as ps

ps.inquiry_to_db("""SELECT examples
   FROM public.hello
   ORDER BY examples DESC
   OFFSET 0 ROWS FETCH NEXT 3 ROWS ONLY;""", flag=True)
