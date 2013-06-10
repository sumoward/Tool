import os


class File_template_handling:

    def directory(self):
        self.path = 'static/downloads'
        print('@handler@', self.path)
        #get the current directory
        self.origdir = os.getcwd()
        self.relativepath = (os.path.relpath(self.origdir))
        print('the present directory is ', self.relativepath)
        #change to the file storage directory
        os.chdir(self.path)
        #get curent
        current = os.getcwd()
        print(current)
        list_of_files = os.listdir(self.relativepath)
        print('please choose the files needed from :\n', list_of_files)
        for file in list_of_files:
            locfile = os.path.join(self.relativepath, file)
            print('\n', locfile)
        #return to orginal directory
        os.chdir(self.origdir)
        print('\nthe present directory is ', os.getcwd())

        return  list_of_files


if __name__ == "__main__":
    handler = File_template_handling()
    handler.directory()
