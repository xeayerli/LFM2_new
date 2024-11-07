# LFM2_new
MemoryLan Axolotl Project Day 2 files

This is the template code to create a new version of this task suitable for LFM2 study follow up.

day2.py runs with the dependency of day1.py for the original study, but is not needed for LFM2. 

TODO: 
1. create two version of the task (participants are randomly assigned to two different image directories during the first day). Image directory for version A and version B are different. The folders needed are "maindir_A", "maindir_B", "foildir_A", "foildir_B". During the task, participants will be seeing all the images in a maindir and a foildir depending on which version they did the previous day (one by one, random order)
2. for day2.py: remove the dependency on day1.py in /results. Day 2 should be a stand-alone file.
3. remove the intrusion question in the file (only recall yes/no question needed)
4. add question: "Enter version number during the previous day" answer should be A or B
5. data to be saved in csv: don't need the valence category (instead need version A or B), response time for key press, accuracy (if foil image answered yes = FALSE, if main img answered yes = TRUE)
