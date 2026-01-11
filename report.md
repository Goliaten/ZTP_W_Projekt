# Wyniki klasyfikacji k-NN

## Parametry klasyfikatora

- Liczba sąsiadów: 5
- Udział zbioru testowego: 0.2
- Liczba foldów CV: 5

## Wyniki walidacji krzyżowej

- Średnia dokładność (CV): 0.6774
- Odchylenie standardowe (CV): 0.0725
- Wyniki dla poszczególnych foldów: 0.5500, 0.7500, 0.6500, 0.7000, 0.7368

## Wyniki na zbiorze testowym

- Dokładność: 0.4800

## Macierz pomyłek

| Klasa | altowka | g_akustyczna | g_elektryczna | kontrabas | skrzypce |
|---|---|---|---|---|---|
| altowka | 2 | 0 | 0 | 1 | 2 |
| g_akustyczna | 2 | 2 | 0 | 1 | 0 |
| g_elektryczna | 1 | 1 | 2 | 0 | 1 |
| kontrabas | 3 | 0 | 0 | 2 | 0 |
| skrzypce | 1 | 0 | 0 | 0 | 4 |

## Raport klasyfikacji (dokładność, precyzja, recall, F1)

### Klasa: altowka

- Precision: 0.2222
- Recall:    0.4000
- F1-score:  0.2857

### Klasa: g_akustyczna

- Precision: 0.6667
- Recall:    0.4000
- F1-score:  0.5000

### Klasa: g_elektryczna

- Precision: 1.0000
- Recall:    0.4000
- F1-score:  0.5714

### Klasa: kontrabas

- Precision: 0.5000
- Recall:    0.4000
- F1-score:  0.4444

### Klasa: skrzypce

- Precision: 0.5714
- Recall:    0.8000
- F1-score:  0.6667


# altowka

| Cecha | Min | Max | Std | Średnia | Mediana |
|---|---:|---:|---:|---:|---:|
| attack_time | 0.00431716 | 0.157689 | 0.0342479 | 0.044238 | 0.0367211 |
| br | 667.222 | 1437.61 | 218.065 | 947.127 | 898.239 |
| even_components | 2.60156 | 7.51463 | 1.29394 | 3.71679 | 3.12005 |
| ir | 4.64213 | 10.1248 | 1.50637 | 6.1271 | 5.69795 |
| odd_components | 2.35225 | 7.50213 | 1.34257 | 3.74243 | 3.32375 |
| release_time | 0.00857633 | 0.926911 | 0.333093 | 0.346767 | 0.253237 |
| zcr | 396.9 | 2337.3 | 495.134 | 984.312 | 749.7 |

# g_akustyczna

| Cecha | Min | Max | Std | Średnia | Mediana |
|---|---:|---:|---:|---:|---:|
| attack_time | 0.00233544 | 0.136275 | 0.0265356 | 0.0210161 | 0.0120902 |
| br | 258.203 | 3450.1 | 894.474 | 1351.62 | 925.306 |
| even_components | 2.13317 | 10.3479 | 2.20118 | 4.48061 | 3.87918 |
| ir | 3.92309 | 19.3497 | 4.22907 | 8.00667 | 7.3971 |
| odd_components | 2.07043 | 10.0498 | 2.16849 | 4.40611 | 4.06132 |
| release_time | 0.000501473 | 0.8867 | 0.254095 | 0.118625 | 0.004352 |
| zcr | 220.5 | 7364.7 | 2540.71 | 2654.82 | 1455.3 |

# g_elektryczna

| Cecha | Min | Max | Std | Średnia | Mediana |
|---|---:|---:|---:|---:|---:|
| attack_time | 0.000824784 | 0.0183634 | 0.00385236 | 0.00465103 | 0.00310894 |
| br | 902.72 | 2325.21 | 395.944 | 1439.5 | 1313 |
| even_components | 2.2191 | 4.52018 | 0.557829 | 2.89541 | 2.74041 |
| ir | 3.9452 | 8.33331 | 1.00177 | 5.22362 | 4.9349 |
| odd_components | 1.97848 | 4.80108 | 0.63578 | 2.91343 | 2.68211 |
| release_time | 0.000574781 | 0.913449 | 0.314316 | 0.599678 | 0.743019 |
| zcr | 176.4 | 2557.8 | 714.701 | 1077.8 | 793.8 |

# kontrabas

| Cecha | Min | Max | Std | Średnia | Mediana |
|---|---:|---:|---:|---:|---:|
| attack_time | 0.00681456 | 0.180458 | 0.0424236 | 0.0431892 | 0.0328388 |
| br | 335.515 | 801.658 | 115.018 | 620.876 | 626.215 |
| even_components | 2.6514 | 6.18143 | 0.878 | 3.97778 | 3.82767 |
| ir | 3.13569 | 10.2482 | 1.85737 | 6.11213 | 6.08833 |
| odd_components | 2.31195 | 5.66607 | 0.85243 | 3.97642 | 3.91239 |
| release_time | 0.00483316 | 0.564488 | 0.162428 | 0.140745 | 0.0652847 |
| zcr | 132.3 | 1146.6 | 261.771 | 413.438 | 418.95 |

# skrzypce

| Cecha | Min | Max | Std | Średnia | Mediana |
|---|---:|---:|---:|---:|---:|
| attack_time | 0.00701179 | 0.257851 | 0.0612869 | 0.0638029 | 0.0375474 |
| br | 703.47 | 1796.6 | 302.954 | 1129.58 | 1037.18 |
| even_components | 2.59293 | 5.87744 | 0.985928 | 3.96884 | 3.80849 |
| ir | 4.68688 | 9.76435 | 1.38434 | 6.81076 | 6.59761 |
| odd_components | 2.4522 | 5.81768 | 1.02169 | 4.03815 | 3.86264 |
| release_time | 0.00429836 | 0.939065 | 0.330127 | 0.340976 | 0.181089 |
| zcr | 661.5 | 2778.3 | 503.127 | 1261.26 | 1102.5 |
