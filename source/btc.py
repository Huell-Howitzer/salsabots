import json
import subprocess

x = subprocess.run(['cryptoco-py', 'sprice', 'bitcoin'], capture_output = True)
x.check_returncode()

y = json.loads(x.stdout)

z = y["bitcoin"]
print(f"Current price: ${z['usd']}")