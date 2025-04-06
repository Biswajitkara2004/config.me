from pyconfig.pyconfig import PyConfig
from j2power import j2p
scriptblocks = []



def GenerateScript(scriptblocks):
    if j2p.main(scriptblocks):
        print("Script generated successfully.")
    
Choice = input("choose your os(linux/windows): ")

if Choice == "linux":
    ...
elif Choice == "windows":
    

    setconfigfor = input("Choose configuration type: \n1. Desktop\n2. Enviroment\n3. Server\n4. software\n5. optimization system")
    if setconfigfor == "1":
        print("You chose Desktop configuration.")
        # Add hosting configuration code here
        
    elif setconfigfor == "2":
        print("You chose Enviroment configuration.")
        idechoice = input("do you need python idle or other Ide's (y/n)")
        if idechoice == 'y':
            #add ide configuration code here
            ide = input("Choose your IDE: \n1. VSCode\n2. PyCharm\n3. IntelliJ\n")
            if ide == "1":
                print("You chose VSCode.")
            elif ide == "2":
                print("You chose PyCharm.")
            elif ide == "3":
                print("You chose IntelliJ.")
            else:
                print("Invalid choice. Please choose a valid IDE.")
        else:
        
            # Add development configuration code here
            devenv = input("Choose your development environment: \n1. Python\n2. C/C++\n3. Web development\n4. Java development\n")
            if devenv == "1":
                
                # Use the PyConfig module to fetch Python versions
                python_versions = PyConfig.get_python_versions()
                
                version = input("Choose your Python version: ")
                
                download_pyver = PyConfig.download_python_version(version)
                scriptblocks.append(download_pyver)
                installpyver = PyConfig.install_python_version(download_pyver['vars']['file_name'])
                scriptblocks.append(installpyver)
                print("script block added successfully")
                
                library = input("Do you want to install any libraries? (yes/no): ")
                if library.lower() == "yes":
                    libnames = input("Enter the library names (comma-separated): ")
                    lib_list = [lib.strip() for lib in libnames.split(",")]  # Split and strip whitespace
                    for libname in lib_list:
                        scriptblocks.append(PyConfig.install_library(libname))
                    print("Library installation scripts added successfully.")
                else:
                    print("No library installation script added.")
                
    else:
        print("Invalid choice. Please choose either '1' or '2'.")
        exit()
else:
    print("Invalid choice. Please choose either 'linux' or 'windows'.")
    exit()

print(scriptblocks)
GenerateScript(scriptblocks)
