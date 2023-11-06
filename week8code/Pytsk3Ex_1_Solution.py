'''
The following skeleton code is designed to help you with the structure of the practice program
for the pytsk Workshop 1
As always, if you feel like something does not make sense, ask for help from your tutor, or
read the relevant documentation.
'''

# 1 Import the required Library
import pytsk3

# 2 Create a new IMG_Info object by opening the file and name object as diskimage
diskimage = pytsk3.Img_Info("diskimageMT.001")

# 3 Display the size of the disk image in raw bytes
print(f"The image file size is {diskimage.get_size()} bytes in size")

# 4 closes the disk image much like the close method unlinked a file from a program using Python File I/O.
diskimage.close()

# 5 Display the number of sectors there are in the disk image file
totalSecors = diskimage.get_size()/512
print(f"Total number of sectors in image is {totalSecors} ")

# 6 Create a Volume_Info object for the Img_Info object to get a Volume_Info object containing the partitions defined in the disk image
volume_info = pytsk3.Volume_Info(diskimage)

# 7 Displays the number of partitions pytsk3 has identified in the disk image.
print(f"Number of Partitions in image is {volume_info.info.part_count}")

# 8 Defines the start of a for loop for processing each partition in the disk image.
part_offsets = []
for volume in volume_info:
    # 9 displays a description of the partition’s type, start sector and number of sectors in the partition
    #print(f" Partition type {volume.desc}, start LBA {volume.start}, number of sectors {volume.len}")
    # Convert the bytes into a string for volume.desc
    print(f" Partition type {volume.desc.decode('ascii')}, start LBA {volume.start}, number of sectors {volume.len}")

    # 11 This statement adds the current volume’s start sector to the end of the list each iteration
    part_offsets.append(volume.start)

# 12 Display the contents of the partitions list
print(f"part_offsets are {part_offsets}")