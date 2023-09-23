meme_dict = {
            "CRINGE":"Garip ya da utandırıcı bir şey",
            "LOL":"Komik bir şeye verilen cevap",
            "ARGO":"Kaba ve küfürlü bir dil olarak bilinir",
            "DR":"Tıp alanında uzmanlık veya doktora çalışmalarını tamamlamış tabiplere (hekimlere) verilen unvandır.",
            "TBMM":"Tıp alanında uzmanlık veya doktora çalışmalarını tamamlamış tabiplere (hekimlere) verilen unvandır.",
            "MEB":"MİLLİ EĞİTİM BAKANLIGI.",
            "TDK":"TÜRK DİL KURUMU.",
            "PROF":"Profesör .",
            "DOÇ":" Doçent.",
            "MAH":"MAHALLE.",
}
word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    
if word in meme_dict.keys():
    print(meme_dict[word]),"kelimenin anlamıdır"
    # Kelime eşleşiyorsa ne yapmalıyız?
else:
    print("kelime bulunamadi")
    # Kelime eşleşmiyorsa ne yapmalıyız?
