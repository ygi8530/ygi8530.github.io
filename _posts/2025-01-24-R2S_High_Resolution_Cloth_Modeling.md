---
title: 'Real-to-Sim High-Resolution Cloth Modeling: Physical Parameter Optimization Using Particle-Based Simulation with Robot Manipulation Data'
date: 2025-01-24 12:00:00 +0900
categories: [paper]
tags: [Cloth Simulation, Robotic Manipulation, Physical Parameter Estimation, Sim-to-Real Transfer, Deformable Object Handling, Realistic Cloth Modeling]     # TAG names should always be lowercase
author: [Kang-il_Yoon, Soo-Chul_Lim]
description: 'Submitted'
toc: true  # 목차 표시 여부 (기본값: true)
comments: true  # 댓글 허용 여부 (기본값: _config.yml 설정 따라감)
pin: true  # 홈 화면에서 상단 고정 (선택 사항)
math: true  # 수학 수식 활성화 (선택 사항)
mermaid: true  # Mermaid 다이어그램 활성화 (선택 사항)
---
DOI: <a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5109969" target="_blank">10.XXXX</a><br>
<a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5109969" target="_blank">[Paper]</a> &nbsp;&nbsp;
<a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5109969" target="_blank">[Project page]</a> &nbsp;&nbsp;
<a href="https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5109969" target="_blank">[Video]</a><br>

This study proposes an optimized real-to-sim model that reflects the physical properties of real cloth to replicate realistic cloth behavior in simulation environments. While previous research has used data-driven or physics-guided methods to build simulation environments, those approaches are significantly limited due to reliance on data and restricted accuracy. In this study, we collect data from real robots manipulating cloth samples of various size and material, and develop a particle system-based cloth simulation model. By optimizing parameters based on real-world data, such as stretching, bending, friction, and damping, the simulation model reproduces the shapes of real cloth. In consequence, in comparison to previous studies that used physical parameter estimation, the proposed methodology demonstrates accuracy and generalization performance. Notably, the model maintains consistent similarity in unseen tasks, proving its adaptability across diverse tasks. This study presents a crucial step toward enhancing the practical applicability of simulation-based robotic learning and improving robot abilities to manipulate deformable objects.