"""Kernel install helper"""
#!/usr/bin/env python
import os
import shutil

from jupyter_client.kernelspec import KernelSpecManager

JSON ="""{"argv":["python","-m","jansvbkernel", "-f", "{connection_file}"],
 "display_name":"Visual Basic"
}"""

SVG = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   id="Layer_1"
   viewBox="0 0 300 300"
   version="1.1"
   width="300"
   height="300"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:cc="http://creativecommons.org/ns#"
   xmlns:dc="http://purl.org/dc/elements/1.1/">
  <defs
     id="defs4">
    <style
       type="text/css"
       id="style2">.cls-1{fill:#004e8c;}.cls-2,.cls-3{fill:#fff;}.cls-2{opacity:0.1;}</style>
  </defs>
  <title
     id="title6">logo_vb</title>
  <g
     id="g306"
     transform="matrix(4.6231565,0,0,4.6231565,4.1179868,0)">
    <circle
       class="cls-1"
       cx="32"
       cy="32"
       r="32"
       id="circle8" />
    <path
       class="cls-2"
       d="M 9.82,9 A 32,32 0 1 0 55,54.18 Z"
       id="path10" />
    <path
       class="cls-3"
       d="M 33.29,19.4 24,44.6 H 20.71 L 11.57,19.4 h 3.29 l 7,20 a 11.87,11.87 0 0 1 0.51,2.23 h 0.07 A 11,11 0 0 1 23,39.35 l 7.12,-20 z"
       id="path12" />
    <path
       class="cls-3"
       d="M 36.92,44.6 V 19.4 h 7.17 a 7.84,7.84 0 0 1 5.18,1.6 5.17,5.17 0 0 1 1.92,4.17 6.13,6.13 0 0 1 -1.19,3.72 6.26,6.26 0 0 1 -3.2,2.25 v 0.07 a 6.41,6.41 0 0 1 4.08,1.92 5.92,5.92 0 0 1 1.53,4.23 6.59,6.59 0 0 1 -2.32,5.24 8.64,8.64 0 0 1 -5.85,2 z m 3,-22.54 v 8.14 h 3 A 5.74,5.74 0 0 0 46.71,29 4.07,4.07 0 0 0 48.1,25.7 q 0,-3.67 -4.83,-3.67 z m 0,10.79 v 9.07 h 4 a 6,6 0 0 0 4,-1.23 4.21,4.21 0 0 0 1.43,-3.37 q 0,-4.46 -6.08,-4.46 z"
       id="path14" />
  </g>
  <metadata
     id="metadata192">
    <rdf:RDF>
      <cc:Work
         rdf:about="">
        <dc:title>logo_vb</dc:title>
      </cc:Work>
    </rdf:RDF>
  </metadata>
</svg>
"""

def install_kernelspec():
    """Installs the jupyter vb kernel"""
    kerneldir = "/tmp/jansvbkernel/"
    print('Creating tmp files...', end="")
    os.mkdir(kerneldir)

    with open(kerneldir + "kernel.json", "w", encoding="utf-8") as file:
        file.write(JSON)

    with open(kerneldir + "logo-svg.svg", "w", encoding="utf-8") as file:
        file.write(SVG)

    print(' Done!')
    print('Installing Jupyter kernel...', end="")

    ksm = KernelSpecManager()
    ksm.install_kernel_spec(kerneldir, 'jansvbkernel', user=os.getenv('USER'))

    print(' Done!')
    print('Cleaning up tmp files...', end="")

    shutil.rmtree(kerneldir)

    print(' Done!')
    print('For uninstall use: jupyter kernelspec uninstall jansvbkernel')
