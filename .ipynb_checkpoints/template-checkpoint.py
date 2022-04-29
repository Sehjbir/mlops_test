import os


dirs = ['notebooks',
        'src',
        'saved_models',
        os.path.join('data','raw'),
        os.path.join('data','processed')]


for dir_ in dirs:
    os.makedirs(dir_, exist_ok = True)
    with open(os.path.join(dir_,'.gitkeep'), 'w') as f:
        pass
    
files = ['dvc.yaml',
         'params.yaml',
         '.gitignore',
         os.path.join('src','__init__.py')]


for f in files:
    with open(f,'w') as f:
        pass