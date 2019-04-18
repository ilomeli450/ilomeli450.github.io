---
layout: project
type: project
image: images/grumpy.jpg
title: Laplacian Pyramids and Image Blending
permalink: projects/laplacian_image_blending
# All dates must be YYYY-MM-DD format!
date: 2019-03-10
labels:
  - Computer Vision
  - Laplacian Pyramids
  - Image Blending
summary: In this project, I explore the concept of laplacian pyramids and how they can be used to do smooth transition image blending.
---

The concepts of laplacian pyramid building and image blending can be used to smoothly blend two images using an alpha mask as well as to build a hybrid image. 

## Methods 

# Obtaining and Preparing Source Images

The images for the image blending task were grabbed from DuckDuckGo's image search engine. We arrived at two self-portrait paintings. The dimensions were matched using $cv2.resize$, according to the smallest image's dimensions. Since one of the pictures was smaller in both dimensions, we encountered no issues with the resizing process. The two input images used in laplacian pyramid blend are shown below. When scouting for images, we attempted to find portraits where the area of one person's face was in the relative vicinity of the other.
