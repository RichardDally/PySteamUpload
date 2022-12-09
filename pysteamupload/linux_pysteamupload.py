import tarfile
from abc import abstractmethod
from pysteamupload.generic_pysteamupload import GenericPySteamUpload


class LinuxPySteamUpload(GenericPySteamUpload):
    @abstractmethod
    def get_steamcmd_local_filename(self) -> str:
        return "steamcmd.sh"

    @abstractmethod
    def get_steamcmd_remote_filename(self) -> str:
        return "steamcmd_linux.tar.gz"

    @abstractmethod
    def extract_steamcmd_archive(self) -> None:
        with tarfile.open(self.get_archive_path(), 'r:gz') as f:
            
            import os
            
            def is_within_directory(directory, target):
                
                abs_directory = os.path.abspath(directory)
                abs_target = os.path.abspath(target)
            
                prefix = os.path.commonprefix([abs_directory, abs_target])
                
                return prefix == abs_directory
            
            def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
            
                for member in tar.getmembers():
                    member_path = os.path.join(path, member.name)
                    if not is_within_directory(path, member_path):
                        raise Exception("Attempted Path Traversal in Tar File")
            
                tar.extractall(path, members, numeric_owner=numeric_owner) 
                
            
            safe_extract(f, path=self.root_directory)
