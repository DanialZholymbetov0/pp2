import re
text =input()
text = re.sub(r'_', ' ', text) 
text = re.sub(r'\b\w', lambda x: x.group(0).upper(), text)
text = re.sub(r'\s', '', text)  
print(text)