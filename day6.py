# ── BAD: No clue what's happening ─────────────────────────────────────
def calculate_average(scores):
    total = sum(scores)
    return total / len(scores)   # crashes if scores is empty!

# ── GOOD: Print debugging reveals the problem ─────────────────────────
def calculate_average(scores):
    print(f"[DEBUG] Input received: {scores}")     # see what came in
    print(f"[DEBUG] Length: {len(scores)}")        # see what len() returns
    if len(scores) == 0:
        print("[DEBUG] Empty list! Returning 0")
        return 0
    total = sum(scores)
    print(f"[DEBUG] Total: {total}")               # verify calculation
    avg = total / len(scores)
    print(f"[DEBUG] Average: {avg}")
    return avg

result = calculate_average([85, 90, 78])
# [DEBUG] Input received: [85, 90, 78]
# [DEBUG] Length: 3
# [DEBUG] Total: 253
# [DEBUG] Average: 84.33...
