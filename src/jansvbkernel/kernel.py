"""Kernel Module"""
#!/usr/bin/env python
import os
import shutil
import pexpect
from ipykernel.kernelbase import Kernel


workingdir = "/tmp/monobasic/"

class jansvbkernel(Kernel):
    """The kernel for visual basic"""
    implementation = 'IPython'
    implementation_version = '8.10.0'
    language = 'basic'
    language_version = '4.8'
    language_info = {
        'name': 'VB.NET',
        'mimetype': 'application/vb',
        'file_extension': '.vb',
    }
    banner = "Visual Basic @ mono"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            if os.path.exists(workingdir):
                shutil.rmtree(workingdir)
            os.mkdir(workingdir)
            os.chdir(workingdir)
            with open(workingdir + "proj.basic", "w") as file:
                file.write(code)
            solution = pexpect.run('vbnc ' + workingdir  + 'proj.basic')
            if os.path.exists(workingdir+'proj.exe'):
                os.chmod(workingdir + 'proj.exe', 0o777)
                solution = pexpect.run(workingdir + 'proj.exe').decode('UTF-8')
            stream_content = {'name': 'stdout', 'text': solution}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }

    def do_shutdown(self, restart):
        if os.path.exists(workingdir):
            shutil.rmtree(workingdir)
