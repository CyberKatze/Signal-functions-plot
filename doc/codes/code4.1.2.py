d = .0001
n = np.arange(-4, 4, d)
x_en = ct_energy(x, n, d)
y1_en = ct_energy(y1, n, d)
y2_en = ct_energy(y2, n, d)
# endsection
print(f'x_en: {x_en}\ny_en: {y1_en}\ny2_en:{y2_en}')
