*********************************************************************************

snapQC v1.0  
Developer: Akshay Sawardekar  
Date: 26 July 2024

*********************************************************************************

Step-by-Step Guide to Install and Use snapQC in Nuke:

1. Copy the entire **'snapQC'** folder into your **.nuke** directory.

2. Locate the **'init.py'** file inside the snapQC folder and:
   - If you **don’t** have an `init.py` in your `.nuke` folder, just copy it there.
   - If you **already have** an `init.py`, just copy the contents of `snapQC/init.py` into your existing `.nuke/init.py`.

3. Launch Nuke. You should now see **SnapQC** in your toolbar.

4. To use:
   - Open any saved Nuke script.
   - Hit **Shift + Q** or click the **SnapQC** button.
   - A snapshot of the current viewer frame will be saved into a `feedback` folder, automatically created beside your script.

⚠️ Note: The script **must be saved** for the tool to work properly, unsaved scripts won’t generate snapshots.

Enjoy and thanks for trying SnapQC!

