import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mticker

# تحميل بيانات COVID-19 من Our World in Data
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
df = pd.read_csv(url)

# إدخال اسم الدولة من المستخدم
country = input("Enter country name: ")

# التحقق من توفر البيانات للدولة المطلوبة
available_countries = df["location"].unique()
if country not in available_countries:
    raise ValueError(f"Data for '{country}' is not available!\nAvailable options: {', '.join(available_countries[:10])}...")

# استخراج بيانات الدولة المختارة
df_country = df[df["location"] == country]

# تحويل التاريخ إلى صيغة مناسبة
df_country["date"] = pd.to_datetime(df_country["date"])

# رسم المخطط الزمني لتطور الحالات
plt.figure(figsize=(12, 6))
sns.lineplot(x=df_country["date"], y=df_country["total_cases"], label="Total Cases", color="blue")
sns.lineplot(x=df_country["date"], y=df_country["total_deaths"], label="Total Deaths", color="red")

# تحسينات على الشكل
plt.xlabel("Date")
plt.ylabel("Count")
plt.title(f"COVID-19 Cases & Deaths in {country}")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)

#  تنسيق الأرقام على المحور Y لجعلها واضحة بدلًا من التدوين العلمي
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}'))

# عرض المخطط
plt.show()