# Layered Communication Framework

## Overview

Layered Communication Framework is a lightweight rule-based model for representing human utterances as a set of overlapping structural layers.

Rather than treating communication as a single intention, emotion, or speech act, the framework models discourse as the coexistence of multiple structural dimensions.

Without relying on deep learning or large-scale corpora, the framework aims to capture the structural complexity of human communication through a minimal ontology and transparent rules.

⸻

## Theoretical Background

Many language analysis approaches tend to assign each utterance to a single category.

In reality, however, human communication often contains multiple simultaneous structures, such as:

* Misalignment
* Evaluation
* Delegation of judgment

These structures frequently coexist within the same utterance.

The framework decomposes discourse into three structural axes and assigns a score to each axis, allowing the coexistence of multiple communicative layers to be visualized.

The goal is not classification accuracy, but structural interpretability.

⸻

## Structural Axes

**A: Misalignment Structure**

Examples include:

* Request–action mismatch
* Reference mismatch
* Expectation–interpretation mismatch

This axis captures structural friction in communication.

⸻

**B: Evaluation Structure**

Examples include:

* Situation evaluation
* Person evaluation
* Strong evaluative expressions that trigger stance formation

This axis extracts evaluative layers based on linguistic and attitudinal indicators.

⸻

**C: Delegated Judgment Structure**

Examples include:

* Responsibility delegation (“it’s up to you”)
* Implicit norm reliance (“that’s just how things are”)
* Conditional responsibility (“if X, then Y”)
* Consideration-based delegation (“if possible”, “if you don’t mind”)

This axis identifies where judgment, responsibility, or decision-making authority is placed.

⸻

## Multi-Layer Scoring

Each utterance receives three normalized scores:

* A_score
* B_score
* C_score

All scores are normalized to the range [0,1].

## Multi-Layer Classification

The highest score is used as the reference axis.

An axis is considered active when:An axis is considered active when:

score >= max_score * 0.6score >= max_score * 0.6

This produces:

* Single-layer utterances
* Dual-layer utterances
* Triple-layer utterances

## Balance Index

The standard deviation of the three axis scores is calculated as:

balance_index

Interpretation:

* Low value → structurally balanced utterance
* High value → structurally concentrated utterance

This provides a simple quantitative measure of structural bias.

## Example

**Input**

If possible, could you check this?

**Output**

A_score: 0.2
B_score: 0.3
C_score: 0.7

active_axes: ['B', 'C']
structure_type: dual

balance_index: 0.21

## Repository Structure

```repository

├── data
│   ├── analysis_output.csv
│   ├── comments_raw.csv
│   ├── gold_sample.csv
│   └── videos.csv
│
├── docs
│   ├── examples.md
│   ├── annotation_guideline.md
│   └── ontology.md
│
├── src
│   ├── layered_communication
│   │    ├── analyzer.py
│   │    └── detectors
│   │
│   ├── project
│   │    ├── lexicon
│   │    ├── ontology
│   │    ├── patterns
│   │    └── rules
│   │
│   └── scoring
│        ├── layer_score.py
│        ├── score_config.py
│        └── stance_score.py
│
├── README.md
├── notebooks
└── scripts

```

## Positioning

This project is not intended to be a high-accuracy classifier.

Its purpose is to balance:

* Lightweight design
* Transparent rules
* High structural interpretability

The framework attempts to represent human communication not through semantic meaning alone, but through the overlap of communicative structures.

⸻

## Future Directions

* Multi-layer frequency analysis on large corpora
* Structural clustering of discourse
* Cross-linguistic adaptation
* Comparison between human and AI-generated communication
