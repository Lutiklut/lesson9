from random import choice
import copy
import re
import random
import dict


class Card:

    def __init__(self):
        self.coloda = {1: '6♥', 2: '7♥', 3: '8♥', 4: '9♥', 5: '10♥', 6: 'J♥', 7: 'Q♥', 8: 'K♥', 9: 'A♥',
                  10: '6♦', 11: '7♦', 12: '8♦', 13: '9♦', 14: '10♦', 15: 'J♦', 16: 'Q♦', 17: 'K♦', 18: 'A♦',
                  19: '6♠', 20: '7♠', 21: '8♠', 22: '9♠', 23: '10♠', 24: 'J♠', 25: 'Q♠', 26: 'K♠', 27: 'A♠',
                  28: '6♣', 29: '7♣', 30: '8♣', 31: '9♣', 32: '10♣', 33: 'J♣', 34: 'Q♣', 35: 'K♣', 36: 'A♣'}
        self.coloda_cherv= {1: '6♥', 2: '7♥', 3: '8♥', 4: '9♥', 5: '10♥', 6: 'J♥', 7: 'Q♥', 8: 'K♥', 9: 'A♥'}
        self.coloda_bubi = {1: '6♦', 2: '7♦', 3: '8♦', 4: '9♦', 5: '10♦', 6: 'J♦', 7: 'Q♦', 8: 'K♦', 9: 'A♦'}
        self.coloda_vinni= {1: '6♠', 2: '7♠', 3: '8♠', 4: '9♠', 5: '10♠', 6: 'J♠', 7: 'Q♠', 8: 'K♠', 9: 'A♠'}
        self.coloda_kresti={1: '6♣', 2: '7♣', 3: '8♣', 4: '9♣', 5: '10♣', 6: 'J♣', 7: 'Q♣', 8: 'K♣', 9: 'A♣'}



    def __razdacha__(self):  # раздача карт
        n=list(self.coloda.keys())
        player1=[]
        player2 = []
        player_1 = []
        player_2 = []
        for i in range(6):  # ключи карт 1 игрока
            d = random.choice(n)
            player1.append(d)
            n.remove(d)

        for i in range(6): # ключи карт 2 игрока
            d = random.choice(n)
            player2.append(d)
            n.remove(d)

        koz = random.choice(n) # ключ козырная карта

        for i in player1:
            p1=(self.coloda.get(i))
            player_1.append(p1)
        for i in player2:
            p2=(self.coloda.get(i))
            player_2.append(p2)

        kozir=self.coloda.get(koz)


        return n, player1,player2, koz,player_1,player_2, kozir #n- ключи карт в колоде, player1-ключи карт игрока 1,,player2
        # , koz-ключ козырной карты ,player_1-значение карт игрока 1,player_2, kozir-значение козыря


    def __card_players(self):
       rez=self.__razdacha__()
       new_coloda_key=list(self.coloda)
       new_coloda_value=list(self.coloda.values())
       new_coloda={}
       k=0
       j=0
       d=0
       g=0
       koz=rez[3]
       carts=rez[0]
       if int(koz) in {1,2,3,4,5,6,7,8,9}:
           for i in new_coloda_key:
               if int(i) < 10:
                   new_coloda_key[k] = int(i) * 100
               k += 1
           for i in carts:
               if int(i) <10:
                  carts[j] =int(i)*100
               j += 1
           for i in rez[1]:
                   if int(i) < 10:
                       rez[1][g] = int(i) * 100
                   g += 1
           for i in rez[2]:
               if int(i) < 10:
                   rez[2][d] = int(i) * 100
               d += 1

       elif int(koz)>9 and int(koz)<19:
            for i in ( carts):
               if int(i) >9 and int (i)<19:
                    carts[k] = int(i) * 100
               k += 1
            for i in ( new_coloda_key):
               if int(i) >9 and int (i)<19:
                    new_coloda_key[j] = int(i) * 100
               j += 1
            for i in rez[1]:
               if int(i) >9 and int (i)<19:
                     rez[1][d] = int(i) * 100
               d += 1
            for i in rez[2]:
                   if int(i) >9 and int (i)<19:
                       rez[2][g] = int(i) * 100
                   g += 1

       elif int(koz)>18 and int(koz)<28:
           for i in (carts):
               if int(i) > 18 and int(i) < 28:
                   carts[k] = int(i) * 100
               k += 1
           for i in (new_coloda_key):
               if int(i) > 18 and int(i) < 28:
                   new_coloda_key[j] = int(i) * 100
               j += 1
           for i in rez[1]:
               if int(i) > 18 and int(i) < 28:
                   rez[1][d] = int(i) * 100
               d += 1
           for i in rez[2]:
               if int(i) > 18 and int(i) < 28:
                   rez[2][g] = int(i) * 100
               g += 1
       elif int(koz)>27 and int(koz)<37:
           for i in (carts):
               if int(i) > 27:
                   carts[k] = int(i) * 100
               k += 1
           for i in (new_coloda_key):
               if int(i) > 27:
                   new_coloda_key[j] = int(i) * 100
               j += 1
           for i in rez[1]:
               if int(i) > 27:
                   rez[1][d] = int(i) * 100
               d += 1
           for i in rez[2]:
               if int(i) > 27:
                   rez[2][g] = int(i) * 100
               g += 1

       koz = int(koz) * 100

       for x, y in zip(new_coloda_key,new_coloda_value):
           new_coloda[x] = y


       min1 = 10000
       min2 = 10000
       for i in rez[1]:
           if int(i) % 100 == 0:
               if int(i) < min1:
                   min1 = i

       for i in rez[2]:
           if int(i) % 100 == 0:
               if i < min2:
                   min2 = i
       if (min2 == 10000) and (min1 == 10000):
           print(' У игроков нет козырей, ходит игрок 1')
           player = 1
       elif min1 < min2:
           print(" У игрока 1 есть минимальный козырь и он ходит первым")
           player = 1
       else:
           print(" У игрока 2 есть минимальный козырь и он ходит первым")
           player = 2


       ostatok_colod = []# оставшиеся карты после раздачи
       ostatok_1 = {}
       for i in carts:
           p = (new_coloda.get(i))
           ostatok_colod.append(p)
       for x, y in zip(carts, ostatok_colod):
           ostatok_1[x] = y


       random.shuffle(carts)

       ostatok_random = {}
       for key in carts:
           ostatok_random.update({key: ostatok_1[key]})


       return carts  ,new_coloda,rez[1],rez[2],player,koz, rez[4],rez[5],rez[6],ostatok_colod, ostatok_1,ostatok_random
       # rez[1]-keys              -0
       # player 1,rez[2]-player2, -1,2,3
       # player-number player     -4
       # ,rez[3]-kozir             -5
       # rez[4],rez[5]-raskladka   -6,7
       # rez[6]-значение козыря    -8
       #ostatok_colod,             -9
       # ostatok_1,               -10
       # ostatok_random             11








    @property
    def game(self):  #сделать ход input?

      b=self.__card_players()
      a=int(b[4])
      print(" Карты игрока 1-", b[6], '\n', "Карты игрока 2-", b[7], '\n', "Козырная масть-", b[8],b[5])
      print(" ход ", a ," игрока")


      def min_card_in_coloda_player(a):
          min1 = 10
          min2 = 10
          min3 = 10
          min4 = 10
          k_ch = 0
          k_b = 0
          k_v = 0
          k_k = 0
          for i in a:

             for key, value in self.coloda_cherv.items():
                if i ==value:
                      if min1 > int(key):
                          min1 = int(key)
                          k_ch=i

             for key, value in self.coloda_bubi.items():
                 if i == value:
                      if min2 > int(key):
                         min2 = int(key)
                         k_b=i

             for key, value in self.coloda_vinni.items():
                 if i == value:
                      if min3 > int(key):
                         min3 = int(key)
                         k_v=i
             for key, value in self.coloda_kresti.items():
                             if i == value:
                                 if min4 > int(key):
                                     min4 = int(key)
                                     k_k=i


          list_min = [min1, min2, min3, min4]
          list_kart=[k_ch,k_b,k_v,k_k]
          minkart=[]
          for i in range(4):
              minkart.append([list_min[i],list_kart[i]])

          list_min.sort()
          min5=[]
          for i in list_min:
              if i== list_min[0]:
                  min5.append(i)
          #print(min5,'throw')
          min5_v=[]

         # for g in min5:
          for i in minkart: # не должно быть у одного ключа несколько значениц

           if int (i[0])==int(min5[0]):
                a=i[1]
                min5_v.append(a) #должно быть значение
          #print(min5_v,'znachrnie mina')
          return min5_v

      def min_dict(a,b): # словарь из мин значений в колоде игрока a=self.card_players()[1]),b=min5_v
          player={}
          list_key=[]
          list_valye=[]
          for j in b:
              for key,value in a.items():
                 if j==value:
                     list_key.append(key)
                     list_valye.append(value)
          for x, y in zip(list_key, list_valye):
              player[x] = y
          return player

      if a==1:
           min_card_in_coloda_player_g=min_card_in_coloda_player(b[6])
      else:
           min_card_in_coloda_player_g = min_card_in_coloda_player(b[7])

      mim_dict=min_dict(b[1],min_card_in_coloda_player_g)


     # for i,j in min5_dict:
      #  for k,val in self.card_players()[1].items():
       #     if j==val:
         #       if k< 37:

            #        print ("сбросить карту",)

      def proverka (mim_d,a): #проверка не является ли минимальная карта козырем (подаем    и а)
          coloda_p=[]
          v=[]
          mim={}
          values=[]
          keys=sorted(mim_d.keys(),reverse=True)
          print(keys)
          for i in keys:
              values.append(mim_d[i])
          #    mim={i:mim_d[i]}


          for x, y in zip(keys,values):
              mim[x] = y
          print("dict sort",mim)

          if a==1:
            coloda_p=b[6]
          else:
            coloda_p=b[7]

          for key,value in mim.items():
              if key>100 or key==100:

                 v=value
                 coloda_p.remove(v)
                 print(coloda_p,'новая раскладка без козыря')
                 min_card_in_coloda_player_g = min_card_in_coloda_player(coloda_p)
                 return min_card_in_coloda_player_g
              else:
                  print("it`s Ok. you can play", b[3],b[7])

                  min_card_in_coloda_player_g = min_card_in_coloda_player(coloda_p)
                  return    min_card_in_coloda_player_g

      proverka_min=proverka(mim_dict,a)

      new_min_dict=min_dict(b[1],proverka_min)
      print(list(new_min_dict.values()),'- хожу')

      def game_begin(mim,a): # подаю минимальный словарь карт в колоде игрока new_min_dict и номер игрока деелающего первый ход (а)
          coloda_p = []
          coloda_p_k=[]
          v = []
          k=0
          if a == 1:
              coloda_p = b[6]
              coloda_p_k=b[2]
          else:
              coloda_p = b[7]
              coloda_p_k=b[3]

          for key,value in mim.items():  # в цикле осуществляется вырезание карт из раскладки игрока делающего первый ход
               for i in coloda_p:
                   if value==i:
                       coloda_p.remove(i)
                       coloda_p_k.remove(key)
          return coloda_p ,coloda_p_k

      sbros_kart=game_begin(new_min_dict,a)
    #  player={}
    #  for x, y in zip(b[2], b[6]):
   #       player[x] = y
   #   print(player,'-')

      def answer (mim,a): # ответ игрока подаем сброшенные карты new_min_dict и а-ход первого игрока,
          player={}
          player_get={}
          new_player={}
          coloda_ostatok=b[11]

          dict_pop={}
          coloda_p=[]
          coloda_p_k=[]
          dict_rem={}
          d_r={}

          if a != 1:
              coloda_p = b[6]
              coloda_p_k = b[2]

          else:
              coloda_p = b[7]
              coloda_p_k = b[3]
          for x, y in zip(coloda_p_k,coloda_p ):
              player[x] = y
          for key, value in mim.items():  # в цикле осуществляется вырезание карт из раскладки игрока делающего первый ход

              for i,j in player.items():
                  if int(key) in {1, 2, 3, 4, 5, 6, 7, 8, 9}  and int(i)in {1, 2, 3, 4, 5, 6, 7, 8, 9}:# or int(i) in {100, 200, 300, 400, 500, 600, 700, 800, 900} and int(key) in {100, 200, 300, 400, 500, 600, 700, 800, 900} :
                    if key < i:
                      coloda_p.remove(j)
                      coloda_p_k.remove(i)
                      new_player.setdefault(i,j)
                      d_r={key:value}
                      dict_rem.update(d_r)
                    break


              for i, j in player.items():
                  if int(key)  in {10, 11, 12, 13, 14, 15, 16, 17, 18} and int(i) in {10, 11, 12, 13, 14, 15, 16, 17, 18}:#  or int(key) in {1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800} and int(i) in {1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 18000} :
                      if key < i:
                          coloda_p.remove(j)
                          coloda_p_k.remove(i)
                          new_player.setdefault(i, j)
                          d_r = {key: value}
                          dict_rem.update(d_r)
                      break
              for i, j in player.items():
                  if int(key) in {19, 20, 21, 22, 23, 24, 25, 26, 27} and int(i) in {19, 20, 21, 22, 23, 24, 25, 26, 27}:#  or int(i) in {1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600,2700} and int(key) in {1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600,2700}:
                      if key < i:
                          coloda_p.remove(j)
                          coloda_p_k.remove(i)
                          new_player.setdefault(i, j)
                          d_r = {key: value}
                          dict_rem.update(d_r)
                      break

              for i, j in player.items():
                  if int(key) in {28, 29, 30, 31, 32, 33, 34, 35, 36} and int(i) in {28, 29, 30, 31, 32, 33, 34, 35, 36}:# or int(i)  in {2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600} and int(key)  in {2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600} :
                      if key < i:
                          coloda_p.remove(j)
                          coloda_p_k.remove(i)
                          new_player.setdefault(i, j)
                          d_r = {key: value}
                          dict_rem.update(d_r)
                      break

          if int(len(new_player)) == int(len(mim)):
              print(list(new_player.values()), '- бью')
      #        for key, value in mim.items():
        #          for i, j in player.items():


          elif int(len(new_player))<int(len(mim)):
              d={}

              if int(len(dict_rem))!=0:
                  for q,w in dict_rem.items():
                      for g,h in mim.items():
                         if w==h:
                            d=mim.pop(q)

              else:d=mim



              for key, value in d.items():  # в цикле осуществляется вырезание карт из раскладки игрока делающего первый ход

                  for i, j in player.items():
                      if int(i) in {100, 200, 300, 400, 500, 600, 700, 800, 900} or  int(i) in {1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800} or int(i)  in {1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600,2700} or int(i)   in {2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600}:

                          coloda_p.remove(j)
                          coloda_p_k.remove(i)
                          new_player.setdefault(i, j)
                          if int(len(new_player)) == int(len(mim)):
                             print(list(new_player.values()), '- бью')
                          break

                  if int(len(new_player)) < int(len(mim)):
                          print('ЗАБИРАЮ КАРТЫ')
                          player.update(mim)
                          print(player.values(), "-карты игрока,под которого ходили")
                          ar = coloda_ostatok.popitem()

                          for i in range(int(len(mim))):  # добавить карты из колоды игроку, начинавшему ход
                              ar = coloda_ostatok.popitem()
                              dict_pop.update({ar[0]: ar[1]})
                          if a == 1:
                              coloda_p = b[6]
                              coloda_p_k = b[2]
                          else:
                              coloda_p = b[7]
                              coloda_p_k = b[3]


                          for x, y in zip(coloda_p_k, coloda_p):
                              player_get[x] = y
                          player_get.update(dict_pop)
                          print(player_get.values(), "- взял карты из колоды")

          return coloda_p, coloda_p_k, new_player
      answer_g=answer(new_min_dict,a)

      #  сбросить карты, вырезав их из раскладки:yes
       #   у второго игрока проверить по ключам и в диапазоне масти максимальное значение, если его нет, то проверить наличие козырей и бить
       #       карту:  вырезать карты, а если нет, забрать все карты себе

      return print(min_card_in_coloda_player_g,'[ход игрока ',a,' ]-',proverka_min,sbros_kart, )



first=Card()

first.game

