import folium
import json

with open("stations.geojson", "r", encoding="utf-8") as f:
    geojson_data = json.load(f)

m = folium.Map(
    location=[26.8206, 30.8025],
    zoom_start=6,
    tiles="OpenStreetMap",
    control_scale=True
)


#  عنوان الخريطة
title_html = """
<div style="
    position: fixed;
    top: 15px;
    left: 50%;
    transform: translateX(-50%);
    z-index: 9999;
    background-color: white;
    padding: 10px 22px;
    border-radius: 10px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.3);
    font-family: Arial;
    text-align: center;
">
    <div style="
        font-size: 20px;
        font-weight: bold;
        color: #222;
    ">
        تحليل الكثافة السكانية في مصر
    </div>

    <div style="
        font-size: 12px;
        color: #666;
        margin-top: 3px;
    ">
        Python • GeoJSON • GIS • Interactive Web Mapping
    </div>
</div>
"""

m.get_root().html.add_child(folium.Element(title_html))

def get_style(density):

    if density > 2000:
        return {
            "color": "#FF0055",
            "radius": 11,
            "label": "كثافة مرتفعة جدًا"
        }

    elif density > 1000:
        return {
            "color": "#FF9900",
            "radius": 8,
            "label": "كثافة مرتفعة"
        }

    elif density > 200:
        return {
            "color": "#00AA55",
            "radius": 6,
            "label": "كثافة متوسطة"
        }

    else:
        return {
            "color": "#0088CC",
            "radius": 5,
            "label": "كثافة منخفضة"
        }

for feature in geojson_data["features"]:

    coords = feature["geometry"]["coordinates"]

    lon = coords[0]
    lat = coords[1]

    props = feature["properties"]

    name = props["name"]
    pop = props["population"]
    area = props["area_sqkm"]
    density = props["pop_density"]

    style = get_style(density)


    popup_html = f"""
    <div style="
        font-family: Arial;
        direction: rtl;
        text-align: right;
        width: 220px;
        color: #222;
    ">

        <h3 style="
            margin: 0 0 8px 0;
            text-align: center;
            color: #1f4e79;
        ">
            {name}
        </h3>

        <hr>

        <b>👥 عدد السكان:</b>
        {pop:,}

        <br><br>

        <b>📐 المساحة:</b>
        {area:,} كم²

        <br><br>

        <b>📊 الكثافة السكانية:</b>

        <span style="
            color: {style["color"]};
            font-weight: bold;
        ">
            {density:,.2f}
        </span>

        نسمة/كم²

        <br><br>

        <b>التصنيف:</b>
        {style["label"]}

    </div>
    """

    folium.CircleMarker(

        location=[lat, lon],

        radius=style["radius"],

        color=style["color"],

        fill=True,

        fill_color=style["color"],

        fill_opacity=0.85,

        weight=2,

        popup=folium.Popup(
            popup_html,
            max_width=300
        ),

        tooltip=f"{name} | {density:,.2f} نسمة/كم²"

    ).add_to(m)


# الليجيند 
legend_html = """
<div style="
    position: fixed;
    bottom: 30px;
    right: 30px;
    z-index: 9999;

    background-color: white;

    padding: 12px 16px;

    border-radius: 10px;

    box-shadow: 0 2px 8px rgba(0,0,0,0.3);

    font-family: Arial;

    direction: rtl;

    text-align: right;

    font-size: 13px;
">

    <div style="
        font-size: 15px;
        font-weight: bold;
        margin-bottom: 8px;
    ">
        الكثافة السكانية
    </div>


    <div style="margin: 5px;">
        <span style="
            display:inline-block;
            width:12px;
            height:12px;
            background:#FF0055;
            border-radius:50%;
            margin-left:6px;
        "></span>

        أكثر من 2000 نسمة/كم²
    </div>


    <div style="margin: 5px;">
        <span style="
            display:inline-block;
            width:12px;
            height:12px;
            background:#FF9900;
            border-radius:50%;
            margin-left:6px;
        "></span>

        1000 – 2000
    </div>


    <div style="margin: 5px;">
        <span style="
            display:inline-block;
            width:12px;
            height:12px;
            background:#00AA55;
            border-radius:50%;
            margin-left:6px;
        "></span>

        200 – 1000
    </div>


    <div style="margin: 5px;">
        <span style="
            display:inline-block;
            width:12px;
            height:12px;
            background:#0088CC;
            border-radius:50%;
            margin-left:6px;
        "></span>

        أقل من 200
    </div>

</div>
"""

m.get_root().html.add_child(folium.Element(legend_html))


m.save("interactive_egypt_map.html")

print("تم إنشاء الخريطة التفاعلية بنجاح!")