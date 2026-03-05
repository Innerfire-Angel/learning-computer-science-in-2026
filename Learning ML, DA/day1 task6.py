import math
EPS = 1e-5  # для проверки дот продукта приближенного к 0

#даны 3 вектора

v1 = (3,4)
v2 = (4,-3)
v3 = (-1,2)


#dot product по координатам
# v1, v2
dot_v1_v2 = v1[0] * v2[0] + v1[1] * v2[1]
# v1, v3
dot_v1_v3 = v1[0] * v3[0] + v1[1] * v3[1]
# v2, v3
dot_v2_v3 = v2[0] * v3[0] + v2[1] * v3[1]


#считаем косинус угла между этими векторами потому что по дот нельзя точно определить сонаправленность

r_v1 = math.hypot(*v1)
r_v2 = math.hypot(*v2)
r_v3 = math.hypot(*v3)

cos_a_v1_v2 = dot_v1_v2 / (r_v1 * r_v2)
cos_a_v1_v3 = dot_v1_v3 / (r_v1 * r_v3)
cos_a_v2_v3 = dot_v2_v3 / (r_v2 * r_v3)

my_dict = {}
my_dict["v1, v2"] = cos_a_v1_v2
my_dict["v1, v3"] = cos_a_v1_v3
my_dict["v2, v3"] = cos_a_v2_v3

for key, value in my_dict.items():
    # 1. Сначала проверяем на перпендикулярность (близость к 0)
    if abs(value) < EPS:
        print(f"{key}: строго перпендикулярны (cos ≈ 0)")
    
    # 2. Проверяем на идеальную сонаправленность (близость к 1)
    elif math.isclose(value, 1, abs_tol=EPS):
        print(f"{key}: идеально сонаправлены (cos ≈ 1)")
        
    # 3. Проверяем на "почти параллельны" (очень острый угол)
    elif value > 0.9:
        print(f"{key}: почти параллельны (cos: {value:.2f})")
        
    # 4. Проверяем на просто острый угол
    elif 0 < value <= 0.9:
        print(f"{key}: острый угол, разные направления (cos: {value:.2f})")
        
    # 5. Проверяем на тупой угол
    elif value < 0:
        print(f"{key}: тупой угол (cos: {value:.2f})")
    

