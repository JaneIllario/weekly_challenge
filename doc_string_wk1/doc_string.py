import os

files=''
path = 'C:\Users\janei\OneDrive\Desktop\Projects\github\weekly_challenge\doc_string_wk1\src_txt'

for file in os.listdir(path):
	doc=open(path+"\\"+file,"r")
	files=files+doc.read()+' '
print(files)

save_path = 'C:\Users\janei\OneDrive\Desktop\Projects\github\weekly_challenge\doc_string_wk1'

with open(os.path.join(save_path, "output"), "w+") as output_file:
	output_file.write(files)