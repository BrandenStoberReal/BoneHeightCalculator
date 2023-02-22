import os
import math

left_humerus = float(input("Left humerus Height (cm): "))
right_humerus = float(input("Right humerus Height (cm): "))
left_ulna = float(input("Left Ulna Height (cm): "))
right_ulna = float(input("Right Ulna Height (cm): "))
left_radius = float(input("Left Radius Height (cm): "))
right_radius = float(input("Right Radius Height (cm): "))
left_femur = float(input("Left Femur Height (cm): "))
right_femur = float(input("Right Femur Height (cm): "))
left_tibia = float(input("Left Tibia Height (cm): "))
right_tibia = float(input("Right Tibia Height (cm): "))
left_fibula = float(input("Left Fibula Height (cm): "))
right_fibula = float(input("Right Fibula Height (cm): "))
ethnicity = input("Skeleton Ethnicity: ")

def africanf_bone_height(bone, size):
    bone = bone.lower()
    if (bone == "humerus"):
        return 3.08 * size + 64.67
    elif (bone == "radius"):
        return 3.67 * size + 71.79
    elif (bone == "ulna"):
        return 3.31 * size + 75.38
    elif (bone == "femur"):
        return 2.28 * size + 59.76
    elif (bone == "tibia"):
        return 2.45 * size + 72.65
    elif (bone == "fibula"):
        return 2.49 * size + 70.90
    else:
        return 0

if (ethnicity.lower() == "african female"):
    final_height = (africanf_bone_height("humerus", left_humerus) + africanf_bone_height("humerus", right_humerus) + africanf_bone_height("ulna", left_ulna) + africanf_bone_height("ulna", right_ulna) + africanf_bone_height("radius", left_radius) + africanf_bone_height("radius", right_radius) + africanf_bone_height("femur", left_femur) + africanf_bone_height("femur", right_femur) + africanf_bone_height("tibia", left_tibia) + africanf_bone_height("tibia", right_tibia) + africanf_bone_height("fibula", left_fibula) + africanf_bone_height("fibula", right_fibula)) / 12
    print(f"Your skeleton's final height is {final_height}cm")


