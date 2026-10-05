# 🗺️ Egypt Population Density - Interactive Web GIS

خريطة تفاعلية لعرض الكثافة السكانية للمحافظات المصرية، تم بناؤها بتحويل بيانات نصية خام إلى طبقات جغرافية تفاعلية منشورة على الويب.

---

### 🛠️ التقنيات والمكتبات المستخدمة
* **Python**: `Pandas` (تنظيف البيانات وحساب الكثافة) | `GeoPandas` (التحويل المكاني ونظام `EPSG:4326`) | `Folium` (إنشاء الخريطة التفاعلية).
* **Basemaps**: خلفيات `Esri Satellite` و `Esri Streets`.
* **UI/UX**: `HTML/CSS` (تصميم مربع عنوان هائم ومتسنتر أعلى الخريطة).
* **Desktop GIS**: `ArcGIS Pro` (تصنيف البيانات وتحليل الكثافة).
* **Deployment**: `GitHub Pages` (استضافة الخريطة التفاعلية عبر `index.html`).

---

### ⚙️ مسار العمل (Workflow)
1. **معالجة البيانات:** قراءة ملف نصي خام (`points.txt`) وحساب الكثافة السكانية:
   $$\text{الكثافة السكانية} = \frac{\text{عدد السكان}}{\text{المساحة (كم²)}}$$
2. **التحويل المكاني:** تحويل الإحداثيات إلى نقاط جغرافية (`GeoDataFrame`) بنظام WGS84 مع استبعاد الأعمدة غير الضرورية.
3. **بناء الخريطة:** 
   * إضافة خلفيات Esri وتفعيل أداة التبديل بين الطبقات (`LayerControl`).
   * ضبط نافذة العرض التفاعلية (`Popups` و `Tooltips`).
   * إضافة مربع عنوان ثابت ومتسنتر في أعلى الشاشة باستخدام كود HTML/CSS مخصص.
4. **النشر:** تصدير الخريطة كملف `index.html` ورفعه إلى GitHub Pages.

---

### 🖼️ معاينة المشروع

#### 1️⃣ الخريطة التفاعلية (Web GIS)
<img width="1917" height="862" alt="Screenshot 2026-10-06 003333" src="https://github.com/user-attachments/assets/7f5bfcce-4411-478e-b45b-6fab62e04b6e" />

#### 2️⃣ التحليل والتصنيف في ArcGIS Pro
![ArcGIS Pro Classification](https://github.com/user-attachments/assets/7a3c71b6-fce7-4388-8d79-2beeb2c009ae)

---

### 🚀 التشغيل المحلي

```bash
# تثبيت المكتبات المطلوبة
conda install -c conda-forge geopandas folium pandas

# تشغيل السكريبت لبناء الخريطة
python MAPs.py
