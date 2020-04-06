import math
import random

# TODO: Ubah jumlah koromosom sama jumlah generasi
kromosom_count = 100
gen_count = 1000
populasi = 1
g1 = random.uniform(-3,3)
g2 = random.uniform(-2,2)
pc = 0,25
pmut = 0,5
# rb_x1 = -3
# ra_x1 = 3
# rb_x2 = -2
# ra_x2 = 2

#Definisi fungsi
def soal(x1, x2):
    return (4-2.1*math.pow(x1, 2) + (math.pow(x1, 4)))*math.pow(x1, 2) + (x1 * x2) + (-4 + 4 * x2 * x2)*x2*x2

#Penjabaran Populasi, dengan pendekodean gen terlebih dahulu
def Populasi(count):
  Populations = []
  for i in range(count):
    kromosom = {
        "x1": -3 + ((6) * g1),
        "x2": -2 + ((4) * g2)
    }
    Populations.append(kromosom)
  return Populations

#Rumus mencari nilai fitness, dengan nilai a =0.005
def nilaiFitness(Populations):
  result = []
  for i in range(kromosom_count):
    a = Populations[i]
    h = soal(a['x1'], a['x2'])
    fit = 1 / (h + 0.005)
    result.append({
        'index': i,
        'h': h,
        'fit': fit
    })
  return result

#Mendapatkan Parent, dengan membandingkan nilai fitness terbesar
def getParent(populations, fit_res):
  sorted_fit = sorted(fit_res, key=lambda x: x['fit'], reverse=True) 
  p1 = populations[sorted_fit[0]['index']]
  p2 = populations[sorted_fit[1]['index']]
  return p1, p2

##Proses crossover, dengan menghasilkan 1 child, dan lebih dari nilai pc=0,25
def pindahSilang(parent):
  p1, p2 = parent
  i = random.uniform(0, 1)
  if i > 0.25:
    return {
        'x1': p1['x1'],
        'x2': p2['x2']
    }
  else:
    return {
        'x1': p2['x1'],
        'x2': p1['x2']
    }

#proses mutasi, dengan pmut = 0.5
def mutation(child):
  i = random.randint(0, 1)
  if i > 0.5:
    return {
        'x1': random.uniform(-3, 3),
        'x2': child['x2']
    }
  else:
    return {
        'x1': child['x1'],
        'x2': random.uniform(-2, 2)
    }

def generasiBaru(Populasi, fit_res, child):
  """
  Akan menghasilkan populasi baru dari parameter populasi, berdasarkan fit_res
  """
  sorted_fit = sorted(fit_res, key=lambda x: x['fit'], reverse=True)
  delete = sorted_fit[len(sorted_fit)-1]['index']
  Populasi[delete] = child
  return populasi

# GENETIC ALGORITHM
Populations = Populasi(kromosom_count)
for i in range(gen_count):
  fit_res = nilaiFitness(Populations)
  parent = getParent(Populations, fit_res)
  child = pindahSilang(parent)
  child = mutation(child)
  populations = generasiBaru(Populations, fit_res, child)

print(Populations)
print(nilaiFitness(Populations))
print("Nilai x1:"+str(Populations[0]['x1'] ))
print("Nilai x2:"+str(Populations[0]['x2'] ))
