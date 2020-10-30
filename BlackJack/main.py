import random
print("Bienvenido al juego de BlackJack.\n")
print("Le repartire dos cartas, recuerde que si tiene 21 es blackjack y si supera 21 es bust y gana la casa.\n")
carta1=random.randint(1,11)
carta2=random.randint(1,10)
carta3=random.randint(1,10)
carta4=random.randint(1,10)
carta5=random.randint(1,10)
carta6=random.randint(1,10)
carta7=random.randint(1,10)
carta8=random.randint(1,10)
carta1casa=random.randint(1,11)
carta2casa=random.randint(1,10)
carta3casa=random.randint(1,10)
carta4casa=random.randint(1,10)
carta5casa=random.randint(1,10)
carta6casa=random.randint(1,10)
carta7casa=random.randint(1,10)
carta8casa=random.randint(1,10)
sumacartascasa=carta1casa+carta2casa
sumacartasj=carta1+carta2
dinero=int(input("Inserte su dinero en numero entero: "))
pierde=sumacartascasa>sumacartasj
gana=sumacartasj>sumacartascasa
empate=sumacartasj==sumacartascasa
print("Sus cartas son: ",carta1,',',carta2,"que son",sumacartasj)
print("La cartas de la casa son: ", carta1casa,',',carta2casa,"que son",sumacartascasa)
if sumacartasj==21 and sumacartascasa==21:
    print("Usted gana al tener BlackJack")
    gana
if sumacartascasa == 21 and sumacartasj<21:
    print("La casa tiene BlackJack por tanto ha ganado.")
    gana
if sumacartasj == 21:
    print("Usted tiene Blackjack")
    gana
else:
    print("Usted tiene", sumacartasj)
