temperaturas = [[28, 31, 34, 33],
                [25, 27, 29, 28],
                [32, 35, 36, 34],
                [24, 26, 25, 27]
                ]
risco =0
nSala = 0
maiorMedia = 0

for temperatura in temperaturas:
    nSala =nSala+1
    temp = 0
    crit = 0
    for info in temperatura:
        temp = info + temp
        media = temp/4
        if(info>=33):
            crit = crit+1
        if(media>=33):
            if(media>maiorMedia):
                risco = nSala
                maiorMedia=media
    print("Sala:", nSala)
    print("Média:", media)
    print("Registros críticos:", crit)
    print()

print()
print()
print("Sala com maior risco: Sala", risco)