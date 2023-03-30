"""Main module"""
from ipykernel.kernelapp import IPKernelApp
from .kernel import jansvbkernel
IPKernelApp.launch_instance(kernel_class=jansvbkernel)
