# Audio Segmentation Using K-means Clustering

## Table of contents
* [General info](#general-info)
* [Library](#library)
* [Module](#modules-used)

## General Info
My project uses Arduino components from OSOYOO Model 3 V2.0 DIY Robot Car Kit. I made this car as a personal project to learn about Arduino. This obstacle avoiding machine uses an HC-SR04 sensor mounted on top of a servo to locate walls in a maze using echolocation. The Arduino, 2 DC motor, servo, and sensor are powered by a separate 9V battery. The car moves forward until it sees a wall that is less than 12cm away. If this condition is met, the car backs up and the servo rotates 90 degrees to the left for the sensor to scan how far away the left wall is. The servo then rotates 180 degrees to the right to scan the distance of the right wall. If the distance of the left wall is more than the right, the car will turn 90 degrees to the left, and vice versa.

## Library
- NewPing
- Servo

## Modules Used
1. Ren He NEO-6M GPS Module Active Antenna
   https://www.amazon.co.jp/gp/product/B07LDX31FY/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1
2. SunFounder Digital Micro Servo Metal Gear
   https://www.amazon.co.jp/-/en/SunFounder-Digital-Micro-Servo-Weight/dp/B0852Z9ZR4/ref=sr_1_6?keywords=マイクロサーボ&qid=1641460206&sr=8-6
3. OSOYOO Model 3 V2.0 Arduino DIY Robot Car Kit

