from distutils.core import setup  
import py2exe  
import matplotlib
  
setup(
    windows=[
        {"script":"Application.pyw", 
         "icon_resources": [(1, "images/tempmonitor.ico")]
         }],
    # options={
    #     "py2exe":{
    #         "includes": []
    #         }
    #     }
    # data_files=[(".", [r".\162.bin"])]
    data_files=matplotlib.get_py2exe_datafiles(),
    )
