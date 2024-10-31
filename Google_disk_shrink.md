# Shrink Google Cloud VM disk 

Google does not have the function to resize their disk smaller. To make the disk smaller requires making new disk and transfer data to it.

* For data disk use rsync 
* Start with a smaller boot disk with same system first for the booting disks. Then use fsarchiver to replicate the root partition and EFI partition. And the most important, make sure that UUID in EFI partition are same to the new disk UUID, and the PARTUUID in the root partition's `boot/grub` aligns with the new root partition.

