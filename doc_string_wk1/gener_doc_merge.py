import os

txt_path = 'C:\Users\janei\OneDrive\Desktop\Projects\github\weekly_challenge\doc_string_wk1\src_txt'
save_path = 'C:\Users\janei\OneDrive\Desktop\Projects\github\weekly_challenge\doc_string_wk1'

open(os.path.join(save_path, "output"), "w+").write(" ".join([open(os.path.join(txt_path, itr_file), "r").read() for itr_file in os.listdir(txt_path)]))

#OR
#broken up for readability

# txt=[open(os.path.join(txt_path, itr_file), "r").read() for itr_file in os.listdir(txt_path)]
# open(os.path.join(save_path, "output"), "w+").write(" ".join(txt))
