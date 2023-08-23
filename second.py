import os

first_name =os.environ.get("FIRST_NAME")
last_name =os.environ.get("LAST_NAME")

home_dir = os.path.expanduser("~")
tmp_dir = os.path.join(home_dir, "tmp")
os.makedirs(tmp_dir, exist_ok=True)
num_sub_dirs = 5
for i in range(num_sub_dirs):
	sub_dir = os.path.join(tmp_dir, f"training_project_{i+1}")
	os.makedirs(sub_dir, exist_ok=True)
	for file_type in ['a', 'b']:
	    file_name = f"module_{i+1}_{file_type}.txt"
	    file_path = os.path.join(sub_dir, file_name)
	    content = f'Hello {first_name} {last_name} Welcome to file {i+1}.{file_type}'
	    with open(file_path, 'w') as f:
	        f.write(content)

