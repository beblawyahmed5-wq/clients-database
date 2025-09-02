import pandas as pd
from datetime import datetime

# قراءة الملف القديم
file_name = "Clients_Updated.xlsx"

try:
    df = pd.read_excel(file_name)
except FileNotFoundError:
    df = pd.DataFrame(columns=["المحافظة", "اسم العميل", "رقم التليفون", "تاريخ الإضافة"])

# المحافظات
governorates = ["القاهرة", "الجيزة", "الإسكندرية", "السويس", "الإسماعيلية", "بور سعيد", "دمياط", "القليوبية"]

# إضافة 30 عميل جديد لكل محافظة
new_rows = []
for gov in governorates:
    for i in range(30):
        new_rows.append({
            "المحافظة": gov,
            "اسم العميل": f"عميل جديد {gov} {i+1}",
            "رقم التليفون": f"010{i:03d}{len(df)}",
            "تاريخ الإضافة": datetime.now().strftime("%Y-%m-%d %H:%M")
        })

df_new = pd.DataFrame(new_rows)

# دمج القديم + الجديد
df = pd.concat([df, df_new], ignore_index=True)

# حفظ الملف
df.to_excel(file_name, index=False)

print("✅ تم تحديث الملف Clients_Updated.xlsx")