choice1j=input("¿Desea recibir una carta?> (y/n)")
if choice1j=='y':
    sumacartasj=carta1+carta2+carta3
    print("usted cogio una carta más, por tanto tiene: ", carta1,',',carta2,',',carta3 ,"y su suma es",sumacartasj)
    if sumacartasj>21:
        print("Vaya se ha pasado, la casa gana.")
        pierde
    elif sumacartasj<21:
        print("Usted tiene:", sumacartasj)
        choice2j=input("¿Desea recibir otra carta?>(y/n)")
        if choice2j=='y':
            sumacartasj=carta1+carta2+carta3+carta4
            print("Usted tiene:", sumacartasj)
            if sumacartasj>21:
                 print("Vaya se ha pasado, la casa gana.")
                 pierde
            elif sumacartasj==21:
                 print("Wow usted tiene 21, que afortunado")
                 gana
            elif sumacartasj<21:
                 print("Usted tiene:", sumacartasj)
                 choice3j=input("¿Desea recibir otra carta?>(y/n)")
                 if choice3j=='y':
                     sumacartasj=carta1+carta2+carta3+carta4+carta5
                     print("Usted tiene:", sumacartasj)
                 if sumacartasj>21:
                     print("Vaya se ha pasado, la casa gana.")
                     pierde
                 elif sumacartasj==21:
                      print("Wow usted tiene 21, que afortunado")
                      gana
                 elif sumacartasj<21:
                      print("Usted tiene:", sumacartasj)
                      choice4j=input("¿Desea recibir otra carta?>(y/n)")
                      if choice4j=='y':
                          sumacartasj=carta1+carta2+carta3+carta4+carta5
                          print("Usted tiene:", sumacartasj)
                      if sumacartasj>21:
                          print("Vaya se ha pasado, la casa gana.")
                          pierde
                      elif sumacartasj==21:
                           print("Wow usted tiene 21, que afortunado")
                           gana
                      elif sumacartasj<21:
                           print("Usted tiene:", sumacartasj)
                           choice5j=input("¿Desea recibir otra carta?>(y/n)")
                           if choice5j=='y':
                              sumacartasj=carta1+carta2+carta3+carta4+carta5+carta6
                              print("Usted tiene:", sumacartasj)
                           if sumacartasj>21:
                              print("Vaya se ha pasado, la casa gana.")
                              pierde
                           elif sumacartasj==21:
                              print("Wow usted tiene 21, que afortunado")
                              gana
                           elif sumacartasj<21:
                              print("Usted tiene:", sumacartasj)
                              choice6j=input("¿Desea recibir otra carta?>(y/n)")
                              if choice6j=='y':
                                sumacartasj=carta1+carta2+carta3+carta4+carta5+carta6+carta7
                                print("Usted tiene:", sumacartasj)
                              if sumacartasj>21:
                                print("Vaya se ha pasado, la casa gana.")
                                pierde
                              elif sumacartasj==21:
                                print("Wow usted tiene 21, que afortunado")
                                gana
                              elif sumacartasj<21:
                                print("Usted tiene:", sumacartasj)
                                choice7j=input("¿Desea recibir otra carta?>(y/n)")
                                if choice7j=='y':
                                  sumacartasj=carta1+carta2+carta3+carta4+carta5+carta6+carta7+carta8
                                  print("Usted tiene:", sumacartasj)
                                if sumacartascasa<17:
                                    sumacartascasa=carta1casa+carta2casa+carta3casa
                                    if sumacartascasa<17:
                                       sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa
                                       if sumacartascasa<17:
                                          sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa+carta5casa
                                          if sumacartascasa<17:
                                             sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa+carta5casa+carta6casa
                                             if sumacartascasa<17:
                                                sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa+carta5casa+carta6casa+carta7casa
                                             if sumacartascasa<17:
                                                sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa+carta5casa+carta6casa+carta7casa+carta8casa
                                if sumacartasj>21:
                                  print("Vaya se ha pasado, la casa gana.")
                                  pierde
                                elif sumacartasj==21:
                                  print("Wow usted tiene 21, que afortunado")
                                  gana
                                elif sumacartasj==21 and sumacartascasa==21:
                                   print("Wow usted tiene 21, que afortunado")
                                   gana
                                elif sumacartasj==21 and sumacartascasa<21:
                                   print("Wow usted tiene 21, que afortunado")
                                   gana
                                elif sumacartasj<21 and sumacartascasa==21:
                                   print("La casa tiene",sumacartascasa,"usted ha perdido.")
                                   pierde
                                elif sumacartascasa>21:
                                   print("La casa se ha pasado y tiene",sumacartascasa)
                                   gana
                                elif sumacartasj<sumacartascasa:
                                   print("La casa tiene",sumacartascasa,"y usted tiene",sumacartasj,"ha perdido.")
                                   pierde
                                elif sumacartasj<21 and sumacartasj>sumacartascasa:
                                   print("La casa tiene",sumacartascasa,"y usted tiene",sumacartasj,"ha ganado.")
                                   gana

                           else:
                             print("Usted tiene:", sumacartasj)
                             if sumacartascasa<17:
                                   sumacartascasa=carta1casa+carta2casa+carta3casa
                                   if sumacartascasa<17:
                                       sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa
                                       if sumacartascasa<17:
                                          sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa+carta5casa
                                          if sumacartascasa<17:
                                             sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa+carta5casa+carta6casa
                                             if sumacartascasa<17:
                                                sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa+carta5casa+carta6casa+carta7casa
                                             if sumacartascasa<17:
                                                sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa+carta5casa+carta6casa+carta7casa+carta8casa
                             if sumacartasj>21:
                                  print("Vaya se ha pasado, la casa gana.")
                                  pierde
                             elif sumacartasj==21:
                                  print("Wow usted tiene 21, que afortunado")
                                  gana
                             elif sumacartasj==21 and sumacartascasa==21:
                                   print("Wow usted tiene 21, que afortunado")
                                   gana
                             elif sumacartasj==21 and sumacartascasa<21:
                                   print("Wow usted tiene 21, que afortunado")
                                   gana
                             elif sumacartasj<21 and sumacartascasa==21:
                                   print("La casa tiene",sumacartascasa,"usted ha perdido.")
                                   pierde
                             elif sumacartascasa>21:
                                   print("La casa se ha pasado y tiene",sumacartascasa)
                                   gana
                             elif sumacartasj<sumacartascasa:
                                   print("La casa tiene",sumacartascasa,"y usted tiene",sumacartasj,"ha perdido.")
                                   pierde
                             elif sumacartasj<21 and sumacartasj>sumacartascasa:
                                   print("La casa tiene",sumacartascasa,"y usted tiene",sumacartasj,"ha ganado.")
                                   gana

                      else:
                           print("Usted tiene:", sumacartasj)
                           if sumacartascasa<17:
                                   sumacartascasa=carta1casa+carta2casa+carta3casa
                                   if sumacartascasa<17:
                                       sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa
                                       if sumacartascasa<17:
                                          sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa+carta5casa
                                          if sumacartascasa<17:
                                             sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa+carta5casa+carta6casa
                                             if sumacartascasa<17:
                                                sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa+carta5casa+carta6casa+carta7casa
                                             if sumacartascasa<17:
                                                sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa+carta5casa+carta6casa+carta7casa+carta8casa
                           if sumacartasj>21:
                                  print("Vaya se ha pasado, la casa gana.")
                                  pierde
                           elif sumacartasj==21:
                                  print("Wow usted tiene 21, que afortunado")
                                  gana
                           elif sumacartasj==21 and sumacartascasa==21:
                                   print("Wow usted tiene 21, que afortunado")
                                   gana
                           elif sumacartasj==21 and sumacartascasa<21:
                                   print("Wow usted tiene 21, que afortunado")
                                   gana
                           elif sumacartasj<21 and sumacartascasa==21:
                                   print("La casa tiene",sumacartascasa,"usted ha perdido.")
                                   pierde
                           elif sumacartascasa>21:
                                   print("La casa se ha pasado y tiene",sumacartascasa)
                                   gana
                           elif sumacartasj<sumacartascasa:
                                   print("La casa tiene",sumacartascasa,"y usted tiene",sumacartasj,"ha perdido.")
                                   pierde
                           elif sumacartasj<21 and sumacartasj>sumacartascasa:
                                   print("La casa tiene",sumacartascasa,"y usted tiene",sumacartasj,"ha ganado.")
                                   gana

                 else:
                    print("Usted tiene:", sumacartasj)
                    if sumacartascasa<17:
                                   sumacartascasa=carta1casa+carta2casa+carta3casa
                                   if sumacartascasa<17:
                                       sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa
                                       if sumacartascasa<17:
                                          sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa+carta5casa
                                          if sumacartascasa<17:
                                             sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa+carta5casa+carta6casa
                                             if sumacartascasa<17:
                                                sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa+carta5casa+carta6casa+carta7casa
                                             if sumacartascasa<17:
                                                sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa+carta5casa+carta6casa+carta7casa+carta8casa
                    if sumacartasj>21:
                                  print("Vaya se ha pasado, la casa gana.")
                                  pierde
                    elif sumacartasj==21:
                                  print("Wow usted tiene 21, que afortunado")
                                  gana
                    elif sumacartasj==21 and sumacartascasa==21:
                                   print("Wow usted tiene 21, que afortunado")
                                   gana
                    elif sumacartasj==21 and sumacartascasa<21:
                                   print("Wow usted tiene 21, que afortunado")
                                   gana
                    elif sumacartasj<21 and sumacartascasa==21:
                                   print("La casa tiene",sumacartascasa,"usted ha perdido.")
                                   pierde
                    elif sumacartascasa>21:
                                   print("La casa se ha pasado y tiene",sumacartascasa)
                                   gana
                    elif sumacartasj<sumacartascasa:
                                   print("La casa tiene",sumacartascasa,"y usted tiene",sumacartasj,"ha perdido.")
                                   gana
                    elif sumacartasj<21 and sumacartasj>sumacartascasa:
                                   print("La casa tiene",sumacartascasa,"y usted tiene",sumacartasj,"ha ganado.")
                                   gana

            else:
                print("Usted tiene:", sumacartasj)
                if sumacartascasa<17:
                                   sumacartascasa=carta1casa+carta2casa+carta3casa
                                   if sumacartascasa<17:
                                       sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa
                                       if sumacartascasa<17:
                                          sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa+carta5casa
                                          if sumacartascasa<17:
                                             sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa+carta5casa+carta6casa
                                             if sumacartascasa<17:
                                                sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa+carta5casa+carta6casa+carta7casa
                                             if sumacartascasa<17:
                                                sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa+carta5casa+carta6casa+carta7casa+carta8casa
                if sumacartasj>21:
                                  print("Vaya se ha pasado, la casa gana.")
                                  pierde
                elif sumacartasj==21:
                                  print("Wow usted tiene 21, que afortunado")
                                  gana
                elif sumacartasj==21 and sumacartascasa==21:
                                   print("Wow usted tiene 21, que afortunado")
                                   gana
                elif sumacartasj==21 and sumacartascasa<21:
                                   print("Wow usted tiene 21, que afortunado")
                                   gana
                elif sumacartasj<21 and sumacartascasa==21:
                                   print("La casa tiene",sumacartascasa,"usted ha perdido.")
                                   pierde
                elif sumacartascasa>21:
                                   print("La casa se ha pasado y tiene",sumacartascasa)
                                   gana
                elif sumacartasj<sumacartascasa:
                                   print("La casa tiene",sumacartascasa,"y usted tiene",sumacartasj,"ha perdido.")
                                   pierde
                elif sumacartasj<21 and sumacartasj>sumacartascasa:
                                   print("La casa tiene",sumacartascasa,"y usted tiene",sumacartasj,"ha ganado.")
                                   gana

        else:
            if sumacartascasa<17:
                                   sumacartascasa=carta1casa+carta2casa+carta3casa
                                   if sumacartascasa<17:
                                       sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa
                                       if sumacartascasa<17:
                                          sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa+carta5casa
                                          if sumacartascasa<17:
                                             sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa+carta5casa+carta6casa
                                             if sumacartascasa<17:
                                                sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa+carta5casa+carta6casa+carta7casa
                                             if sumacartascasa<17:
                                                sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa+carta5casa+carta6casa+carta7casa+carta8casa
            print("Usted tiene:", sumacartasj)
            if sumacartasj>21:
                                  print("Vaya se ha pasado, la casa gana.")
                                  pierde
            elif sumacartasj==21:
                                  print("Wow usted tiene 21, que afortunado")
                                  gana
            elif sumacartasj==21 and sumacartascasa==21:
                                   print("Wow usted tiene 21, que afortunado")
                                   gana
            elif sumacartasj==21 and sumacartascasa<21:
                                   print("Wow usted tiene 21, que afortunado")
                                   gana
            elif sumacartasj<21 and sumacartascasa==21:
                                   print("La casa tiene",sumacartascasa,"usted ha perdido.")
                                   pierde
            elif sumacartascasa>21:
                                   print("La casa se ha pasado y tiene",sumacartascasa)
                                   gana
            elif sumacartasj<sumacartascasa:
                                   print("La casa tiene",sumacartascasa,"y usted tiene",sumacartasj,"ha perdido.")
                                   pierde
            elif sumacartasj<21 and sumacartasj>sumacartascasa:
                                   print("La casa tiene",sumacartascasa,"y usted tiene",sumacartasj,"ha ganado.")
                                   gana

    else:
        if sumacartascasa<17:
            sumacartascasa=carta1casa+carta2casa+carta3casa
            if sumacartascasa<17:
               sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa
               if sumacartascasa<17:
                  sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa+carta5casa
                  if sumacartascasa<17:
                     sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa+carta5casa+carta6casa
                     if sumacartascasa<17:
                        sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa+carta5casa+carta6casa+carta7casa
                        if sumacartascasa<17:
                           sumacartascasa=carta1casa+carta2casa+carta3casa+carta4casa+carta5casa+carta6casa+carta7casa+carta8casa
        if sumacartasj>21:
                                  print("Vaya se ha pasado, la casa gana.")
                                  pierde
        elif sumacartasj==21:
                                  print("Wow usted tiene 21, que afortunado")
                                  gana
        elif sumacartasj==21 and sumacartascasa==21:
                                   print("Wow usted tiene 21, que afortunado")
                                   gana
        elif sumacartasj==21 and sumacartascasa<21:
                                   print("Wow usted tiene 21, que afortunado")
                                   gana
        elif sumacartasj<21 and sumacartascasa==21:
                                   print("La casa tiene",sumacartascasa,"usted ha perdido.")
                                   pierde
        elif sumacartascasa>21:
                                   print("La casa se ha pasado y tiene",sumacartascasa)
                                   gana
        elif sumacartasj<sumacartascasa:
                                   print("La casa tiene",sumacartascasa,"y usted tiene",sumacartasj,"ha perdido.")
                                   pierde
        elif sumacartasj<21 and sumacartasj>sumacartascasa:
                                   print("La casa tiene",sumacartascasa,"y usted tiene",sumacartasj,"ha ganado.")
                                   gana

