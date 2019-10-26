# reportlab_qrcode
reportlab_qrcode

```console
virtualenv reportlab
source reportlab/bin/activate

pip install reportlab
```

## Edit page layour

> /home/soiqualang/programing/python/reportlab/lib/python3.6/site-packages/reportlab/lib/pagesizes.py

```python
C0 = (917*mm,1297*mm)
C1 = (648*mm,917*mm)
C2 = (458*mm,648*mm)
C3 = (324*mm,458*mm)
C4 = (229*mm,324*mm)
C5 = (162*mm,229*mm)
C6 = (114*mm,162*mm)
C7 = (81*mm,114*mm)
C8 = (57*mm,81*mm)
C9 = (40*mm,57*mm)
C10 = (28*mm,40*mm)
#3 tem
QRCode = (110*mm,75*mm)

#American paper sizes
LETTER = (8.5*inch, 11*inch)
LEGAL = (8.5*inch, 14*inch)
ELEVENSEVENTEEN = (11*inch, 17*inch)

QRCodeInch = (4.33070866*inch,2.95275591*inch)

# From https://en.wikipedia.org/wiki/Paper_size
JUNIOR_LEGAL = (5*inch, 8*inch)
```


## References

http://www.blog.pythonlibrary.org/2013/03/25/reportlab-how-to-create-barcodes-in-your-pdfs-with-python/

http://www.blog.pythonlibrary.org/2010/09/21/reportlab-tables-creating-tables-in-pdfs-with-python/

