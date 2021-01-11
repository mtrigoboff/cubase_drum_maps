# create_dm.py

_by [Michael Trigoboff](http://spot.pcc.edu/~mtrigobo)_

* * *

The **Montage Data List** PDF has a **Drum Kit Assign List** that shows, for each drum kit, the name of the sound that each assigned note will produce. For example, the first drum kit listed in the Data List for firmware version 1.5.0, **Schlager Weapon 1**, shows the name **Sd TB Comp1** for note **C0**.

It would be nice to have Cubase show you the correct names when using a particular Montage drum kit, but the only method Cubase provides to do that is to type in all the names by hand. Given that there are 128 different names for most of the drum kits, that would be a real pain.

This Python code lets you create a Cubase drum map for any of the Montage drum kits described in the Data List.

To do this, you need to create a text file containing the information about that drum kit from the Data List. Using **Schlager Weapon 1** as an example, open the Data List PDF to that page. Select from where it says **C0** down to and including the last item, **Electric Fx Perc9**. Copy the selected text, and paste it into a blank text document.

Add one line to the beginning of the text file. This line will contain the name of the drum map you are creating. The name of the drum kit would be a good choice here, but it's entirely up to you.

Save the text file with a name that contains no spaces. For **Schlager Weapon 1**, I used **SchlagerWeapon1.txt**.

Now you need to run the Python code. To do this, you need to install a Python interpreter, which you can get from [here](https://www.python.org/downloads/). Just choose the most recent one.

When you have the Python interpreter installed, open a command-line window such as Windows PowerShell. Navigate to the directory (i.e. folder) containing your text file, and run the Python code like this:

> <pre>python create_dm.py yourtextfile.txt</pre>

The Python code will create a Cubase drum map file named **yourtextfile.drm**. Note that the internal name of the drum map will be taken from the first line of the text file, _not_ from the name of the text file.

Once you have created your drum map file, you just need to import it into Cubase as described in the Cubase documentation.

The provided zip file expands into a folder that includes these instructions, the Python code (**create_dm.py**), an empty Cubase drum map file (**empty.drm**) that is used by the Python code, and some example text files and the drum maps that the code produced from them.