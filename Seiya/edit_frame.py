import json

f0 = open('Spt.json')
spt_data = json.load(f0)
f0.close()

frame_data = spt_data["Data.Spt"]["frame"]
action_data = spt_data["Data.Spt"]["action"]
num_of_action = len(action_data) - 1

action_group = []

for i in range (0, num_of_action):
    end_frame = -1
    start_frame = int(action_data[str(i)]["frameIndex"])
    j = start_frame
    temp = [action_data[str(i)]["name"], j]
    while (end_frame == -1):
        if (frame_data[str(j)]["last"]):
            temp.append(j)
            temp.append(j - start_frame + 1)
            end_frame = j
        else:
            j += 1
    #print(f"{i}: {temp}")
    #print(f"{i}: {duration}")
    action_group.append(temp)

f1 = open('Spt_old.json')
spt_data_old = json.load(f1)
f1.close()

frame_data_old = spt_data_old["Data.Spt"]["frame"]
action_data_old = spt_data_old["Data.Spt"]["action"]
num_of_action_old = len(action_data_old) - 1

action_group_old = []

for i in range (0, num_of_action_old):
    end_frame = -1
    start_frame = int(action_data_old[str(i)]["frameIndex"])
    j = start_frame
    temp = [action_data_old[str(i)]["name"], j]
    while (end_frame == -1):
        if (frame_data_old[str(j)]["last"]):
            temp.append(j)
            temp.append(j - start_frame + 1)
            end_frame = j
        else:
            j += 1
    #print(f"{i}: {temp}")
    action_group_old.append(temp)

#print(len(action_group))
#print(len(action_group_old))

'''
for i in range(0, len(action_group)):
    if (action_group[3] != action_group_old[3]):
        print(action_group, action_group_old)
'''
'''
key_table1 = []
for key in frame_data["0"].keys():
    key_table1.append(key)
key_table1 = sorted(key_table1)
#print(key_table1)

key_table2 = []
for key in frame_data_old["0"].keys():
    key_table2.append(key)
key_table2 = sorted(key_table2)
#print(key_table2)

for i in range(0, len(key_table1)):
    if key_table1[i] != key_table2[i]:
        print(key_table1[i], key_table2[i])
'''

key_table = []
for key in frame_data["0"].keys():
    key_table.append(key)
key_table = sorted(key_table)
#print(key_table1)

#checklist = ["duration", ]

modified = []

check_list = ['duration', 'attack', 'editAttack', 'cat', 'ite', 'fSpec', 'allowKeyTrigger', 'rid', 'vx', 'bx1']

for i in range(0, len(action_group)):
    printed = False
    if (action_group[i][3] != action_group_old[i][3]):
        print(f"{i}) {action_group[i]}:")
        print("Numbers of frames are different.")
        printed = True
    else:
        for j in range(0, action_group[i][3]):
            diff_key = []
            for key in key_table:
                if frame_data[str(action_group[i][1] + j)][key] != frame_data_old[str(action_group_old[i][1] + j)][key]:
                    if (key in check_list):
                        diff_key.append(key)
                    if (len(modified) == 0 or (key in modified) == False):
                        modified.append(key)
            if (len(diff_key) > 0):
                if (printed == False):
                    print(f"{i}) {action_group[i]}:")
                    printed = True
                print(f"{action_group[i][1] + j} vs {action_group_old[i][1] + j}: {diff_key}")
    if (printed == True):
        print("")

#print("Different table:", modified)