# def teskari_tartib(listt):
#     teskari_juft = []
#     teskari_toq = []
#     for i in listt:
#         if i > 9 and i%2==0:
#             teskari_juft.append(int(str(i)[::-1]))
#         else:
#             teskari_toq.append(int(str(i)))

#     n = teskari_juft+teskari_toq
#     m = len(teskari_juft+teskari_toq)    

#     for el in range(m):
#         for j in range(0, m-1):
#             if n[j] > n[j+1]:
#                 n[j], n[j+1] = n[j+1], n[j]
#     return n


# print(teskari_tartib([1,21,48,21,48,56,764]))




# def kamayish_tartibi(num):
#     m = len(num)
#     for i in range(m):
#         for j in range(0, m-1):
#             if num[j] < num[j+1]:
#                num[j+1], num[j] = num[j], num[j+1]
#     return num
# print(kamayish_tartibi([1,64,91,24,31]))




# def fayldagi_sozlar_soni(fayl_nomi):
#     num=0
#     with open(fayl_nomi, 'r') as fayl:
#         malumot = fayl.read()
#         for i in  malumot.split():
#             num += 1
#         return num


# fayldagi_sozlar_soni('text.txt')




# def text(matn):
#     textt = matn.title().replace(" ","")
#     javob = '#'+textt
#     if len(javob) > 140 and len(javob) == 0:
#         return False
#     return javob

# print(text('Hello world thanks for you'))


