import random

words = [
    "absorb", "accent", "access", "acting", "action", "active", "actual", "adjust",
    "admire", "advice", "advise", "afford", "agency", "almost", "always", "amount",
    "animal", "answer", "anyone", "appear", "artist", "aspect", "assert", "assign",
    "assist", "assume", "attach", "attack", "attempt", "attend", "author", "autumn",
    "beauty", "become", "before", "behalf", "behave", "belief", "belong", "better",
    "beyond", "bishop", "bother", "bottle", "bottom", "branch", "breach", "breath",
    "bridge", "bright", "broken", "burden", "button", "camera", "cannot", "carbon",
    "career", "castle", "caught", "center", "chance", "change", "charge", "choice",
    "choose", "church", "circle", "client", "closed", "closer", "coffee", "colony",
    "column", "combat", "commit", "common", "comply", "consent", "consist", "contact",
    "contain", "content", "contest", "continue", "control", "convert", "cookie", "corner",
    "cotton", "county", "couple", "course", "covers", "create", "credit", "crisis"
]


def get_random_word():
    return random.choice(words)