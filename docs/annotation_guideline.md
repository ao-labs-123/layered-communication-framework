## 1. Purpose
このデータセットはSNSコメントにおける「態度の向き先(subject)」と「態度の種類(stance)」を分析するために作成された。

## 2. Layer Annotation

## 3. Subject Annotation
   3.1 基本原則
   subjectは登場する名詞ではなく、態度の向き先を選ぶ。
   
   3.2 Subject Boundary Cases
   国 vs 政府 vs 自治体
   
例：
「東京に出ないと国は動かない」

→ 国

⸻

熊 vs 自治体

例：
「熊を駆除してほしい」

→ 自治体

理由：
要求の向き先が自治体だから

⸻

熊 vs 被害者

例：
「亡くなられた方が気の毒」

→ 被害者

## 4. Stance Annotation
   4.1 基本原則
   stanceは発話の中心的態度を選ぶ。
   
   4.2 Stance Boundary Cases
   批判 vs 皮肉

例：
「熊かわいそうと言ってた人はどう思うんだろう」

→ 皮肉

⸻

批判 vs 分析

例：
「暖冬で冬眠できなかったから増えた」

→ 分析

⸻

不安 vs 共感

例：
「本当に怖い」

→ 不安

例：
「気の毒でならない」

→ 共感
   
## 5. Multi-label Policy

## 6. Difficult Examples
