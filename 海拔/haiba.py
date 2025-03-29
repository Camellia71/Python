import numpy as np
import geopandas as gpd
import rasterio
from rasterstats import zonal_stats
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------
# 输入文件路径
# ----------------------------
dem_path = "E:\张岐奕1\EPI\github\Python\海拔\dem-china1.jpg"          # 30米分辨率DEM数据（需提前拼接裁剪）
province_path = "E:\张岐奕1\EPI\github\Python\海拔\省级行政区.shp"  # 省级行政区划矢量文件（需包含NAME字段）

# ----------------------------
# 参数设置
# ----------------------------
# 定义海拔区间（单位：米）
elevation_bins = [0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, np.inf]
bin_labels = [
    "0-500m", "500-1000m", "1000-1500m", "1500-2000m", 
    "2000-2500m", "2500-3000m", "3000-3500m", 
    "3500-4000m", "4000-4500m", ">4500m"
]

# ----------------------------
# 数据处理
# ----------------------------
def calculate_elevation_percentage():
    # 1. 重分类DEM
    with rasterio.open(dem_path) as src:
        dem = src.read(1)
        # 将DEM像元值分配到对应的海拔区间（1-10）
        reclassified = np.digitize(dem, elevation_bins)
        affine = src.transform

    # 2. 加载省级行政区划
    provinces = gpd.read_file(province_path)
    
    # 3. 分区统计每个海拔区间的像元数量
    stats = zonal_stats(
        provinces, 
        reclassified, 
        affine=affine, 
        categorical=True, 
        category_map={i: bin_labels[i-1] for i in range(1, 11)},
        nodata=0
    )

    # 4. 计算各省份海拔区间占比
    results = []
    for idx, row in provinces.iterrows():
        province_name = row['NAME']
        total_pixels = sum(stats[idx].values())
        
        # 初始化当前省份的占比字典
        province_data = {"Province": province_name}
        
        # 计算每个区间的占比
        for bin_id, label in enumerate(bin_labels, start=1):
            pixel_count = stats[idx].get(label, 0)
            percentage = (pixel_count / total_pixels) * 100 if total_pixels > 0 else 0
            province_data[label] = round(percentage, 2)
        
        results.append(province_data)
    
    # 转换为DataFrame
    df = pd.DataFrame(results)
    return df

# ----------------------------
# 执行分析并保存结果
# ----------------------------
if __name__ == "__main__":
    # 计算海拔占比
    elevation_df = calculate_elevation_percentage()
    
    # 保存为CSV
    elevation_df.to_csv("province_elevation_percentage.csv", index=False)
    print("结果已保存至 province_elevation_percentage.csv")

    # ----------------------------
    # 可视化（堆叠柱状图）
    # ----------------------------
    plt.figure(figsize=(15, 8))
    elevation_df.set_index("Province").plot(kind='bar', stacked=True, colormap='viridis')
    plt.title("各省份海拔区间占比")
    plt.ylabel("占比 (%)")
    plt.xticks(rotation=45, ha='right')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig("province_elevation_distribution.png", dpi=300)
    plt.show()