# %%
import numpy as np
import matplotlib.pyplot as plt

from question1 import x, y1, y2

# d is the distance between samples


def ct_energy(x, n, d): return sum([np.abs(x(i))**2 for i in n])*d


d = .0001
n = np.arange(-4, 4, d)
x_en = ct_energy(x, n, d)
y1_en = ct_energy(y1, n, d)
y2_en = ct_energy(y2, n, d)
# endsection
print(f'x_en: {x_en}\ny_en: {y1_en}\ny2_en:{y2_en}')
x_en: 2.6666166750070275
y_en: 1.3332833500056211
y2_en:2.6667166749880353
