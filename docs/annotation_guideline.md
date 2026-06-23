## 1. Purpose

## 2. Layer Annotation

- **Definition**

A:コミュニケーション上の認識ズレや参照ズレを扱う発話

B:対象に対する評価、感情、解釈を含む発話

C:判断、要求、提案、責任帰属を含む発話

- **Layer Selection Rule**

最も支配的なLayerを選択する。

A/B/Cの複数付与は行わない。

曖昧な場合は以下を優先する。

C > B > A

アノテーションでは単一Layerを付与する。
解析システムでは各Layerの割合を別途算出する。

## 3. Subject Annotation

   **3.1 基本原則**
   
   subjectは登場する名詞ではなく、態度の向き先を選ぶ。

   **3.2 Subject Boundary Cases**

   - 国 vs 政府 vs 自治体
   
   例：「東京に出ないと国は動かない」
   
   → 国
   
   ⸻
   
   - 熊 vs 自治体
   
   例：「熊を駆除してほしい」
   
   → 自治体
   
   理由：要求の向き先が自治体だから
   
   ⸻
   
   - 熊 vs 被害者
   
   例：「亡くなられた方が気の毒」
   
   → 被害者

## 4. Stance Annotation

   **4.1 基本原則**

   **4.2 Stance Boundary Cases**

   

## 5. Multi-label Policy
- **Layer**

Layerは原則単一ラベル。

最も支配的な層を選択する。

- **Subject**

Subjectは原則単一ラベル。

発話の態度が最も向いている対象を選択する。

- **Stance**

Stanceのみ複数ラベルを許可する。

- **許可例**
```stance
批判/要求
共感/賞賛
不安/要求
皮肉/批判
```
- **非推奨**
```stance
賞賛/批判
共感/皮肉
```
