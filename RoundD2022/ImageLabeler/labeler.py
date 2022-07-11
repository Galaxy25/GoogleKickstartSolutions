cases = int(input())
for i in range(1, cases+1):
    input()
    audio = [int(u) for u in input().split(" ")]
    input()
    labeler = [int(u) for u in input().split(" ")]
    size = int(input())

    labelerLeft = [0]
    labelerRight = [0]
    audioLeft = [0]
    audioRight = [0]

    for u in labeler[:size+2]:
        labelerLeft.append(u+labelerLeft[-1])
    for u in audio[:size+2]:
        audioLeft.append(u+audioLeft[-1])
    for u in labeler[::-1][:size+2]:
        labelerRight.append(u+labelerRight[-1])
    for u in audio[::-1][:size+2]:
        audioRight.append(u+audioRight[-1])
        
    labelerLeft.append(0)
    labelerRight.append(0)
    audioLeft.append(0)
    audioRight.append(0)
    total = 0
    
    for u in range(max(size - len(audio), 0), min(size, len(labeler))+1):
        labelMax = 0
        audioMax = 0
        if u > 0:
            a = u
            o = 0
            while a >= 0:
                labelMax = max(labelMax, labelerLeft[a] + labelerRight[o])
                a -= 1
                o += 1
        if size - u > 0:
            a = size - u
            o = 0
            while a >= 0:
                audioMax = max(audioMax, audioLeft[a] + audioRight[o])
                a -= 1
                o += 1
        total = max(total, labelMax+audioMax)
    print(f"Case #{i}: {total}")