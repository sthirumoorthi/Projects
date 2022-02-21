# **MongoDB Operations using Python**

## **Project Overview:**
  This repository contains a Jupyter Notebook with origianl carbon nanotubes dataset and other python modules, designed to perform MongoDB operations for the given dataset. A cloud version of the MongoDB (Atlas) is being used in this project as a storage repository. 
  
### **Functionalities:**
 - [x] **<ins>Database and Collection:</ins>** New database and collection has been created during the project initiation (using OOP Python script).
 - [x] **<ins>Bulk Load:</ins>** The Carbon Nanotubes csv file has been loaded into Mongo DB Atlas
 - [x] **<ins>Insert Documents:</ins>** Performed insert_many() and insert_one() operation on the MongoDB collections
 - [x] **<ins>Update Documents:</ins>** Updates the documents in the MongoDB Collection (update_many() and update_one()).
 - [x] **<ins>Delete Documents:</ins>** Deleted the documents in the MongoDB Collection (delete_many() and delete_one()).
 - [x] **<ins>Find and Filter:</ins>** Performed various Find and Filter operations on the MongoDB Collection.
 - [x] **<ins>Drop Collection:</ins>** Drop the collection once the above functionalities are done.

### **Carbon Nanotubes Data:**
CASTEP can simulate a wide range of properties of materials proprieties using density functional theory (DFT). DFT is the most successful method calculates atomic coordinates faster than other mathematical approaches, and it also reaches more accurate results. The dataset is generated with CASTEP using CNT geometry optimization. Many CNTs are simulated in CASTEP, then geometry optimizations are calculated. Initial coordinates of all carbon atoms are generated randomly. Different chiral vectors are used for each CNT simulation. The atom type is selected as carbon, bond length is used as 1.42 A° (default value). CNT calculation parameters are used as default parameters. To finalize the computation, CASTEP uses a parameter named as elecenergytol (electrical energy tolerance) (default 1x10-5 eV) which represents that the change in the total energy from one iteration to the next remains below some tolerance value per atom for a few self-consistent field steps. Initial atomic coordinates (u, v, w), chiral vector (n, m) and calculated atomic coordinates (u’, v’, w’) are obtained from the output files.
The summary of the attributes is given below. Please read the papers (https://doi.org/10.1007/s00339-016-0153-1 and https://doi.org/10.17341/gazimmfd.337642) for detailed descriptions of the attributes

#### **Summary of columns:**
 - <ins>Chiral indice n:</ins> n parameter of the selected chiral vector.
 - <ins>Chiral indice m:</ins> m parameter of the selected chiral vector.
 - <ins>Initial atomic coordinate u:</ins> Randomly generated u parameter of the initial atomic coordinates of all carbon atoms.
 - <ins>Initial atomic coordinate v:</ins> Randomly generated v parameter of the initial atomic coordinates of all carbon atoms.
 - <ins>Initial atomic coordinate w:</ins> Randomly generated w parameter of the initial atomic coordinates of all carbon atoms.
 - <ins>Calculated atomic coordinate u’:</ins> Calculated u’ parameter of the atomic coordinates of all carbon atoms.
 - <ins>Calculated atomic coordinate v’:</ins> Calculated v’ parameter of the atomic coordinates of all carbon atoms.
 - <ins>Calculated atomic coordinate w’:</ins> Calculated w’ parameter of the atomic coordinates of all carbon atoms.

# **Highlights:**
 - Application was designed using the OOP concept
 - Multiple classes were created for this use case
 - Class created for Mongo DB operations follows Hybrid Inheritance and standalone class was created for CSV data read and dictionary conversion
 - Followed the Modular programming concept
 - Try and catch is being followed to capture the exceptions
 - Logging mechanism is being used to capture the application navigation and control. It will capture the info, Error and Exception details.

# **Application Architecture:**
![image](https://user-images.githubusercontent.com/90926526/155011416-990a895a-420e-4067-9b2d-1f86ef9bfe77.png)


# **Modules Used:**
![image](https://user-images.githubusercontent.com/90926526/155007325-2e75717f-91a3-48b1-9186-90dea099c50f.png)
![image](https://user-images.githubusercontent.com/90926526/155007036-ed189605-fa36-4b36-b06f-ea70f123a057.png)
![image](https://user-images.githubusercontent.com/90926526/155007169-96dff99c-b884-4a73-bc69-e5311c64c70d.png)


#### Additional libraries:
  - logging

# **Folder Structure:**
![image](https://user-images.githubusercontent.com/90926526/155008837-9930212e-3f04-42fe-a040-5715e1c09803.png)


# **Screenshots**

Initial screen:

![image](https://user-images.githubusercontent.com/90926526/155009428-54ab3e95-915a-47c8-9f2d-071fca841a2f.png)

After loading the CSV file to DB:

![image](https://user-images.githubusercontent.com/90926526/155009156-ae970b7f-a91c-40c9-a5e6-935a32ff2743.png)

Document format in MongoDB:

![image](https://user-images.githubusercontent.com/90926526/155009266-f0f4811d-cc69-4458-ac21-07fe9b64e21e.png)

Document filter samples:

![image](https://user-images.githubusercontent.com/90926526/155009313-906f96e3-448e-478c-88e9-9a3a755511a5.png)
![image](https://user-images.githubusercontent.com/90926526/155009348-3652e9d5-4f16-4f38-a19a-493c41688391.png)
![image](https://user-images.githubusercontent.com/90926526/155009475-98280a6e-e5f2-4cab-9814-352f06bbce5d.png)


# **References:**
- Based on the notes from [iNeuron](https://ineuron.ai/)  (Thanks to Sudhanshu & Sunny)
- PyMongo [documentation](https://pymongo.readthedocs.io/en/stable/tutorial.html)
- The dataset used in the Jupyter Notebook was downloaded from the [University of California, Irvine's Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Carbon+Nanotubes). A special thanks is to be given to the original authors Mehmet Acı and Mutlu Avcı, whose work is cited below.

Acı, M., Avcı, M. Artificial neural network approach for atomic coordinate prediction of carbon nanotubes. Appl. Phys. A 122, 631 (2016). https://doi.org/10.1007/s00339-016-0153-1
