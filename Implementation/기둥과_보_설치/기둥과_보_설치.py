

def check_all(frames):  # 모든 기둥과 보가 정상이면 True, 아니면 False
    for x, y, a in frames:
        if a == 0:  # 기둥 일 때
            if y == 0:
                continue
            if [x, y - 1, 0] in frames or [x, y, 1] in frames or [x - 1, y, 1] in frames:
                continue
            return False
        if a == 1:  # 보 일 때
            if [x, y - 1, 0] in frames or [x + 1, y - 1, 0] in frames:  # 기둥이 있을 때
                continue
            if [x - 1, y, 1] in frames and [x + 1, y, 1] in frames:
                continue
            return False
    return True


def solution(n, build_frame):
    frames = []

    for x, y, a, b in build_frame:
        if b == 1:  # 설치
            if a == 0:  # 기둥
                if y == 0 or [x, y - 1, 0] in frames or [x, y, 1] in frames or [x - 1, y, 1] in frames:
                    frames.append([x, y, 0])
            if a == 1:  # 보
                if [x, y - 1, 0] in frames or [x + 1, y - 1, 0] in frames or (
                        [x - 1, y, 1] in frames and [x + 1, y, 1] in frames):
                    frames.append([x, y, 1])
        if b == 0:  # 삭제
            if [x, y, a] in frames:
                frames.remove([x, y, a])
            if not check_all(frames):
                frames.append([x, y, a])
    frames.sort()
    return frames
