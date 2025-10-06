foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform",
           "intermediate cuneiform", "medical cuneiform"]
longer_names = ""
shorter_names = ""

for bone_name in foot_bones:
    if len(bone_name) < 10:
        shorter_names += bone_name + "\n"
    else:
        longer_names += bone_name + "\n"
print("Short names:\n" + shorter_names)
print("Long names:\n" + longer_names)





foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform",
           "intermediate cuneiform", "medical cuneiform"]
longer_names = []
shorter_names = []

for bone_name in foot_bones:
    if len(bone_name) < 10:
        shorter_names.append(bone_name)
    else:
        longer_names.append(bone_name)
print(shorter_names)
print(longer_names)