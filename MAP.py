import folium
import geopandas as gpd
import pandas as pd

# 1. قراءة بيانات المحافظات
df = pd.read_csv(
    "points.txt",
    header=None,
    names=["lat", "lon", "name", "population", "area_sqkm"],
)
df["pop_density"] = (df["population"] / df["area_sqkm"]).round(2)

gdf = gpd.GeoDataFrame(
    df, geometry=gpd.points_from_xy(df["lon"], df["lat"]), crs="EPSG:4326"
)

# 2. إنشاء الخريطة
m = folium.Map(
    location=[gdf.geometry.y.mean(), gdf.geometry.x.mean()], zoom_start=6
)

# طبقة الأقمار الصناعية
folium.TileLayer(
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    attr="Esri Satellite",
    name="أقمار صناعية",
).add_to(m)

# طبقة الشوارع
folium.TileLayer(
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}",
    attr="Esri Streets",
    name="خريطة الشوارع",
).add_to(m)

# 3. إضافة النقاط والبيانات التفاعلية
folium.GeoJson(
    gdf,
    name="المحافظات",
    tooltip=folium.GeoJsonTooltip(fields=["name"], aliases=["المحافظة:"]),
    popup=folium.GeoJsonPopup(
        fields=["name", "population", "pop_density"],
        aliases=["الاسم:", "السكان:", "الكثافة (نسمة/كم²):"],
    ),
).add_to(m)

# 4. إضافة أداة التحكم في الطبقات
folium.LayerControl().add_to(m)

# مربع العنوان متسنتر في المنتصف
title_html = """
    <div style="position: fixed; 
                top: 15px; left: 50%; transform: translateX(-50%); 
                z-index: 9999; background-color: rgba(255, 255, 255, 0.95); 
                border: 2px solid #2b5c8f; border-radius: 8px; 
                padding: 10px 20px; font-family: 'Segoe UI', Tahoma, Geneva, sans-serif;
                box-shadow: 0px 4px 10px rgba(0,0,0,0.2); direction: rtl; text-align: center;">
        <h4 style="margin: 0; color: #1a365d; font-size: 16px;">🗺️ خريطة الكثافة السكانية</h4>
        <p style="margin: 4px 0 0 0; font-size: 12px; color: #4a5568;">
            عرض توزيع المحافظات وحساب الكثافة (نسمة/كم²)
        </p>
    </div>
"""

m.get_root().html.add_child(folium.Element(title_html))

# 5. حفظ 
m.save("index.html")
print("تم")
