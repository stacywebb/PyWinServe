#!/usr/bin/env python


############################################################################
# 
# File: PyWinServe - Run any Python Script as a Windows Service
# Version: 0.5
# Author: Stacy E. Webb
# URL: http://stacywebb.com
# REPO: http://gitub.com/stacywebb/PyWinServe
############################################################################

import threading
import socket
import subprocess
import time
import servicemanager
import win32serviceutil
import win32service
import win32event


class PyWinServe(win32serviceutil.ServiceFramework):
	"""
	Creates Windows Service
	"""
	_svc_name_ = "YourPythonService"
	_svc_display_name_ = "YourPythonNmae"
	_svc_description_ = "YourDescription"
	_svc_deps_ = ["EventLog"]

	def __init__(self, args):
		#sys.stdout = open(os.path.join(VALCOMALERTPATH, "ValcomAlert_service.log"), "a")
		win32serviceutil.ServiceFramework.__init__(self, args)
		self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

	def SvcStop(self):
		"""
		Stops the service
		"""
		self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
		win32event.SetEvent(self.hWaitStop)

	def SvcDoRun(self):
		"""
		Write a 'started' event to the event log...
		"""
		servicemanager.LogInfoMsg("YourPythonService is starting.")
		servicemanager.EVENTLOG_INFORMATION_TYPE, (self._svc_name_, '')

		while True:
			result = win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)
			if result == win32event.WAIT_OBJECT_0:
				break

		# and write a 'stopped' event to the event log.
		servicemanager.LogInfoMsg("YouPythonService is stopping.")
		servicemanager.EVENTLOG_INFORMATION_TYPE, (self._svc_name_, '')

	def loopcall(self, myfunction, wait):
		"""
		basically Waits
		:param myfunction:
		:param wait:
		"""
		self.timer = threading.Timer(wait, myfunction)
		self.timer.start()

	def loop(self):
		"""
		Put your Python Script here
		"""

if __name__ == '__main__':
	# Note that this code will not be run in the 'frozen' exe-file!!!
	win32serviceutil.HandleCommandLine(YourPythonService)
