l, c = map(int, input().split(' '))
seq = list(input().split(' '))

vowel = []
consonant = []

for seq_elem in seq:
    if seq_elem in ['a', 'e', 'i', 'o', 'u']:
        vowel.append(seq_elem)
    else:
        consonant.append(seq_elem)

seq.sort()
ans = []

# 모든 조합을 보고 하나의 모음, 두개의 자음을 가질 때 ans에 넣어주기
def bt(i, picked):
    
    if len(picked) == l:

        # 모음, 자음 개수 새기
        vowel_cnt, consonant_cnt = 0, 0
        for picked_elem in picked:
            if picked_elem in vowel:
                vowel_cnt += 1
            elif picked_elem in consonant:
                consonant_cnt += 1

        # 조건 이상이면 정답에 추가
        if vowel_cnt >= 1 and consonant_cnt >= 2:
            ans.append(''.join(picked))
        return

    for j in range(i, len(seq)):
        bt(j+1, picked+[seq[j]])


bt(0, [])

for ans_elem in ans:
    print(ans_elem)