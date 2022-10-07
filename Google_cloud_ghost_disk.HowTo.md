# Shrink Google Cloud VM disk size
## Tested working with Ubuntu boot disk

The Google Cloud VM I am using is Ubuntu 20 LTS. Shrank the boot disk with Boot and EFI. Google system itself doesn't support make a disk smaller. But you always can make it bigger. Easier to spend more but no way to cost down.

This method can be down hot machines. No need to turn of it. 

### First make a smaller disk, and mount to your VM (with the disk to shrink)

Here I generate the smaller disk from Ubuntu public image by making a new VM. While making the new VM, remember to check "Keep disk" for your boot disk. The new smaller disk will have partition table made and the Boot partition is ready to go. During the following steps, we will find there is no way to duplicate the Boot partition.

After the new VM generated, delete it. Since we check the "Keep disk", the boot disk will be available to be mounted to the VM with disk to shrink. Mount the disk by editing that machine, and this step is done.

### Install weresync

There are several different ways to install it. But I found it can be done by apt directly now. Why not use the official way to install?

### Clone the disk

After running `lsblk` one can see the partitions as below for this example from a Google Cloud VM instance:
```
sda       8:0    0    75G  0 disk 
├─sda1    8:1    0  74.9G  0 part /
├─sda14   8:14   0     4M  0 part 
└─sda15   8:15   0   106M  0 part /boot/efi
sdb       8:16         5G  0 disk
├─sdb1    8:17   0   4.9G  0 part
├─sdb14   8:18   0     4M  0 part 
└─sdb15   8:19   0   106M  0 part 
```
One might run:
```
weresync -C --root-partition 1 --efi-partition 15 /dev/sda /dev/sdb
```
Or in shorthand:
```
weresync -C -g 1 -E 15 /dev/sda /dev/sdb
```

### Copy fstab

Running the command above gave an error message about `fstab` for me. If we use the new small disk to boot a new VM. It won't work.

Since the partition arrangement are identical in the two disks. I just manually copy `/etc/fstab` from the big disk to small disk. The file looks like below. There is not UUID in the file. If there is, you may need modify them.
```
LABEL=cloudimg-rootfs   /  ext4   defaults 0 0
LABEL=UEFI /boot/efi vfat defaults 0 0
```

Today is Oct 7, 2022. The method works for the current GCP.
Good luck. 

