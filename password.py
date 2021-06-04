import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "↕↖↗↘↙↚↛↜↝↞↟↠↡↢↣↤↥↦↧↨↩↪↫↬↭↮ ↯↰↱↲↳↴↶↷↸↹↺↻↼↽↾↿⇀⇃⇄⇅⇆⇇⇈⇉⇊⇋⇌ "
lenth = 16
temp = random.sample(lower+upper+symbols,lenth)
password = "".join(temp)
print(password)