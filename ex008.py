medida = float(input('distância em metros:'))
cm = medida * 100
mm = medida * 1000
km = medida / 1000
hm = medida / 100
dm = medida / 10
dcm = medida * 10
mm = medida * 1000
print('a medida de {}m é de {}cm, {}mm, {}km, {}hm, {}dm, {}dcm, {}mm '.format(medida, cm, mm, km, hm, dm, dcm,mm))
