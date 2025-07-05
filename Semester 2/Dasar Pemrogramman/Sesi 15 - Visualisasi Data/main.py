# https://www.kaggle.com/datasets/jayaantanaath/student-habits-vs-academic-performance?resource=download

# import library
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# baca file csv
df = pd.read_csv('student_habits_performance.csv')

# Siapkan variabel x dan y
x = df[['study_hours_per_day']]
y = df['exam_score'] # target / output

# Statistik dasar
mean_x = x['study_hours_per_day'].mean()
median_x = x['study_hours_per_day'].median()
std_x = x['study_hours_per_day'].std()

mean_y = y.mean()
median_y = y.median()
std_y = y.std()

# Buat model regresi
model = LinearRegression()
model.fit(x, y)
y_pred = model.predict(x)

# Intercept dan slope
intercept = model.intercept_
slope = model.coef_[0]

# ==== Dashborad ====
fig, axs = plt.subplots(2, 2, figsize = (12,8))
fig.suptitle('Dashboard Analisis Regresi Linier', fontsize=16)

# Statistik deskriptif (pakai table visual)
axs[0, 0].axis('off')
table_data = [
    ['Variabel', 'Mean', 'Median', 'Std_Dev'],
    ['Jam Belajar', f'{mean_x:.2f}', f'{median_x:.2f}', f'{std_x:.2f}'],
    ['Nilai Ujian', f'{mean_y:.2f}', f'{median_y:.2f}', f'{std_y:.2f}']
 ]
table = axs[0, 0].table(cellText=table_data, loc='center', cellLoc='center')
table.scale(1.2, 2)
table.auto_set_font_size(False)
table.set_fontsize(13)
for key, cell in table.get_celld().items():
    cell.set_linewidth(0.6)
    cell.set_fontsize(12)
    if key[0] == 0:
        cell.set_facecolor('#eeeeee')
        cell.set_text_props(weight='bold')
axs[0, 0].set_title('Statistika Deskriptif', pad=20)


# Visualisasi regresi
axs[0, 1].scatter(x, y, color='#4E89AE', alpha=0.6, edgecolor='white', s=40, label='Data Asli')
axs[0, 1].plot(x, y_pred, color='#ED6663', linewidth=2, label='Regresi')
axs[0, 1].set_xlabel('Jam Belajar per Hari')
axs[0, 1].set_ylabel('Nilai Ujian')
axs[0, 1].set_title('Regresi Linier: Jam Belajar vs Nilai')

# Tambahkan teks persamaan regresi 
regresi_text = f'y = {intercept:.2f} + {slope:.2f}x'
axs[0, 1].text(0.05, 0.95, regresi_text,
               transform=axs[0, 1].transAxes,
               fontsize=11, color='#06923E',
               verticalalignment='top',
               bbox=dict(facecolor='white', alpha=0.6, edgecolor='gray'))
axs[0, 1].legend()

# Histogram y
axs[1, 0].hist(y, bins=10, color='#ED6663', edgecolor='black')
axs[1, 0].set_title('Distribusi Nilai Ujian')
axs[1, 0].set_xlabel('Nilai')
axs[1, 0].set_ylabel('Frekuensi')

# Histogram x
axs[1, 1].hist(x, bins=10, color='#4E89AE', edgecolor='black')
axs[1, 1].set_title('Distribusi Jam Belajar')
axs[1, 1].set_xlabel('Jam Belajar')
axs[1, 1].set_ylabel('Frekuensi')

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # biar gak numpuk ke judul
plt.subplots_adjust(wspace=0.5, hspace=0.4)
plt.show()
