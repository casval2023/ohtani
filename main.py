import streamlit as st
import math

def get_values_for_strike(strike_val):
    # データを辞書に格納
    data = {
        0: {
            "release_speed": -0.017419404,
            "plate_x": 0.021309378,
            "plate_z": 0.013781465,
            "pfx_x": -0.006296974,
            "pfx_z": -0.006914947,
            "constant": -1.370638217,
        },
        1: {
            "release_speed": 0.067209915,
            "plate_x": 0.007987288,
            "plate_z": -0.001185316,
            "pfx_x": -0.02173839,
            "pfx_z": -0.012146986,
            "constant": -8.1197733,
        },
        2: {
            "release_speed": -0.041298348,
            "plate_x": -0.011432993,
            "plate_z": 0.004616806,
            "pfx_x": 0.000293761,
            "pfx_z": -0.00331083,
            "constant": 1.548106875,
        },
    }
    
    # 指定されたstrikeの値に対応するデータを返す
    return data.get(strike_val, "Invalid strike value")

def get_movement_for_pitch(pitch_type):
    # データを辞書に格納
    data = {
        "4シーム": {"縦変化": 43, "横変化": 22},
        "2シーム": {"縦変化": 28, "横変化": 37},
        "スライダー": {"縦変化": 9, "横変化": -12},
        "カーブ": {"縦変化": -19, "横変化": -22},
        "チェンジアップ": {"縦変化": 23, "横変化": 33},
        "カットボール": {"縦変化": 24, "横変化": -4},
        "スプリット": {"縦変化": 17, "横変化": 30},
    }

    # 指定された球種に対応するデータを返す
    return data.get(pitch_type, "Invalid pitch type")

def get_coordinates_for_course(course):
    # データを辞書に格納
    data = {
        "内角高め": {"x": -16.75, "z": 102.5},
        "真ん中高め": {"x": 0, "z": 102.5},
        "外角高め": {"x": 16.75, "z": 102.5},
        "内角真ん中": {"x": -16.75, "z": 77.5},
        "ど真ん中": {"x": 0, "z": 77.5},
        "外角真ん中": {"x": 16.75, "z": 77.5},
        "内角低め": {"x": -16.75, "z": 57.5},
        "真ん中低め": {"x": 0, "z": 57.5},
        "外角低め": {"x": 16.75, "z": 57.5},
    }

    # 指定されたコースに対応するデータを返す
    return data.get(course, "Invalid course")

defcalculate_discriminant_score(coefficients, release_speeed,plate_x,plate_z,pfx_x,pfx_z)
    score = (coefficients ["release_speed"] * release_speed + coefficients ["plate_×"] * plate_x + coefficients ["plate_z"] * plate_z + coefficients ["pfx_×"] * pfx_x + coefficients ["pfx_z"] * pfx_z + coefficients ["constant"])
    score=1/(1+math.exp(-score))*100
    score = 100-score
    return round (score, 1)

image_path = "my_image.jpg"
st.image(image_path, use_column_width=True)

# タイトルと説明
st.title("大谷翔平を打ち取れ!")
st.write("以下の情報を入力して大谷翔平に打たれない確率を最大にした人が優勝です:")

# 入力部分
strike = st.number_input("ストライクカウント", 0, 2, 1)
speed = st.number_input("ボールの速度 (km/h)", 100.0, 180.0, 145.0)
zone = st.selectbox("コース", ["ど真ん中", "真ん中高め", "外角高め", "内角真ん中", "ど真ん中", "外角真ん中", "内角低め", "真ん中低め", "外角低め"])
balltype = st.selectbox("ボールの種類", ["4シーム", "2シーム", "スライダー", "カーブ", "チェンジアップ", "カットボール", "スプリット"])

balltypes = get_movement_for_pitch(balltype)
zones = get_coordinates_for_course(zone)

release_speed = speed / 1.609343
plate_x = balltypes["横変化"]
plate_z = balltypes["縦変化"]
pfx_x = zones["x"]
pfx_z = zones["z"]

# 係数
coefficients = get_values_for_strike(strike)

# 計算結果を取得
score = calculate_discriminant_score(coefficients, release_speed, plate_x, plate_z, pfx_x, pfx_z)

# 結果を表示
st.header(f"2023年の大谷翔平に打たれない確率は{score}%です")
