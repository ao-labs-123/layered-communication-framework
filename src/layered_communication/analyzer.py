from detect_subject import detect_subject
from detect_stance import detect_stance
from detect_layer import detect_layer

text = "ここまで同じタイミングで一斉に街に流れ出てるの凄いな。ただ熊被害で亡くなる人が増える前に対策してほしい"

print(detect_subject(text))
print(detect_stance(text))
print(detect_layer(text))
