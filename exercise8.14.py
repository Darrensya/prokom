def bwtMbl(manufacturer, model, **infombl):

    mbl = {'manufacturer': manufacturer, 'model': model}
    mbl.update(infombl)
    return mbl


mbl = bwtMbl('subaru', 'outback', color='blue', tow_package=True)
print(mbl)