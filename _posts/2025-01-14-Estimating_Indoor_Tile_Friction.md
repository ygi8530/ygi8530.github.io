---
title: 'Estimating Indoor Tile Friction Coefficient Using Visual Information'
date: 2025-01-14 12:00:00 +0900
categories: [paper]
tags: [Computer Vision, Coefficient of Friction Estimation, Deep Learning]     # TAG names should always be lowercase
author: [Jung‐Hwan_Yang, Kang-il_Yoon, Seunghyeon_Ha, Andy_Hong, Soo-Chul_Lim]
description: 'Journal of Computational Design and Engineering, vol.12, Issue 1, January 2025, Pages 331–341'
toc: true  # 목차 표시 여부 (기본값: true)
comments: true  # 댓글 허용 여부 (기본값: _config.yml 설정 따라감)
pin: true  # 홈 화면에서 상단 고정 (선택 사항)
math: true  # 수학 수식 활성화 (선택 사항)
mermaid: true  # Mermaid 다이어그램 활성화 (선택 사항)
---
![이미지](/assets/image/estimating_indoor_tile_friction.png)
DOI: <a href="https://academic.oup.com/jcde/advance-article/doi/10.1093/jcde/qwaf003/7954144" target="_blank">/10.1093/jcde/qwaf003</a><br>
<a href="https://academic.oup.com/jcde/advance-article/doi/10.1093/jcde/qwaf003/7954144" target="_blank">[Paper]</a> &nbsp;&nbsp;

Slip and fall accidents are common both indoors and outdoors, posing and risks from minor to serious injuries. An effective way to prevent these accidents is for pedestrians to know the friction properties of their path beforehand. Developing a network that can discern the frictional properties of surfaces from camera-captured images and convey this information to pedestrians could significantly reduce the incidence of slips. However, predicting the indoor friction coefficient of tiles accurately is challenging due to reflections from multiple fluorescent lights and the tiles themselves. Additionally, water accumulation on tiles due to cleaning or leakage greatly contributes to slip accidents. This paper presents an algorithm that accurately predicts floor friction coefficients in real indoor environments, accounting for image distortions caused by light reflections and water on the floor. Experimental results validate that the proposed system reliably predicts indoor floor friction coefficients despite factors such as lighting angles and water presence. Moreover, to demonstrate its practical applicability, a user-application has been developed to predict the friction coefficient for specific areas as required. This system can be integrated into various devices, including walkers, canes, and smartphones, to assist pedestrians in navigating safely.