import json
import glob
import os

base = r"c:\Users\tterrag\.vscode\SMF1trials\PoetPundit\poet_pundit"
prompt_files = glob.glob(os.path.join(base, "prompts", "*.json"))
const_files = glob.glob(os.path.join(base, "techConstraints", "*.json"))

prompt_cats = set()
for f in prompt_files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                prompt_cats.add(item.get("category", "Unknown"))
    except: pass

const_types = set()
const_diffs = set()
for f in const_files:
    try:
        with open(f, 'r', encoding='utf-8') as file:
            data = json.load(file)
            for item in data:
                const_types.add(item.get("type", "Unknown"))
                const_diffs.add(item.get("difficulty", "Unknown"))
    except: pass

print("Prompt Categories:", list(prompt_cats))
print("Const Types:", list(const_types))
print("Const Difficulties:", list(const_diffs))
