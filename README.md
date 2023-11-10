## UMIACS SETUP
1. Download Remote Explorer on vscode
2. configure ssh to ssh c-------@nexusclass01.umiacs.umd.edu (press add button then type ssh cmd)
3. type umiacs password
4. type 'push' when prompted for password again
5. approve on dup
6. type umiacs password again
7. type 'push' again
8. approve on duo again
You are now logged in :)
<img width="271" alt="image" src="https://github.com/hbalickgoodman/image-generation-CMSC421/assets/56572956/9af25997-fb93-4751-9630-755024b59299">
Click open folder and you will see all of your files on UMIACS

## CONDA SETUP
Download and setup miniconda (we are using linux)
https://docs.conda.io/projects/miniconda/en/latest/


## Run on GPU cluster
Make sure to do this before you run the python file
`srun --pty --partition=class --account=class --qos=default --gres=gpu:1 bash`

## Install pytorch and transformers
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
pip install transformers

## Running the script
``` python image-gen.py 'prompt' filename ```


Ex: ``` python image-gen.py 'cat with very long neck standing on a chair' cat.png ```
