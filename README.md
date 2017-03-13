# Gear Detector for FIRST Steamworks

**Forked from [weiliu89/caffe](https://github.com/weiliu89/caffe/tree/ssd/)**

This is a CNN (convolutional neural network) for detecting the gear game pieces in FIRST Steamworks. It uses the [SSD](https://arxiv.org/abs/1512.02325) architecture.

## Installation

Follow the installation instructions from [weiliu89/caffe](https://github.com/weiliu89/caffe/tree/ssd/#installation).

## Preparing Data

#### Setup environment variables:

Set `$CAFFE_ROOT` to the directory caffe is in:
```sh
export CAFFE_ROOT=<your caffe installation path>
```

#### Download VGGNet

This downloads a pretrained VGGNet model. **Warning:** this will download an **82 MB** file.

```sh
mkdir  -p $CAFFE_ROOT/models/VGGNet
cd $CAFFE_ROOT/models/VGGNet
wget http://cs.unc.edu/~wliu/projects/ParseNet/VGG_ILSVRC_16_layers_fc_reduced.caffemodel
```

#### Download the gear training data:

```sh
mkdir -p ~/data/VOCdevkit_STEAMWORKS
cd ~/data/VOCdevkit_STEAMWORKS
git clone https://github.com/Team334/gear-data.git GearData
```

#### Create LMDB files:
```sh
cd $CAFFE_ROOT
./data/STEAMWORKS/create_data.sh
```

## Training

Train the model using `examples/ssd/ssd_pascal_steamworks.py`:

```sh
cd $CAFFE_ROOT
python examples/ssd/ssd_pascal_steamworks.py
```

You can change the script to suite your needs:
- The GPUs to use can be specified [here](https://github.com/Team334/gear-detector/blob/450c6132dd7cfa514c46e71051c8cccb0623a4a8/examples/ssd/ssd_pascal_steamworks.py#L332).
- The number of iterations to run can be specified [here](https://github.com/Team334/gear-detector/blob/450c6132dd7cfa514c46e71051c8cccb0623a4a8/examples/ssd/ssd_pascal_steamworks.py#L374)
