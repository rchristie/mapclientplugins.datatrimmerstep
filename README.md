# mapclientplugins.datatrimmerstep
A mapclient step to trim anatomical mesh groups from Zinc EX data files.

Clone the repo:

`git clone https://github.com/mahyar-osn/mapclientplugins.datatrimmerstep.git`

You should then add the path of the location where you cloned the repo to the mapclient plugin manager.
The plugin will then appear under the 'Utility' category:

![alt text](resources/utility.png)

### A typical workflow using this plugin:

The plugin has one input port for the Zinc EX data file using the "File Chooser" plugin. The output port provides
a new, trimmed Zinc EX data file.

![alt text](resources/workflow.png)

### The UI:

The UI is very simple. The plugin automatically discovers all the groups in the Zinc file and populates them in the 
'Control Panel' on the left side bar as a set of checkboxes. Initially, these checkboxes are all checked.
Unchecking them will remove the corresponding groups from the scene view. When you press the "Done" button, only
the checked checkboxes will remain and a new file with those groups will be saved in the same directory as the original data file.

#### Example:
##### - Step 1:

![alt text](resources/step1.png)

##### - Step 2:

![alt text](resources/step2.png)
