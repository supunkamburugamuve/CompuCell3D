
import CommandLineArgumentParser
import CC3DProjectFileReader
import ProjectFileStore
import os

class CC3DLauncher:

    def parseCommandLineArgument(self):
        commandLineArgumentParser = CommandLineArgumentParser.CommandLineArgumentParser()
        commandLineArgumentParser.initialize()
        commandLineArgumentParser.parseArguments()

    def loadCC3DProjectFile(self):
        cc3dReader = CC3DProjectFileReader.CC3DReader()
        cc3dReader.readCC3DFile(ProjectFileStore.projectFilePath)

    def configureCompuCellSetup(self):
        '''

        :return:
        '''
        '''
        Add directories to sys.path
            (1) PYTHON_MODULE_PATH - ../PythonSetupScripts which contains CompuCellSetup.py
            (2) Python Script Directory - It contains steppables used in the python script file 
        '''
        import sys
        sys.path.append(os.environ['PYTHON_MODULE_PATH'])
        sys.path.append(os.path.dirname(ProjectFileStore.pythonScriptPath))

        screenShotOutputDirectory = os.path.join(ProjectFileStore.outputDirectoryPath, "screenshots")
        # Configuration of CompuCellSetup
        # (1) Set the output directory for the Simulation
        import CompuCellSetup
        CompuCellSetup.playerType = "CML"
        print "Screenshot Storage Directory: ", screenShotOutputDirectory
        CompuCellSetup.simulationPaths.setSimulationResultStorageDirectory(screenShotOutputDirectory)


    def executeCompuCell3DSimulation(self):
        pythonScriptPath = ProjectFileStore.pythonScriptPath
        #subprocess.call([os.environ['PYTHON_EXEC'], pythonScriptPath])
        execfile(pythonScriptPath)


def main():
    cc3dLauncher = CC3DLauncher()
    cc3dLauncher.parseCommandLineArgument()
    cc3dLauncher.loadCC3DProjectFile()
    cc3dLauncher.configureCompuCellSetup()
    #cc3dLauncher.executeCompuCell3DSimulation()

if __name__ == '__main__':
    main()