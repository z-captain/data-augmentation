import skimage
import os
import numpy as np
from skimage import io
from os import listdir
from skimage.transform import resize


class_label_file = 'original_data/train_class_labels.txt'
f=open(class_label_file)
lines=f.read().splitlines()
train_labels={}
f.close()
for i in range(0,len(lines)):
    tmp=lines[i].split("\t")
    filename=tmp[0]
    Class=tmp[1]
    train_labels[filename]=Class
    
print('Number of training images:', len(train_labels.keys()))
imagedir='original_data/train/'
files=listdir('original_data/train/')

#makes a directory
if not os.path.exists('augmented_data/train/'):
    os.mkdir('augmented_data/train/')
augmentation_folder ='augmented_data/train/'
new_train_labels={}
NUM_ROTATE = 2
for i in range(0,len(files)):
    if(i%2000 == 0):
        print('done processing ' + str(i) + ' images')
    I = io.imread(imagedir+files[i])
    new_train_labels[files[i]] = train_labels[files[i]]
    io.imsave(augmentation_folder+files[i],I)
    for j in range(0,NUM_ROTATE):
        I1 = skimage.transform.rotate(I,angle=np.random.uniform(-45, 45))
        #print(I1.shape)
        newFile = "rotated_"+str(j)+"_"+files[i]
        io.imsave(augmentation_folder+"rotated_"+str(j)+"_"+files[i], I1)
        new_train_labels[newFile] = train_labels[files[i]]



new_train_label_file = 'augmented_data/train_class_labels.txt'
f=open(new_train_label_file,"w")
for keys in new_train_labels.keys():
    f.write(keys+"\t" + new_train_labels[keys]+"\n")
f.close()





