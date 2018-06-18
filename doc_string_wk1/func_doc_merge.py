import os
save_path = 'C:\Users\janei\OneDrive\Desktop\Projects\github\weekly_challenge\doc_string_wk1'
txt_path = os.path.join(save_path, "src_txt")

open(os.path.join(save_path, "output"), "w+").write(" ".join(list(map(lambda x: open(os.path.join(txt_path, x), "r").read(), os.listdir(txt_path)))))
print("it worked!")