else:
  print("Usted tiene:", sumacartasj)
  if sumacartasj>21:
       print("Vaya se ha pasado, la casa gana.")
       pierde
  elif sumacartasj==21:
         print("Wow usted tiene 21, que afortunado")
         gana
  elif sumacartasj==21 and sumacartascasa==21:
         print("Wow usted tiene 21, que afortunado")
         gana
  elif sumacartasj==21 and sumacartascasa<21:
         print("Wow usted tiene 21, que afortunado")
         gana
  elif sumacartasj<21 and sumacartascasa==21:
         print("La casa tiene",sumacartascasa,"usted ha perdido.")
         pierde
  elif sumacartascasa>21:
         print("La casa se ha pasado y tiene",sumacartascasa)
         gana
  elif sumacartasj<sumacartascasa:
         print("La casa tiene",sumacartascasa,"y usted tiene",sumacartasj,"ha perdido.")
         pierde
  elif sumacartasj<21 and sumacartasj>sumacartascasa:
         print("La casa tiene",sumacartascasa,"y usted tiene",sumacartasj,"ha ganado.")
         pierde
if gana:
    dinero=dinero*2
    print("Usted tiene ahora:",dinero)
elif empate:
    dinero=dinero
    print("Usted tiene ahora:",dinero)
elif pierde:
    dinero=dinero/2
    print("Usted tiene ahora:",dinero)
if sumacartascasa<17:
    sumacartascasa=carta1casa+carta2casa+carta3casa
input("Pulsa ENTER para cerrar el juego.")
