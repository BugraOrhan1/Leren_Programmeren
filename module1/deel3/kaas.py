
antwoordt_geel = input('is de kaas geel?(ja/nee)')
if antwoordt_geel == 'ja':
    antwoordt_gaten = input('zitten er gaten in?(ja/nee)')
    if antwoordt_gaten == 'ja':   
        antwoordt_duur = input('is de kaas belachelijk duur?')
        if antwoordt_duur == 'ja': 
            print('emmenthaler') 
        else:
            print('leerdammer')
    else:
        antwoordt_hard = input('is de kaas hard als steen?(ja/nee)')
        if antwoordt_hard == 'ja': 
            print('parmigiano reggiano') 
        else:
            print('goudse kaas')
else:
    antwoordt_schimmel = input('heeft de kaas blauwe schimmel?(ja/nee)')
    if antwoordt_schimmel == 'ja':   
        antwoordt_korst = input('heeft de kaas korst?')
        if antwoordt_korst == 'ja': 
            print('blue de rochbaron') 
        else:
            print("foume da'ambert")
    else:
        antwoordt_korst_1 = input('heeft de kaas korst?(ja/nee)')
        if antwoordt_korst_1 == 'ja': 
            stinkt = input('stinkt die?(ja/nee)')
            if stinkt == 'ja':
                print('camenbert') 
            else :
                print('brie')
        else:
            print('mozzarella ')

     




