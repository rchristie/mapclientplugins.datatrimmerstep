# mapclientplugins.datatrimmerstep
A mapclient step to trim anatomical mesh groups from Zinc EX data files.

Clone the repo:

`git clone https://github.com/mahyar-osn/mapclientplugins.datatrimmerstep.git`

You should then add the path of the location where you cloned the repo to the mapclient plugin manager.
The plugin will then appear under the 'Utility' category:

![alt text](resources/utility.png)

### A typical workflow using this plugin:

The plugin has one input port for the Zinc EX data file using the "File Chooser" plugin. The output port port provides
a new, trimmed Zinc EX data file.

![alt text](resources/workflow.png)

### The UI:

The UI is very simple. The plugin automatically discovers all the groups in the Zinc file and populate them in the 
Control Panel on the left side bar. You can select the group(s) that you want to delete by selecting the checkbox(es) 
and then click on the "Destroy selected groups" to remove those groups. Once you're done, you can press the "Done" button
and the new file will be saved in the same directory as the original data file.

#### Example:
##### - Step 1:

![alt text](resources/step1.png)

##### - Step 2:

![alt text](resources/step2.png)
