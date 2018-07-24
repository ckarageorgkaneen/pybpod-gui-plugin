import pyforms, git
from pyforms.basewidget import BaseWidget
from pyforms.controls   import ControlProgress
from pyforms.controls   import ControlList

class CodeUpdatedException(Exception):pass

class UpdateCenter(BaseWidget):

    TITLE = 'Update center'

    def __init__(self, *args, **kwargs):
        super().__init__(self.TITLE, **kwargs)

        self._list     = ControlList('Modules')
        self._progress = ControlProgress('Progress')

        self.formset = ['_list', '_progress']

        self.verify_version()
    
    def verify_version(self):

        local_repo  = git.Repo(".")
        remote_repo = local_repo.remotes.origin
        
        local_commit = local_repo.head.commit
        remote_commit = remote_repo.repo.head.commit

        local_date = local_commit.committed_datetime
        remote_date = remote_commit.committed_datetime

        if local_date<remote_date:

            answer = self.question(
                """A new version from {0} is available. Your version is from {1},
                would you like to update it?""".format(local_date, remote_date)
            )

            if answer=='yes':
                self.message('The application was updated with success, please start the application again.',title='Updated')
                raise CodeUpdatedException()

        #else:
        #    for submodule in local_repo.submodules:
        #        submodule.update()



def start_update_center(self):
    pyforms.start_app(UpdateCenter)
