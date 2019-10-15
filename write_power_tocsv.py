import pandas as pd

# データフレームを作成
df = pd.DataFrame([freqlist, amp], index=['Hz', 'power'])

#周波数帯域5000Hzまでの範囲に制限してcsvで取得
df_limit = df.iloc[:,1:311]

# CSV ファイルとして出力、名前は任意で変えて
df_limit.to_csv("audio_power.csv", index=True)
